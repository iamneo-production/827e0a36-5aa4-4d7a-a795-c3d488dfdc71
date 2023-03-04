import streamlit as st
import streamlit as st
import pandas as pd

# Using object notation
add_selectbox = st.sidebar.selectbox(
    "What would you like to see?",
    ("AQI Prediction", "Heatwave prediction")
)
if add_selectbox == "AQI Prediction":

    st.title("AQI Prediction for 2023")


    curr_selection=st.selectbox("Select a Location", ["Adilabad", "Nizamabad", "Warangal", "Karimnagar", "Khammam"])
    # load your DataFrame here for AQI prediction
    df_adilabad=pd.read_csv("PredictionFiles/Adilabadpreds.csv")
    df_nizamabad=pd.read_csv("PredictionFiles/Nizamabadpreds.csv")
    df_warangal=pd.read_csv("PredictionFiles/Warangalpreds.csv")
    df_karimnagar=pd.read_csv("PredictionFiles/Karimnagarpreds.csv")
    df_khammam=pd.read_csv("PredictionFiles/Khammampreds.csv")


    def show(df):
        st.header("Showing for {}".format(curr_selection))
        # select only the 2023 year dates from Date column
        df = df[df['ds'].str.contains('2023')]
        df['ds'] = pd.to_datetime(df['ds'])
        # create a list of unique months in the data
        months = df['ds'].dt.strftime('%Y-%m').unique()
        # create a dropdown menu to select a month
        selected_month = st.selectbox("Select a month", options=months)
        # filter the DataFrame to only include data for the selected month
        subset_df = df[df['ds'].dt.strftime('%Y-%m') == selected_month]
        # rename the columns , ds to Date and 0 to AQI
        subset_df = subset_df.rename(columns={'ds': 'Date', '0': 'AQI'})
        # display the resulting DataFrame in a table
        # drop column index 1
        subset_df = subset_df.drop(subset_df.columns[0], axis=1)
        st.table(subset_df)

        # #show all the data with 2023 year
        # df['ds'] = pd.to_datetime(df['ds'])
        # st.write(df)

    if curr_selection=="Adilabad":
        df=df_adilabad
    elif curr_selection=="Nizamabad":
        df=df_nizamabad
    elif curr_selection=="Warangal":
        df=df_warangal
    elif curr_selection=="Karimnagar":
        df=df_karimnagar
    elif curr_selection=="Khammam":
        df=df_khammam

    show(df)

if add_selectbox == "Heatwave prediction":
    st.title("Heatwave Prediction for 2023")

    curr_selection = st.selectbox("Select a Location", ["Adilabad", "Nizamabad", "Warangal", "Karimnagar", "Khammam"])
    # load your DataFrame here for Heatwave Prediction
    df_adilabad_heat = pd.read_csv("PredictionFiles/AdilabadUrbanMaxTpredict.csv")
    df_nizamabad_heat = pd.read_csv("PredictionFiles/NizamabadMaxTpredict.csv")
    df_warangal_heat = pd.read_csv("PredictionFiles/WarangalMaxTpredict.csv")
    df_karimnagar_heat = pd.read_csv("PredictionFiles/KarimnagarMaxTpredict.csv")
    df_khammam_heat = pd.read_csv("PredictionFiles/KhammamMaxTpredict.csv")

    def show(df):
        st.header("Showing for {}".format(curr_selection))
        # select only the 2023 year dates from Date column
        df = df[df['ds'].str.contains('2023')]
        df['ds'] = pd.to_datetime(df['ds'])
        # create a list of unique months in the data
        months = df['ds'].dt.strftime('%m-%Y').unique()
        # create a dropdown menu to select a month
        selected_month = st.selectbox("Select a month", options=months)
        # filter the DataFrame to only include data for the selected month
        subset_df = df[df['ds'].dt.strftime('%m-%Y') == selected_month]
        # rename the columns , ds to Date and 0 to AQI
        subset_df = subset_df.rename(columns={'ds': 'Date', '0': 'Temperature deg C'})
        # display the resulting DataFrame in a table
        # drop column index 1
        subset_df = subset_df.drop(subset_df.columns[0], axis=1)
        st.table(subset_df)

        # #show all the data with 2023 year
        # df['ds'] = pd.to_datetime(df['ds'])
        # st.write(df)

    if curr_selection == "Adilabad":
        df = df_adilabad_heat
    elif curr_selection == "Nizamabad":
        df = df_nizamabad_heat
    elif curr_selection == "Warangal":
        df = df_warangal_heat
    elif curr_selection == "Karimnagar":
        df = df_karimnagar_heat
    elif curr_selection == "Khammam":
        df = df_khammam_heat

    show(df)

