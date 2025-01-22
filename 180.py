import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    logs['is_consecutive'] = (logs['num'] == logs['num'].shift(1)) & (logs['num'] == logs['num'].shift(-1))
    result = logs[logs['is_consecutive']]['num'].unique()
    result_dataframe = pd.DataFrame({'ConsecutiveNums': result})
    return result_dataframe
