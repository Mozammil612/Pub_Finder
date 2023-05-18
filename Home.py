import streamlit as st
import pandas as pd


st.title('Welcome to Closest Open Pub Finder Page')

df = pd.read_csv('final_data.csv')


st.subheader("Basic Information about the Data.")
st.write(f"Number of Rows: {df.shape[0]}")
st.write(f'Number of Columns: {df.shape[1]}')

st.write("Names of Columns in the dataset:")
st.write(df.columns.T)

st.subheader("Preview of the Data")
st.write("head()")
st.write(df.head())
st.write("tail()")
st.write(df.tail())


# Show some statistics
st.subheader(f"basic statistics about the pubs in uk:")
st.write(df.describe())
