import streamlit as st 
from democlass import Demo as ds
import pandas as pd

st.title('demo')

df = ds()
st.dataframe(df.read_csv().head())

st.plotly_chart(df.plot_box_plot('food'), use_container_width=False, sharing="streamlit")