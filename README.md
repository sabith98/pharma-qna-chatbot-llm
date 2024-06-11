# Pharma QnA Chatbot LLM Project

## Overview

The Pharma QnA Chatbot project is designed to interact with users by converting their pharmaceutical-related questions into SQL queries. These queries are then executed against a MySQL database, and the results are retrieved and presented to the user in an understandable format. This allows users to obtain precise information from the database without needing to know SQL or the underlying database structure.

![Chatbot with results](https://github.com/sabith98/pharma-qna-chatbot-llm/assets/53857418/ded9d5e5-d5c6-41ab-a899-6bb1fd1b833f)

## Prerequisites

- Python 3.x
- MySQL
- pip (Python package installer)

## Setup Instructions

### 1. Clone the Repository

First, clone the project repository to your local machine using the following command:

```bash
git clone https://github.com/sabith98/pharma-qna-chatbot-llm.git
```

### 2. Add .env File

Navigate to the cloned repository and create a .env file in the project root directory. Add the following environment variables to the .env file:

```makefile
GOOGLE_API_KEY=
DB_USER=
DB_PASSWORD=
DB_HOST=localhost
DB_NAME=Pharma
DB_PORT=
```

Replace the placeholder values with your actual database and API credentials.

### 3. Create a New MySQL Database

Log in to your MySQL server and create a new database named Pharma. You can do this using the MySQL command line interface or any MySQL database management tool of your choice.

```sql
CREATE DATABASE Pharma;
```

### 4. Create Tables and Populate Data

Use the SQL scripts provided in the project (if any) or create your own tables and insert necessary data into the Pharma database. Ensure that your database schema matches the requirements of the project.

### 5. Install Project Dependencies

Navigate to the project directory and install the required Python packages using pip

```bash
pip install -r requirements.txt
```

### 6. Run the Application

Start the application by running the following command

```bash
python app.py
```

### 7. Run the Streamlit UI

To launch the Streamlit UI, execute the following command

```
streamlit run app.py
```
