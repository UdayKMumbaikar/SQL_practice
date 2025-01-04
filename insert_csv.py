import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

def insert_csv_to_db(csv_file_path, table_name, db_config):
    # Your existing code for inserting CSV to DB
    pass

try:
    db_config = {
        'dbname': os.getenv('DB_NAME'),
        'user': os.getenv('DB_USER'),
        'password': os.getenv('DB_PASSWORD'),
        'host': os.getenv('DB_HOST'),
        'port': os.getenv('DB_PORT')
    }
    
    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()
    
    csv_file_path = '/path/to/your/csvfile.csv'
    table_name = 'your_table_name'
    
    insert_csv_to_db(csv_file_path, table_name, db_config)
    
    conn.commit()
except Exception as e:
    print(f"Error: {e}")
    if conn:
        conn.rollback()
finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()