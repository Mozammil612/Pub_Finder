import streamlit as st
import folium
from streamlit_folium import folium_static
import pandas as pd

#### 2.Pub Locations
df = pd.read_csv(r'C:\Users\mozammil\final_data.csv')
st.sidebar.title("Pub_Locations")

st.title('Find Pubs by Postal Code or Local Authority')

# Ask the user for the Postal Code or Local Authority
search_type = st.selectbox('Search by:', ('Postal Code', 'Local Authority'))

if search_type == 'Postal Code':
    search_text = st.text_input('Enter the Postal Code:')
    pubs = df[df['postcode'] == search_text]
elif search_type == 'Local Authority':
    search_text = st.text_input('Enter the Local Authority:')
    pubs = df[df['local_authority'] == search_text]

# Show the map
if pubs is not None and not pubs.empty:
    # Get the center of the pubs
    center_lat = pubs['latitute'].mean()
    center_lon = pubs['longitute'].mean()

    # Create the map
    m = folium.Map(location=[center_lat, center_lon], zoom_start=12)

    # Add markers for each pub
    for _, pub in pubs.iterrows():
        folium.Marker(location=[pub['latitute'], pub['longitute']], popup=pub['pub']).add_to(m)

    # Display the map
    folium_static(m)
else:
    st.write('No pubs found.')