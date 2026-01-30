import pandas as pd
from sqlalchemy import create_engine, text

# Database connection settings
DB_USER = "postgres"
DB_PASS = "postgres"
DB_HOST = "db"
DB_PORT = "5432"
DB_NAME = "ny_taxi"

engine = create_engine(f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

# Load Parquet file
parquet_path = "data/green_tripdata_2025-11.parquet"
df_parquet = pd.read_parquet(parquet_path)
df_parquet.to_sql("green_tripdata", engine, if_exists="replace", index=False)

# Load CSV file
csv_path = "data/taxi_zone_lookup.csv"
df_csv = pd.read_csv(csv_path)

# Create table with correct types if not exists
with engine.begin() as conn:
    conn.execute(text("""
        CREATE TABLE IF NOT EXISTS taxi_zone_lookup (
            "LocationID" INTEGER PRIMARY KEY,
            "Borough" TEXT,
            "Zone" TEXT,
            "service_zone" TEXT
        );
    """))

df_csv.to_sql("taxi_zone_lookup", engine, if_exists="replace", index=False)

print("Data loaded successfully.")