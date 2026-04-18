import os
import pandas as pd
import uuid
from sqlalchemy import create_engine, text

DB_HOST = os.getenv("DB_HOST", "127.0.0.1")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "vendor_db")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")

DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL)

query = text("""
    INSERT INTO address(
        id, street, city, state, zip, country, created_by, updated_by
    )
    VALUES (
        :id, :street, :city, :state, :zip, :country, :created_by, :updated_by
    )
""")

params = {
    "id": str(uuid.uuid4()),
    "street": "hello",
    "city": "hello",
    "state": "he",
    "zip": "123456",
    "country": "united",
    "created_by": "000122c4-1b8d-459f-8d16-513530c0a1dd",
    "updated_by": "000122c4-1b8d-459f-8d16-513530c0a1dd"
}


with engine.begin() as conn:
    print(conn.execute(text("select current_database()")).scalar())
    df = pd.read_sql("select * from ticket limit 5", con=conn)
    print(df.head())
    conn.execute(query, params)