import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Even or Odd Check
""")

# def evaluate()

input = st.number_input("Enter a number", step=1)

if st.button('Check'):
     st.write("Even" if input%2==0 else "Odd")
else:
    st.write('')
