import os
import psycopg2
import sqlite3
import csv
from dotenv import load_dotenv

load_dotenv()
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_HOST = os.getenv('DB_HOST')
conn = psycopg2.connect(f'''dbname={DB_NAME}
                        user={DB_USER}
                        password={DB_PASS}
                        host={DB_HOST}''')

cursor = conn.cursor()

create_titanic_table_query = '''
DROP TABLE titanic; 

CREATE TABLE IF NOT EXISTS titanic (
    Survived INT,
    Pclass INT,
    Name TEXT,
    Sex TEXT,
    Age FLOAT,
    Siblings_SpousesAboard INT,
    Parents_ChildrenAboard INT, 
    Fare FLOAT
);
'''
cursor.execute(create_titanic_table_query)
conn.commit()

with open('titanic.csv', 'r') as db:
    next(db)
    cursor.copy_from(db, 'titanic', sep=',')

conn.commit()