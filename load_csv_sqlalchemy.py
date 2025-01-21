import pandas as pd
from sqlalchemy import create_engine
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

# Get list of CSV files in the olist_data directory
olist_data_dir = 'olist_data'
csv_files = [f for f in os.listdir(olist_data_dir) if f.endswith('.csv')]

print("CSV files in olist_data directory:")
for csv_file in csv_files:
    print(csv_file)
    table_name = os.path.splitext(csv_file)[0]  # Remove .csv extension
    print(table_name)

    # Load CSV data into a DataFrame
    csv_file_path = os.path.join(olist_data_dir, csv_file)  
    df = pd.read_csv(csv_file_path)

    # Upload data to the database
    df.to_sql(table_name, engine, if_exists='replace', index=False)

    print(f"Data from {csv_file_path} has been uploaded to the {table_name} table in the database.")