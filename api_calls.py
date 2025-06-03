# Data Ingestion
# This script pulls data from https://api.usaspending.gov/

# Boilerplate
import requests as requests

# Function to get NASA spending by geography for the state of Virginia
def get_spending_by_geography(start_date:str, end_date:str):
    url = "https://api.usaspending.gov/api/v2/search/spending_by_geography/"
    json = {"scope":"recipient_location","geo_layer":"district","geo_layer_filters":["5401","5402","5106","2408","2401","5110","2405","2406","2403","2404","5111","5108","1198","5109","5105","5103","5104","5102","5107","5101"],"filters":{"time_period":[{"start_date":start_date,"end_date":end_date}],"agencies":[{"type":"awarding","tier":"toptier","name":"National Aeronautics and Space Administration"}],"recipient_locations":[{"country":"USA","state":"VA"}]},"subawards":False,"auditTrail":"Map Visualization"}
    response = requests.post(url=url, json=json)

    return response.json()