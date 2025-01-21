import pandas as pd
from sqlalchemy import create_engine, inspect
import os
from dotenv import load_dotenv


load_dotenv()

 # Database connection details from environment variables
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')

# Create the database URL
db_url = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
   

# Create a SQLAlchemy engine
engine = create_engine(db_url)

# Use the inspect module to get table names
inspector = inspect(engine)
tables = inspector.get_table_names()

print("Tables in the database:")
for table in tables:
    print(table)
