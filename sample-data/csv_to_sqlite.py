import sqlite3
import pandas as pd
import os

# Folder containing CSV files
csv_folder = "./data"

# SQLite database file
db_file = "my_database.db"

# Connect to SQLite (creates file if it doesn't exist)
conn = sqlite3.connect(db_file)

# Loop through all CSV files
for file in os.listdir(csv_folder):
    if file.endswith(".csv"):
        file_path = os.path.join(csv_folder, file)

        # Table name = file name without extension
        table_name = os.path.splitext(file)[0]

        # Read CSV
        df = pd.read_csv(file_path)

        # Write to SQLite
        df.to_sql(table_name, conn, if_exists="replace", index=False)

        print(f"Loaded {file} into table '{table_name}'")

# Close connection
conn.close()