import pandas as pd

def transform_data(df):
    # Remove cancelled orders
    df = df[df['status'] != 'Cancelled']

    # Create total amount column
    df['total_amount'] = df['price'] * df['quantity']

    # Convert date column
    df['order_date'] = pd.to_datetime(df['order_date'])

    print("Data Transformed Successfully")
    return df
