import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    email_occurence = person.groupby('email').size().reset_index(name='count')
    # print(email_occurence)
    result = email_occurence[email_occurence['count'] > 1]
    # print(result)
    # print(result[['email']])
    return result.rename(columns={'email': 'Email'})

data = {
    "id": [1, 2, 3],
    "email": ["a@b.com", "c@d.com", "a@b.com"]
}
person_df = pd.DataFrame(data)
print(duplicate_emails(person_df))
