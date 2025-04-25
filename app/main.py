import streamlit as st
from services.standings import get_standings_with_cross_division_ranks

st.set_page_config(page_title="MLB Standings Viewer", layout="wide")
st.title("🏟️ MLB Standings + Cross-Division Rankings")

st.markdown(
    """
    This tool shows current MLB standings and where each team would rank in other divisions.  
    Example: *"The 4th place team in the NL West would be leading any other division..."*
    """
)

standings_df = get_standings_with_cross_division_ranks()

st.dataframe(standings_df, use_container_width=True)




# def main():
#     print("Hello from mlb-standints-app!")


# if __name__ == "__main__":
#     main()
