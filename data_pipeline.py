# Data Pipeline
#


# Boilerplate
import api_calls as api_calls
import pandas as pd

# Instantiate empty list to hold Pandas DataFrames
dfl = []

# Instantiate years list to be iterated over
years = list(range(2010, 2025, 1))

# Iterate over each year and get the relevant data, appending it to dfl
for y in years:
    start_date = f"{y-1}-10-01"
    end_date = f"{y}-09-30"
    json = api_calls.get_spending_by_geography(start_date, end_date)
    df_in = pd.json_normalize(json, record_path='results')
    df_in['year'] = y
    dfl.append(df_in)

# Concactenate the intermediate DataFrames into a single DataFrame
df = pd.concat(dfl)

# Write out df to be used by Quarto dashboard(s)
df.to_csv('data/spending_by_geography.csv')