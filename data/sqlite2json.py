import sqlite3
import json
import csv

# Connect to the database file
db_connection = sqlite3.connect('data.sqlite3')

# Get a cursor object
cursor = db_connection.cursor()

# Execute the SQL query
cursor.execute('SELECT * FROM institutions;')

# Get the results
results = cursor.fetchall()

# Convert the results to a list of dictionaries
data = []

for row in results:
    data.append({
        'id': row[0],
        'source': row[1],
        'university': row[2],
        'data': row[3],
    })


# Close the connection
db_connection.close()

with open('data.csv', 'r') as f:
    reader = csv.reader(f, delimiter=';')
    
    # will skip the header
    next(reader)

    for i, row in enumerate(reader):
        #print(i, row[3])
        data[i]['country'] = row[3]


for row in data:
    row['data'] = json.loads(row['data'])
    
    try:
        row['location'] = row['data'][0]['geometry']['location']
    except:
        row['location'] = None
    #print(row['location'])


# Convert the list of dictionaries to JSON
json_data = json.dumps(data)

# Write the JSON to a file
with open('data.json', 'w') as f:
    f.write(json_data)

# Create a sqlite3 database with the JSON data
db_connection = sqlite3.connect('data_fixed.sqlite3')
cursor = db_connection.cursor()
cursor.execute('DROP TABLE IF EXISTS institutions;')
cursor.execute('CREATE TABLE institutions (id INTEGER PRIMARY KEY, source TEXT, university TEXT, country TEXT, location TEXT, data TEXT);')

for row in data:
    cursor.execute('INSERT INTO institutions VALUES (?, ?, ?, ?, ?, ?);', (row['id'], row['source'], row['university'], row['country'], json.dumps(row['location']), json.dumps(row['data'])))

db_connection.commit()
db_connection.close()
