# -*- coding: utf-8 -*-
"""
Created on Sat May 20 16:33:33 2023

@author: Nariman.J
"""

import pymysql 
import pandas as pd


# Establish connection to MySQL server
cnx = pymysql.connect(
    host='192.168.2.27',
    user='nina',
    password='hotbabe',
)

# Create a cursor object
cur = cnx.cursor()

# Check if the database exists
cur.execute("SHOW DATABASES LIKE 'youtubeDB'")
database_exists = cur.fetchone()

if database_exists:
    print("Database 'youtubeDB' already exists.")
else:
    # Create the database
    cur.execute("CREATE DATABASE youtubeDB")
    print("Database 'youtubeDB' created successfully.")

# Close the cursor and connection
cur.close()
cnx.close()


# # Read data from CSV files
# data1 = pd.read_csv('data1.csv')
# data2 = pd.read_csv('data2.csv')

# # Create the first table
# create_table1_query = '''
# CREATE TABLE table1 (
#     id INT PRIMARY KEY,
#     column1 VARCHAR(50),
#     column2 INT
# )
# '''
# with connection.cursor() as cursor:
#     cursor.execute(create_table1_query)

# # Create the second table
# create_table2_query = '''
# CREATE TABLE table2 (
#     id INT PRIMARY KEY,
#     table1_id INT,
#     column3 FLOAT,
#     FOREIGN KEY (table1_id) REFERENCES table1(id)
# )
# '''
# with connection.cursor() as cursor:
#     cursor.execute(create_table2_query)
    
    



# # Insert data into table1
# with connection.cursor() as cursor:
#     for _, row in data1.iterrows():
#         insert_query = f"INSERT INTO table1 (id, column1, column2) VALUES ({row['id']}, '{row['column1']}', {row['column2']})"
#         cursor.execute(insert_query)

# # Insert data into table2
# with connection.cursor() as cursor:
#     for _, row in data2.iterrows():
#         insert_query = f"INSERT INTO table2 (id, table1_id, column3) VALUES ({row['id']}, {row['table1_id']}, {row['column3']})"
#         cursor.execute(insert_query)
        
        
# # Commit changes and close connection
# connection.commit()
# connection.close()
