import streamlit as st
import pandas as pd
from db import get_all_events

st.set_page_config(page_title="Disaster Dashboard", layout="wide")
st.title("🌍 Real-Time Earthquake Alerts in India")

events = get_all_events()
if events:
    df = pd.DataFrame(events)
    st.map(df[['latitude', 'longitude']])
    st.dataframe(df[['location', 'magnitude', 'timestamp']])
else:
    st.info("No events recorded yet.")