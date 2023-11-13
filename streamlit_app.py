import streamlit as st
from datetime import date

import yfinance as yf
from fbprophet import Prophet
from fbprophet.plot import plot_plotly
from plotly import graph_objs as go

START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

st.title("STOCK PREDICTION APP")

stocks=("Reliance","TCS","HDFC Bank","ICICI Bank","HUL","Infosys","ITC","Bharti Airtel","SBI","Bajaj Finance","Larsen","LIC India","Kotak Mahindra","HCL Tech","Axis Bank","Maruti Suzuki","Asian Paints","Titan","Sun Pharma","Adani Enterpris",
        "Bajaj Finserv","UltraTechCement","ONGC","Avenue Supermar","NTPC","Nestle","Tata Motors","Coal India","Wipro","Power Grid Corp","M&M","JSW Steel","Adani Ports","LTIMindtree","Bajaj Auto","Adani Power","DLF","Adani Green Ene","Tata Steel",
        "Jio Financial","IOC","Hindustan Aeron","HDFC Life","SBI Life Insua","Varun Beverages","Hind Zinc","Grasim","Pidlite Ind","Siemens","Indusind Bank","Britannia","Tech Mahindra","Hindalco","Zomato","Bharat Elc","Power Finance","Bank Of Baroda",
        "Godrej Consumer","Cipla","Eicher Motors","Interglobe Avi","IRFC","Chola Invest.","Shree Cements","Dabur India","Divis Labs","ABB India","Trent","Vedanta","Dr Reddy Labs","REC","PNB","TATA Cons. Prod","Adani Energy","BPCL","GAIL","Ambuja Cement"
        "Union Bank","Macrotech Dev","Tata Power","Bajaj Holdings","Havells India","TVS Motor","Polycab","IOB","United Spirits","ICICI Prudentia","Apollo Hospital","Mankind Pharma","Shriram Finance","Canara Bank","SBI Card","Torrent Pharma","IDBI Bank",
        "SRF","Vodafone Idea","Marico","Berger Paints","ICICI lombard","Jindal Steel")
selected_stocks = st.selectbox("Select dataset for prediction",stocks)

n_years = st.slider("Years of prediction",1,4)
period = n_years * 365
