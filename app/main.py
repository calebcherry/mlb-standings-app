import sys
import os

# Add the project root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from services.standings import fetch_mlb_standings, parse_standings, cross_division_ranks, get_div_leader

# Title
st.title("⚾️ MLB Standings + Cross-Division Rankings 🏟️")

# Description
st.markdown(
    """
    This tool shows current MLB standings and where each team would rank in other divisions.  
    Example: *"The 4th place team in the NL West would be leading any other division..."*
    """
)

# Fetch & process data
with st.spinner("Fetching MLB standings..."):
    raw_data = fetch_mlb_standings()
    # st.json(raw_data)
    standings_df = parse_standings(raw_data)
    ranked_df = cross_division_ranks(standings_df)

# Display the dataframe/standings
st.subheader("📈 Standings and Cross-Division Rankings")
st.dataframe(ranked_df, use_container_width=True)


# TODO: add a visual on the page that shows when the standings are updated and the last time the data was fetched/most recent game played