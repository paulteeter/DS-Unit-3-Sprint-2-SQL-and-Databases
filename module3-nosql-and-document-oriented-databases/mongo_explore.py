
import os
import json
from pdb import set_trace as breakpoint
from dotenv import load_dotenv
import pandas as pd
import psycopg2
from psycopg2.extras import execute_values
import pymongo


load_dotenv() #> loads contents of the .env file into the script's environment

MongoUSER = os.getenv("MongoUSER", default="OOPS")
MongoPASS = os.getenv("MongoPASS", default="OOPS")
MongoNAME = os.getenv("MongoNAME", default='OOPS')

uri = f'mongodb+srv://{MongoUSER}:{MongoPASS}@{MongoNAME}?retryWrites=true&w=majority'
client = pymongo.MongoClient(uri)
print(uri)

# breakpoint()

analytics_db = client.sample_analytics
print(analytics_db.list_collection_names())

# access a specific collection
transactions = analytics_db.transactions
print(transactions.count_documents({}))

# How many customers have more than 50 transactions
print(transactions.count_documents({'transaction_count': {'$gt': 50}}))

# get all customers intoa  dataframe
customers = analytics_db.customers
all_customers = customers.find()

df = pd.DataFrame(all_customers)

# breakpoint()

# Import into MongoDB collection from JSON file

with open('/Users/macuser/Lambda/Unit 3/DS-Unit-3-Sprint-2-SQL-and-Databases/module3-nosql-and-document-oriented-databases/test_data_json.txt') as json_file:
    rpg_data = json.load(json_file)

# Create a new database
rpg_db = client.rpg_data

# Create a collection inside the database
character_table = rpg_db.characters

# Insert many into collection
character_table.insert_many(rpg_data)
print(character_table.count_documents({}))