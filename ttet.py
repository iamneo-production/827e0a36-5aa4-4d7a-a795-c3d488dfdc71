import streamlit as st
import pandas as pd

# load your DataFrame here
df=pd.read_csv("Models_and_Data/predict2.csv") # Predicted values in CSV
df=df.drop(df.columns[0], axis=1)
# select only the 2023 year dates from Date column
df = df[df['Date'].str.contains('2023')]

df['Date'] = pd.to_datetime(df['Date'])
# create a list of unique months in the data
months = df['Date'].dt.strftime('%Y-%m').unique()

# create a dropdown menu to select a month
selected_month = st.selectbox("Select a month", options=months)

# filter the DataFrame to only include data for the selected month
subset_df = df[df['Date'].dt.strftime('%Y-%m') == selected_month]

# display the resulting DataFrame in a table
st.write(subset_df)
# st.table(df)
