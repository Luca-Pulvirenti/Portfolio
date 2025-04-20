import streamlit as st
from Utils import check_connection
import pymysql

pymysql.install_as_MySQLdb()

# Function for set the page configuration 
st.set_page_config(
    page_title="Quaderno3",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Print some text int he Home Page
st.title("Welcome to my Web Application for Managing a Podcast Database.")

# This lines of code are useful for set the buttom for connecting to the database
if check_connection():
    ...
else:
    st.write("Connect the Database before continuing....")




