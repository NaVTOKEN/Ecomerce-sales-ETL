from extract import extract_data
from transform import transform_data
from load import load_data

def run_etl():
    file_path = "../data/sales_data.csv"
    db_path = "../db/ecommerce.db"

    df = extract_data(file_path)
    df = transform_data(df)
    load_data(df, db_path)

if __name__ == "__main__":
    run_etl()
