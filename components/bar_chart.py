import streamlit as st
import random as rd
import pandas as pd

# custom bar_chart
def make_bar_chart(subheader, df):
   #  st.title("Home")
    st.subheader(subheader)
    st.bar_chart(df)