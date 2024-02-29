import os
from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import (
    ChatGoogleGenerativeAI,
    HarmBlockThreshold,
    HarmCategory,
)

from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.example_selectors import SemanticSimilarityExampleSelector

from langchain.prompts.prompt import PromptTemplate
from langchain.prompts import FewShotPromptTemplate
from langchain.chains.sql_database.prompt import PROMPT_SUFFIX
from langchain_community.utilities import SQLDatabase
from langchain.chains import create_sql_query_chain
from langchain_community.tools.sql_database.tool import QuerySQLDataBaseTool


def connect_mysql_db():
    # Check for env variables declared in environment
    required_env_vars = ['DB_USER', 'DB_HOST', 'DB_NAME']
    for var in required_env_vars:
        if not os.getenv(var):
            raise ValueError(f"{var} environment variable is not set properly.")

    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    db_host = os.getenv('DB_HOST')
    db_name = os.getenv('DB_NAME')
    db_port = os.getenv('DB_PORT')

    db = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}", sample_rows_in_table_info=3)
    return db

def load_llm():
    try:
        api_key = os.getenv('GOOGLE_API_KEY')
        if not api_key:
            raise ValueError("Google_API_key environment variable is not set.")

        llm = ChatGoogleGenerativeAI(
            model="gemini-pro",
            google_api_key=api_key,
            safety_settings={
                HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
            }
        )
        return llm
    except Exception as e:
        raise RuntimeError(f"Failed to load language model: {e}")

def store_and_select_example_vectors(few_shots):
    try:
        embeddings = HuggingFaceEmbeddings()
        to_vectorize = [" ".join(example.values()) for example in few_shots]
        vectorstore = Chroma.from_texts(to_vectorize, embeddings, metadatas=few_shots)
        example_selector = SemanticSimilarityExampleSelector(
            vectorstore=vectorstore,
            k=2,
        )
        return example_selector
    except Exception as e:
        raise RuntimeError(f"Failed to store and select example vectors: {e}")
    
def create_few_shot_prompt(example_selector):
    mysql_prompt = """You are a MySQL expert. Given an input question, first create a syntactically correct MySQL query to run, then look at the results of the query and return the answer to the input question.
    If the question explicitly asks to list down all relevant entries without limiting them, do not use the LIMIT clause, and retrieve all matching entries.
    Unless the user specifies in the question a specific number of examples to obtain, query for at most {top_k} results using the LIMIT clause as per MySQL. You can order the results to return the most informative data in the database.
    Never query for all columns from a table. You must query only the columns that are needed to answer the question. Wrap each column name in backticks (`) to denote them as delimited identifiers.
    Pay attention to use only the column names you can see in the tables below. Be careful to not query for columns that do not exist. Also, pay attention to which column is in which table.
    Pay attention to use CURDATE() function to get the current date, if the question involves "today".

    Use the following format:

    Question: Question here
    SQLQuery: Query to run with no pre-amble
    SQLResult: Result of the SQLQuery
    Answer: Final answer here

    No pre-amble.
    """

    example_prompt = PromptTemplate(
        input_variables=["Question", "SQLQuery", "SQLResult","Answer",],
        template="\nQuestion: {Question}\nSQLQuery: {SQLQuery}\nSQLResult: {SQLResult}\nAnswer: {Answer}",
    )

    few_shot_prompt = FewShotPromptTemplate(
        example_selector=example_selector,
        example_prompt=example_prompt,
        prefix=mysql_prompt,
        suffix=PROMPT_SUFFIX,
        input_variables=["input", "table_info", "top_k"],
    )

    return few_shot_prompt

def generate_result(llm, db, few_shot_prompt, question):
    try:
        execute_query = QuerySQLDataBaseTool(db=db)
        query_chain = create_sql_query_chain(llm, db, prompt=few_shot_prompt)
        query = query_chain.invoke({"question": question})
        result = execute_query(query)
        return query, result
    except Exception as e:
        raise RuntimeError(f"Failed to generate result: {e}")

def format_result(query, result, llm):
    try:
        prompt_template = """
        Based on the query and result, Please convert the given result into 
        a format suitable for display in a Pandas DataFrame with appropriate 
        column names. If the output cannot be displayed in a DataFrame, 
        please provide a simple natural language response.

        SQL Query: {query}
        Results: {result}
        """

        prompt = prompt_template.format(query=query, result=result)
        response = llm.invoke(prompt)
        return response.content
    except Exception as e:
        raise RuntimeError(f"Failed to format response: {e}")