import streamlit as st
import pandas as pd


header = st.container()
introduction = st.container()

with header:
    st.title("This is my streamlit App")
    st.text("This is where you write descriptions about the header")


with introduction:
    st.header("Introduction to using streamlit")