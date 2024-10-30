import pandas as pd
import sqlite3
import json

# Load the Excel file
file_path = './Landmark_Phuket_TableToExce.xls'
df = pd.read_excel(file_path)

# Convert the DataFrame to JSON
json_data = df.to_json(orient='records')

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('../landmark_phuket.db')
cursor = conn.cursor()

# Create table structure with updated column names
cursor.execute('''
    CREATE TABLE IF NOT EXISTS landmarks (
        FID INTEGER,
        qc_id TEXT,
        objectid INTEGER,
        sub_code TEXT,
        name TEXT,
        location_e TEXT,
        Landmark_N TEXT,
        Landmark_L TEXT
    )
''')

# Insert each row from JSON into the database
data = json.loads(json_data)
for record in data:
    cursor.execute('''
        INSERT INTO landmarks (FID, qc_id, objectid, sub_code, name, location_e, Landmark_N, Landmark_L)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        record.get('FID'), 
        record.get('qc_id'), 
        record.get('objectid'), 
        record.get('sub_code'), 
        record.get('name'), 
        record.get('location_e'), 
        record.get('Landmark_N'), 
        record.get('Landmark_L')
    ))

# Commit and close
conn.commit()
conn.close()

print("Data successfully inserted into database.")