import pandas as pd
import httpx

def fetch_mlb_standings():
    url = "https://site.api.espn.com/apis/site/v2/sports/baseball/mlb/standings"
    response = httpx.get(url)
    response.raise_for_status()  # Raise an error for bad responses
    return response.json()


# TODO: Write code to parse the standings data
def parse_standings(raw_data):
    teams = []:
    for group in raw_data["children"]:
        division_name = group["name"]:
        for team_entry in group["standings"]["entries"]:
            






