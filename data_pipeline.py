import api_calls as api_calls
import pandas as pd

dfl = []
year_list = [2020, 2021, 2022, 2023, 2024]
for y in year_list:
    start_date = f"{y-1}-10-01"
    end_date = f"{y}-09-30"
    json = api_calls.get_spending_by_geography(start_date, end_date)
    df_in = pd.json_normalize(json, record_path='results')
    df_in['year'] = y
    dfl.append(df_in)

df = pd.concat(dfl)

df.to_csv('data/spending_by_geography.csv')