# https://leetcode.com/problems/nth-highest-salary/description/
import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    unique_salaries = employee['salary'].drop_duplicates()

    highest_to_lowest = unique_salaries.sort_values(ascending=False)
    
    if N > len(highest_to_lowest) or N <= 0:
        return pd.DataFrame({f'getNthHighestSalary({N})' : [None]})

    nth_highest_salary = highest_to_lowest.iloc[N - 1]

    return pd.DataFrame({f'getNthHighestSalary({N})': [nth_highest_salary]})

