# https://leetcode.com/problems/combine-two-tables/description/
import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    result = pd.merge(person, address, how='left', on='personId')
    return result[['firstName', 'lastName', 'city', 'state']]

