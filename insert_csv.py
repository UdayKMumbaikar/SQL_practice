import os
from dotenv import load_dotenv
import psycopg2
import csv

load_dotenv()

def insert_csv_to_db(csv_file_path, table_name, db_config):
    # Your existing code for inserting CSV to DB
    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()
    
    with open(csv_file_path, 'r') as f:
        reader = csv.reader(f)
        headers = next(reader)
        query = f"INSERT INTO {table_name} ({', '.join(headers)}) VALUES %s"
        
        for row in reader:
            cursor.execute(query, (tuple(row),))
    
    conn.commit()
    cursor.close()
    conn.close()

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
    
    # csv_file_path = os.path.join(os.getcwd(), 'olist_data','olist_geolocation_dataset.csv')
    # table_name = 'olist_geolocation_dataset'


    csv_file_path = os.path.join(os.getcwd(), 'olist_data','olist_customers_dataset.csv')
    table_name = 'olist_customers_dataset'
    
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