import pandas as pd

def load_data():
    emp = pd.read_csv('employees.csv')
    sys_access = pd.read_csv('system_access.csv')

    return emp, sys_access

def correct_id(df):
    df.rename(columns={'id':'employee_number'}, inplace=True)
    df['employee_number'] = 'EMP' + df['employee_number'].astype(str).str.zfill(6)

    return df

def join_data(emp, sys_access):
    emp.set_index('employee_number', inplace = True)
    sys_access.set_index('employee_number', inplace = True)
    df = emp.join(sys_access)

    return df
