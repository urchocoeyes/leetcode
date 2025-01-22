import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    employee = employee.merge(employee, left_on='managerId', right_on='id', suffixes=('', '_manager'))
    result = employee[employee['salary'] > employee['salary_manager']]
    return result[['name']].rename(columns={'name': 'Employee'})
