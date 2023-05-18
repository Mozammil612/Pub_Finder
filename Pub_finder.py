import streamlit as st
import folium
from streamlit_folium import folium_static
import pandas as pd


df = pd.read_csv('final_data.csv')

st.sidebar.title("Find the nearest Pub")

st.title("Know the Nearest Pubs in Your Area")


# Ask the user for their location
lat = st.text_input("Enter your latitude:")
lon = st.text_input("Enter your longitude:")

# Convert the user's location to floats, checking for empty input
if lat and lon:
    lat = float(lat)
    lon = float(lon)

    # Compute the Euclidean distance between the user's location and each pub's location
    df['dist'] = ((df['latitute'] - lat) ** 2 + (df['longitute'] - lon) ** 2) ** 0.5

    # Select the nearest 5 pubs
    nearest_pubs = df.sort_values(by='dist').head(5)
    for _, pub in nearest_pubs.iterrows():
        
        st.write(f"Distance: {pub['dist']:.2f} km")
        st.write("")




    # Create a map and add markers for each of the nearest pubs
    m = folium.Map(location=[lat, lon], zoom_start=12)

    for _, pub in nearest_pubs.iterrows():
        folium.Marker(location=[pub['latitute'], pub['longitute']], popup=pub['pub']).add_to(m)

    folium_static(m)
else:
    st.write("Please enter your latitude and longitude.")
