# Definition of functions and commands to connect to the database.
import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text

# Useful information about the database
dialect = "mysql"
username = "root"
password = ""
host = "localhost"
dbname = "db_quaderno3" # modify with your database name

# - connect_db(dialect,username,password,host,dbname): connects to the db.
    # displays an error if it fails.
def connect_db(dialect,username,password,host,dbname):
    try:    
        engine = create_engine(f'{dialect}://{username}:{password}@{host}/{dbname}')
        return engine.connect()
    except Exception as e:
        print(e)
        return False

# execute_query(conn,query): function which given a connection and a query executes it.
def execute_query(conn,query):
        try:
            with conn.begin():
                return conn.execute(text(query))
        except Exception as e:
            st.write(e)
            return False

# check_connection(): 
''''' a function that when called will initialise a connection state to False if not initialised (st.session_state). 
      In case the connection has not yet been made displays a button in the sidebar to connect to the db. 
      When the button is pressed it should connect to the db and display a success or error message 
      depending on the result of the connection. 
      The function returns True if the connection is active if not False 
      '''''
def check_connection():
    if 'connection' not in st.session_state:
        st.session_state['connection'] = False
        
    if st.button('Connessione al Database'):
        st.session_state['connection'] = connect_db(dialect,username,password,host,dbname)
        if not st.session_state['connection']:
            st.error("Connessione Fallita.")
        else:
            st.success("Connessione Riuscita.")
    
    if st.session_state['connection']:
        return True
    else:
        return False
