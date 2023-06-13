import sqlite3 as sq
import pandas as pd

connection = sq.connect('db.sqlite3')
curs = connection.cursor()
  
# Load CSV data into Pandas DataFrame
data = pd.read_csv('data.csv')
 
# Write the data to a sqlite db table
data.to_sql('api_api', connection, if_exists='replace', index=False)
   
# Run select sql query
curs.execute('select * from api_api')
 
# Fetch all records
# as list of tuples
records = curs.fetchall()
 
# Display result 
for row in records:
    # show row
    print(row)
     
# Close connection to SQLite database
connection.close()