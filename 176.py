# https://leetcode.com/problems/second-highest-salary/description/
import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee = employee['salary'].drop_duplicates()
    employee.sort_values(ascending=False)
    if len(employee) == 1:
        return pd.DataFrame({'SecondHighestSalary' : [None]})
    second_salary = employee.iloc[1]
    return pd.DataFrame({'SecondHighestSalary' : [second_salary]})
    # approach
    # dont have duplicates
    # sort by descending order salary
    # choose second row(first index)