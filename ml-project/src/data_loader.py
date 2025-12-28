import pandas as pd
from sklearn.model_selection import train_test_split

def load_csv(file_path:str):
    try:
        df = pd.read_csv(file_path)
        # print(f'Data Loaded successfull {df.shape}\n{df.head()}')
        return df
    
    except FileNotFoundError:
        print('File Not Exist')


def split_data(df):
    try:
        X = df.drop(columns=['satisfaction'])
        Y = df['satisfaction']

        X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.21, random_state=42)
        print(f'Size of X_train: {X_train.shape}\nSize of X_test: {X_test.shape}')
        return X_train, X_test, y_train, y_test
    
    except Exception as e:
        print('Error while Splitting the data ', e)
        
