import numpy as np 
import pandas as pd
import streamlit as st
import urllib3
from io import StringIO

http = urllib3.PoolManager()

st.title("COVID-19 Data App with streamlit")
st.header("Covid data of World")


response = http.request("GET", "https://disease.sh/v3/covid-19/all?yesterday=true")

result = str(response.data, "utf-8")

data = StringIO(result)

df = pd.read_json(data)

opts = st.multiselect("Choose the columns", 
["cases","todayCases","deaths","todayDeaths","recovered","todayRecovered","active"])

chart_data = pd.DataFrame({
	'updated' : df['updated'],
	  'cases': df['cases'],
	  'todayCases': df['todayCases'],
	  'deaths': df['deaths'],
	  'todayDeaths': df['todayDeaths'],
	  'recovered': df['recovered'],
	  'todayRecovered': df['todayRecovered'],
	  'active': df['active'],
	  'population': df['population'],
}, index=[0])



st.text("Corona Line Chart")
st.line_chart(chart_data)


st.text("Corona Barchart")
st.bar_chart(chart_data)

st.text("Corona area Chart")
st.area_chart(chart_data)


st.subheader("Data Frame")
st.write(chart_data)
