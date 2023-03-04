# AQI and Heatwave Prediction- StellarHackers
Use the Link for Live Demo- https://abhinandanroul-827e0a36-5aa4-4d7a-a795-c3d488dfdc71-main-1rmle1.streamlit.app/ <br>
The PDF- https://drive.google.com/drive/folders/1boXHBMH1thsVF6GClaBYPPODhWB09ru2?usp=sharing

## About the Project-
This project uses AR-Net (Neuralprophet), a neural network-based forecasting library, to predict heatwaves🔥 and air✨ quality. The goal of this project is to create a model that can accurately predict the occurrence of heatwaves and poor air quality to help people prepare for and mitigate the effects of extreme weather events.

## Data
The data used for this project is sourced from publicly available datasets. The datasets include historical weather data, air quality data, and other relevant environmental variables. The data is pre-processed and formatted for use with NeuralProphet.

## NeuralProphet
NeuralProphet is a neural network-based forecasting library built on top of PyTorch. It allows for flexible data input and supports a range of forecasting tasks such as time series forecasting and anomaly detection. NeuralProphet is designed to handle time series data with missing values and seasonality.
- Support for auto-regression and covariates.
- Automatic selection of training related hyperparameters.
- Fourier term seasonality at different periods such as yearly, daily, weekly, hourly.
- Plotting for forecast components, model coefficients and final predictions.

## Project Structure
The project is structured as follows:

Models_and_Data : Contains the models, jupyternotebooks and prediction data
notebooks: contains Jupyter notebooks for data exploration, model training, and model evaluation
requirements.txt: contains the Python dependencies required to run the project

# Getting Started
To get started with this project, you will need to clone the repository and install the Python dependencies listed in requirements.txt. Once the dependencies are installed, you can explore the Jupyter notebooks in the notebooks directory to see how the model is trained and evaluated.

## Screenshots-
<p float="left">
<img src = "https://i.imgur.com/AaqRfLF.png" width=500>
<img src= "https://i.imgur.com/cuIq4sn.png" width=500>
<img src="https://i.imgur.com/eD0a2Px.png" width=500>
</p>
The Fig 1. (Left) Shows the Trends and Seasonality, Fig 2. (Right) Shows the prediction vs actual data (the model fitting), Fig 3. (Bottom) Shows the correlation heatmap


## Conclusion
In this project, we have used NeuralProphet to predict heatwaves and air quality. The model is trained on pre-processed data and is designed to handle missing values and seasonality. The project structure allows for easy exploration and modification of the model. With further refinement and tuning, this model can be used to provide valuable insights and predictions for people living in areas prone to extreme weather events.

https://sonarcloud.io/summary/overall?id=examly-test_827e0a36-5aa4-4d7a-a795-c3d488dfdc71



