import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    result = pd.DataFrame(columns=['id'])
    for i in weather.shape[0]:
        if weather.loc[i] < weather.loc[i + 1]:
            result.loc[len(result)] = {'id': i + 1}  # Adds row at the next available index

