import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    result = customers.merge(orders, how='left', left_on='id', right_on='customerId')
    return pd.DataFrame(result[result['id_y'].isna()]['name'].rename('Customers'))
