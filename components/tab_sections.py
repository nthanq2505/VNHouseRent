import streamlit as st

def make_tab_sections():
   st.subheader('Tabs')
   tab1, tab2 = st.tabs(["TAB 1", "TAB 2"])

   with tab1:
      st.write('WOW!')
      st.image("https://i.gifer.com/DJR3.gif", width=400)

   with tab2:
      st.write('Do you like ice cream? 🍨')
      agree = st.checkbox('Yes! I love it')
      disagree = st.checkbox("Nah! 😅")
      if agree:
         st.write('Even I love it 🤤')
      if disagree:
         st.write('You are boring 😒')