import sqlite3

def load_data(df, db_path):
    conn = sqlite3.connect(db_path)
    df.to_sql("sales", conn, if_exists="replace", index=False)
    conn.close()

    print("Data Loaded to SQLite Successfully")
