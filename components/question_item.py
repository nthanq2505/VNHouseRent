import streamlit as st
import pandas as pd

from constants.index import list_questions

def question_one(df):
   st.subheader(list_questions[0])
   st.write("The bar chart below shows the number of houses for rent in each district of Ho Chi Minh City.")
   st.bar_chart(df['district'].value_counts())
   
def question_two():
   st.subheader(list_questions[1])
   
def question_three():
   st.subheader(list_questions[2])

def question_four():
   st.subheader(list_questions[3])
   