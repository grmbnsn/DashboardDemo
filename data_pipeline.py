import api_calls as api_calls
import pandas as pd

dfl = []
years = list(range(2010, 2025, 1))

for y in years:
    start_date = f"{y-1}-10-01"
    end_date = f"{y}-09-30"
    json = api_calls.get_spending_by_geography(start_date, end_date)
    df_in = pd.json_normalize(json, record_path='results')
    df_in['year'] = y
    dfl.append(df_in)

df = pd.concat(dfl)

df.to_csv('data/spending_by_geography.csv')