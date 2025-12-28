import pandas as pd
from sklearn.preprocessing import StandardScaler, OrdinalEncoder
from src.data_loader import split_data, load_csv

#Remove Unwanted Columns- Unnamed: 0, id
def remove_column(df):
    try:
        df.drop(columns=['Unnamed: 0', 'id'], inplace=True)
        return df
    
    except Exception as e:
        print('Unable to get the file', e)

def mapping_column(df):
    if 'satisfaction' in df.columns:
        df['satisfaction'] = df['satisfaction'].map({
            'neutral or dissatisfied':0,
            'satisfied': 1 
            })
        
    if 'Gender' in df.columns:
        df['Gender'] = df['Gender'].map({
            'Female':0,
            'Male': 1
            })
    return df


def fill_missing_values(df):
    #Fill the missing values in the column
    df['Arrival Delay in Minutes'] = df['Arrival Delay in Minutes'].fillna(df['Arrival Delay in Minutes']).median()
    return df

#Preprocess the data basically to create a single column rather than use it differently
def create_column(df):

    df['Flight Service'] = df[
        ['Inflight wifi service', 'Food and drink','Seat comfort','Inflight entertainment',
         'Leg room service','Baggage handling','Inflight service',
         'Cleanliness']
         ].mean(axis=1)
    
    df['Total_delayed'] = df['Departure Delay in Minutes'] + df['Arrival Delay in Minutes']

    df['Online Services'] = df[
        ['Ease of Online booking', 'Online boarding', 
         'On-board service', 'Checkin service']
         ].mean(axis=1)
    
    return df


def drop_columns(df):
    drop_cols = ['Inflight wifi service', 'Food and drink','Seat comfort','Inflight entertainment',
                 'Leg room service','Baggage handling','Inflight service','Cleanliness', 'Departure Delay in Minutes', 
                 'Ease of Online booking','Arrival Delay in Minutes','Online boarding', 'On-board service', 'Checkin service']
    
    df.drop(columns=drop_cols, inplace=True)
    return df


def categorical_encode(X_train, X_test):
    cat_cols = ['Customer Type', 'Type of Travel', 'Class']

    encoder = OrdinalEncoder()

    X_train[cat_cols] = encoder.fit_transform(X_train[cat_cols])
    X_test[cat_cols] = encoder.transform(X_test[cat_cols])

    return X_train, X_test

#Dropping columns with low scores[Use Random Forest to calculate the Important Feature]
def drop_low_importance_columns(X_train, X_test):
    
    cols_to_drop = [
        'Departure/Arrival time convenient',
        'Departure Delay in Minutes',
        'Gate location',
        'Gender'
    ]

    X_train.drop(columns=cols_to_drop, inplace=True, errors='ignore')
    X_test.drop(columns=cols_to_drop, inplace=True, errors='ignore')
    return X_train, X_test


def final_preprocess(df):
    try:
        df = remove_column(df)
        df = mapping_column(df)
        df = fill_missing_values(df)
        df = create_column(df)
        df = drop_columns(df)
        X_train, X_test, y_train, y_test = split_data(df)
        # print(f'Split completed\n{X_train.shape}\n{X_test.shape}\{X_train.head()}')
        categorical_encode(X_train, X_test)
        drop_low_importance_columns(X_train, X_test)

        print(X_train)

        return X_train, X_test, y_train, y_test
        
    except Exception as e:
        print('Successful Done', e)




