import os
import time
import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError

DB_HOST = os.getenv("DB_HOST", "db")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "vendor_db")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")

DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)

for attempt in range(10):
    try:
        with engine.connect() as conn:
            print("Connected to database.")
        break
    except OperationalError:
        print(f"Database not ready yet, retrying... ({attempt + 1}/10)")
        time.sleep(3)
else:
    raise RuntimeError("Could not connect to the database.")

csv_folder = "./data"
load_order = [
    "user",
    "address",
    "client",
    "vendor",
    "services",
    "vendor_user",
    "contractors",
    "vendor_contractor",
    "client_user",
    "client_vendor",
    "background_check",
    "drug_test",
    "licenses",
    "certifications",
    "insurance",
    "compliance_document",
    "msa",
    "msa_requirements",
    "well",
    "well_location",
    "vendor_services",
    "vendor_well",
    "work_orders",
    "ticket",
    "invoice",
    "line_item",
    "contractor_performance",
]
with engine.begin() as conn:
    conn.execute(text("SET CONSTRAINTS ALL DEFERRED;"))

    for table_name in load_order:
        file_path = os.path.join(csv_folder, f"{table_name}.csv")

        if not os.path.exists(file_path):
            continue

        df = pd.read_csv(file_path)

        df.to_sql(table_name, conn, if_exists="append", index=False)

        print(f"Loaded {table_name}")