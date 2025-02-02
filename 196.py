import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    # smallest id and one email
    # inplace=True
    # order of Person table doesnt matter
    person.sort_values(by='id', ascending=True, inplace=True)
    person.drop_duplicates(subset='email', keep='first', inplace=True)