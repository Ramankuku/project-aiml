import sqlite3
import pandas as pd
import os


def save_to_sqlite(file_path, table_name, db_name):
    try:
        df = pd.read_csv(file_path)
        print('File Loaded', df.shape)

        with sqlite3.connect(db_name) as conn:
            df.to_sql(
                name = table_name,
                con = conn,
                if_exists='replace',
                index=False
            )    
    except FileNotFoundError:
        print("File not Found")


def main():
    file_path = r"D:\\Projects\\Airline Passenger Satisfaction Dataset\\data\\train.csv"
    table_name = 'airplane_passenger'
    db_name = 'data.db'
    save_to_sqlite(file_path, table_name, db_name)

if __name__ == '__main__':
    main()

