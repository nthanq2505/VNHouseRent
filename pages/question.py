import streamlit as st
import pandas as pd

from components import question_item

df_house_rent = pd.read_csv('./data/HCMHouseRentPreprocessing.csv')

def app():
   st.title("Asking meaningful questions that need to be answered")
   option = st.selectbox(
      'How would you like to be contacted? 💔',
      ('Question 1', 'Question 2', 'Question 3', 'Question 4', 'Question 5', 'Question 6', 'Question 7', 'Question 8')
   )
   
   if option == 'Question 1':
      question_item.question_one(df_house_rent)
   elif option == 'Question 2':
      question_item.question_two()
   elif option == 'Question 3':
      question_item.question_three()
   elif option == 'Question 4':
      question_item.question_four()
   # elif option == 'Question 5':
   #    question(5)
   # elif option == 'Question 6':
   #    question(6)
   # elif option == 'Question 7':
   #    question(7)
   # elif option == 'Question 8':
   #    question(8)