import os  
import dotenv  
import openai  
import psycopg2  
  
# Load environment variables  
dotenv.load_dotenv()  
  
# Set the OpenAI Azure API endpoint and key  
openai.api_type = "azure"  
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")  
openai.api_key = os.getenv("AZURE_OPENAI_API_KEY")  
  
# Set the deployment name (Azure's equivalent of the model name)  
deployment = os.getenv("DEPLOYMENT_NAME", "gpt-4o")  
  
# Connect to PostgreSQL database  
import psycopg2
import os

# Define connection parameters using your provided host and username
host = "db.postgres.database.azure.com"   # Your Azure PostgreSQL server hostname
database = "postgres"               # Replace with your actual database name
user = "user@db"                     # Username must be in the format 'username@server-name'
password = ""                    # Replace with your actual password
port = "5432"                                 # Default PostgreSQL port

from psycopg2 import sql  
import csv

# Update connection string information

dbname = "" 
user = ""
sslmode = "require"

# Construct connection string

conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)
conn = psycopg2.connect(conn_string)
print("Connection established")
cursor = conn.cursor()

with open('instruct1.txt', 'r') as file:
    # Read the content of the file
    instruct1 = file.read()

with open('instruct2.txt', 'r') as file:
    # Read the content of the file
    instruct2 = file.read()
  
def generate_sql_query(user_input):  
    response = openai.ChatCompletion.create(  
        engine=deployment,  
        messages=[  
            {"role": "system", "content": instruct1+"\nYour job is only to give SQL query, noneed to explain"},  
            {"role": "user", "content": user_input},  
        ],  
        max_tokens=800,  
        temperature=0.4,  
        stream=False,  
    )  
    res = response.choices[0].message["content"]  
    res = res.replace("```sql", "")
    res = res.replace("```", "")
    res = res.replace("\n", " ")
    return res
  
def filter_response(user_input, data):  
    response = openai.ChatCompletion.create(  
        engine=deployment,  
        messages=[  
            {"role": "system", "content": instruct2},  
            {"role": "user", "content": user_input + "\n" + data},  
        ],  
        max_tokens=800,  
        temperature=0.4,   
        stream=True,  
    )  
    for chunk in response:  
        try:
            print(chunk.choices[0].delta.get("content", ""), end="", flush=True)  
        except:  
            pass
    print()  
  
while True:  
    try:  
        # Phase 1: User Input  
        user_input = input("Enter your query (or 'exit' to quit): ")  
        if user_input.lower() == 'exit':  
            break  
  
        # Generate SQL Query  
        sql_query = generate_sql_query(user_input)  
        print(f"Generated SQL Query: {sql_query}")  
  
        # Phase 2: Execute SQL Query  
        cursor.execute(sql_query)  
        rows = cursor.fetchall()  
  
        # Prepare data for filtering  
        data = "\n".join([str(row) for row in rows])  
        print(f"Database Rows: {data}")  
  
        # Phase 3: Filter and Present Response  
        filtered_response = filter_response(user_input, data)  
        print(f"Filtered Response: {filtered_response}")  
  
    except Exception as e:  
        print(f"An error occurred: {e}")  
  
# Close the database connection  
cursor.close()  
conn.close()  
