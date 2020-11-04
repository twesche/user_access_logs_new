import pandas as pd

def find_missing(df):
    missing = df.loc[df['access_level'].isnull()]

    return missing

def map_update(df, emp_title, new_access):
    df.loc[df['title'] == emp_title, 'access_level'] = new_access
    return df

def output_results(df):
    df.to_csv('results.csv')
