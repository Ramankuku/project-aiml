import sqlite3
import pandas as pd


def save_csv_tosqlite(file_path, db_name, table_name):
    try:
        df = pd.read_csv(file_path)
        print('loaded')
        with sqlite3.connect(db_name) as conn:
            df.to_sql(
                name=table_name,
                con=conn,
                if_exists='replace',
                index = False
            )
            print('Sucess')
    except FileNotFoundError:
        print('File Not Exist')

def check_table_exists(db_name):
    with sqlite3.connect(db_name) as conn:
        query = """
        SELECT name FROM sqlite_master 
        WHERE type='table' AND name='airline_passenger_satisfaction_data';
        """
        result = pd.read_sql(query, conn)
        print("Table exists:" if not result.empty else "Table NOT found")

def check_row_count(db_name, table_name):
    with sqlite3.connect(db_name) as conn:
        df = pd.read_sql(
            f"SELECT COUNT(*) AS total_rows FROM {table_name}",
            conn
        )
        print("Total rows:", df.loc[0, "total_rows"])

def preview_data(db_name, table_name):
    with sqlite3.connect(db_name) as conn:
        df = pd.read_sql(
            f"SELECT * FROM {table_name} LIMIT 5",
            conn
        )
        print(df)

def main():
    file_path = r"D:\\Projects\\Airline Passenger Satisfaction Dataset\\data\\train.csv"
    db_name = "data.db"
    table_name = "airline_passenger_satisfaction_data"

    save_csv_tosqlite(file_path, db_name, table_name)
    check_table_exists(db_name)
    check_row_count(db_name, table_name)
    preview_data(db_name, table_name)


if __name__ == "__main__":
    main()
