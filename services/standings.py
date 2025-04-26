import pandas as pd
import httpx
import pybaseball

def fetch_mlb_standings():
    url = "https://site.api.espn.com/apis/site/v2/sports/baseball/mlb/standings"
    response = httpx.get(url)
    response.raise_for_status()  # Raise an error for bad responses
    return response.json()


# TODO: Write code to parse the standings data
def parse_standings(raw_data):
    teams = []
    for div in raw_data["records"]:
        division_id = div['division']['id']
        for team_entry in div['teamRecords']:
            team = team_entry['team']['name']
            team_id = team_entry['team']['id']
            wins = team_entry['leagueRecord']['wins']
            losses = team_entry['leagueRecord']['losses']
            win_percentage = team_entry['leagueRecord']['pct']
            games_back = team_entry['gamesBack']
            division_rank = team_entry['divisionRank']
            league_rank = team_entry['leagueRank']
            mlb_rank = team_entry['sportRank']
            games_played = team_entry['gamesPlayed']
            teams.append({
                'team': team,
                'team_id': team_id,
                'wins': wins,
                'losses': losses,
                'win_percentage': win_percentage,
                'games_back': games_back,
                'division_id': division_id,
                'division_rank': division_rank,
                'league_rank': league_rank,
                'mlb_rank': mlb_rank,
                'games_played': games_played
            })
    return pd.DataFrame(teams)

def get_div_leader(df):
    div_leader = df.loc[df.groupby('division_id')['division_rank'].idxmin()]
    return div_leader.reset_index(drop=True)

def cross_division_ranks(df):
    division_leaders = get_div_leader(df)
    division_leaders = division_leaders.set_index('division_id')

    results = []
    for idx, team_row in df.iterrows():
        team_result = team_row.to_dict()
        for div_id, leader_row in division_leaders.iterrows():
            if team_row['division_id'] == div_id:
                continue  # Skip their own division
            is_better = int(team_row['mlb_rank']) < int(leader_row['mlb_rank'])
            col_name = f"would_lead_{div_id}"
            team_result[col_name] = is_better
        results.append(team_result)

    return pd.DataFrame(results)

# TODO: Include logic to show when team doesn't have as many games played and highlight or add asterisk


