import streamlit as st

from helpers import (
    load_llm, 
    connect_mysql_db,
    store_and_select_example_vectors,
    create_few_shot_prompt,
    generate_result,
    format_result,
)
from few_shots import few_shots

from dotenv import load_dotenv
load_dotenv()

llm = load_llm()

db = connect_mysql_db()

example_selector = store_and_select_example_vectors(few_shots)

few_shot_prompt = create_few_shot_prompt(example_selector)

st.header(f"Business chatbot")

## Generate result
question = st.text_input("Ask your question")

checkbox = st.checkbox('Display SQL query')

if st.button("Ask"):
    try:
        query, result = generate_result(llm=llm, db=db, few_shot_prompt=few_shot_prompt, question=question)
    
        if checkbox:
            st.caption(f"SQL Query")
            st.code(query, language='sql')
        
        ## display the results
        formatted_result = format_result(query, result, llm)
        st.caption("Result")
        st.write(formatted_result)
    except Exception as e:
        raise RuntimeError(f"Failed to display results")







