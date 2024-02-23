'''
Data entry in the database

Develop a page that contains all the fields necessary for the entry of a
new appearance of a person (existing or new) at an existing podcast in the database
(insertion of a record in the apparition table).

If the person is an existing person, it is sufficient to enter his or her tax code.

If the person is new, all fields must be entered (insertion of a record in the table
PERSON)

The selection of the podcast code should be done via a drop-down menu generated from the content of the
table of the database. The insertion form must fulfil the following constraints:
A specific error message must be generated in case of missing data (empty fields) or incorrectly
typed correctly (incorrect data format). In the event of errors, the page must notify the
relevant error.

A specific error message must be generated in the event that the end time of appearance is earlier
the start time of the appearance.

If the person cannot be entered, the entry of the appearance must not be made.
If the insertion ends successfully, the form should display a message of successful insertion
with a message informing about the total number of appearances of the person, otherwise it must
notify the error with the reason for the failed entry '''

import streamlit as st
import pandas as pd
from Utils import execute_query

# Create entry cells for the fields required to enter a
# new appearance of a person (existing or new) at an existing podcast in the database
# (inserting a record in the Appearance table).

CodiceFiscale = st.text_input("Codice Fiscale")

query_CodFiscale = f'''SELECT * FROM PERSONA WHERE CodiceFiscale = '{CodiceFiscale}' '''
result_CodFiscale = execute_query(st.session_state['connection'],query_CodFiscale)
df_CodFiscale = pd.DataFrame(result_CodFiscale)

if 'button_clicked_CodFiscale' not in st.session_state:
    st.session_state.button_clicked_CodFiscale = False
if 'button_clicked_Persona' not in st.session_state:
    st.session_state.button_clicked_Persona = False
if 'button_clicked_Apparizione' not in st.session_state:
    st.session_state.button_clicked_Apparizione = False

if st.button('Verifica del codice fiscale', key='button1'):

    # Verify code format
    if CodiceFiscale != "" and len(CodiceFiscale) != 7:
        st.warning("Il codice fiscale deve essere lungo 7 caratteri.")
        st.session_state.button_clicked_CodFiscale = False
    elif CodiceFiscale != "" and not CodiceFiscale.isalnum():
        st.warning("Il codice fiscale deve essere alfanumerico.")
        st.session_state.button_clicked_CodFiscale = False
    elif CodiceFiscale == "":
        st.warning("Il codice fiscale non deve essere vuoto.")
        st.session_state.button_clicked_CodFiscale = False
    else:
        st.success("Il codice fiscale è Valido.")  
        st.session_state.button_clicked_CodFiscale = True

if st.session_state.button_clicked_CodFiscale:
    
    # If the person is new, all fields must be entered (insertion of a record in the table PERSON)
    if df_CodFiscale.empty:

        st.header("Codice Fiscale non presente nel Database, inserisci i dati della persona.")
        
        Nome = st.text_input("Nome")
        Cognome = st.text_input("Cognome")
        Nazione = st.text_input("Nazione")
        Età = st.text_input("Età")
        
        try:
        # A specific error message must be generated in case of missing data (empty fields) 
        # or not typed correctly (incorrect data format).
            if not Nome or not Cognome or not Nazione or not Età:
                raise ValueError("All fields must be filled in.")
            
            # Add more checks here if needed, for example to check the format of the data
            if st.button('Verifica della persona inserita.', key='button2'):
                st.session_state.button_clicked_Persona = True

                # Format verification of First Name, Surname and Country
                if not Nome.isalpha() and not len(Nome) < 100: 
                    st.warning("Il nome deve essere composto da sole lettere.")
                    st.session_state.button_clicked_Persona = False
                elif not Cognome.isalpha() and not len(Cognome) < 100:
                    st.warning("Il cognome deve essere composto da sole lettere.")
                    st.session_state.button_clicked_Persona = False
                elif not Nazione.isalpha() and not len(Nazione) < 100:
                    st.warning("La nazione deve essere composta da sole lettere.")
                    st.session_state.button_clicked_CodFiscale = False
                elif not Età.isdigit():
                    st.warning("L'età deve essere un numero.")
                    st.session_state.button_clicked_CodFiscale = False
                else:
                    query_insert_persona = f'''INSERT INTO PERSONA (CodiceFiscale, Nome, Cognome, Nazione, Età) VALUES ('{CodiceFiscale}', '{Nome}', '{Cognome}', '{Nazione}', {Età})'''
                    result_insert_persona = execute_query(st.session_state['connection'],query_insert_persona)
                    st.success("Persona inserita correttamente.")

        except Exception as e:
            st.warning(e)

    # If the person is an existing person, it is sufficient to enter his or her tax code.
    if st.session_state.button_clicked_Persona or not df_CodFiscale.empty:        
        st.header("Inserisci i dati dell'apparizione.")

        query_InfoPodcast = '''SELECT CodPodcast FROM INFO_PODCAST'''
        result_InfoPodcast = execute_query(st.session_state['connection'],query_InfoPodcast)
        df_InfoPodcast = pd.DataFrame(result_InfoPodcast)
        CodPodcast = st.selectbox("Codice Fiscale", [row[0] for row in df_InfoPodcast.values])
        NumeroPuntata = st.text_input("Numero Puntata")
        DataUscita = st.date_input("Data Uscita")
        try:
            if not CodPodcast or not NumeroPuntata or not DataUscita:
                raise ValueError("All fields must be filled in.")
                
            # Check the format of the data
            if st.button("Verifica dell'apparizione inserita.", key='button3'):
                st.session_state.button_clicked_Apparizione = True

                # Checking the format of the IssueNumber
                if not NumeroPuntata.isdigit():
                    st.warning("Il numero della puntata deve essere un numero.")
                else:
                    query_insert_apparizione = f'''INSERT INTO APPARIZIONE (CodiceFiscalePartecipante, CodPodcast, NumeroPuntata, DataUscita) VALUES ('{CodiceFiscale}', '{CodPodcast}', {NumeroPuntata}, '{DataUscita}')'''
                    result_insert_apparizione = execute_query(st.session_state['connection'],query_insert_apparizione)

                    # the form must display a message of correct entry
                    # with a message informing about the total number of participations of the person, otherwise it must
                    # notify the error with the reason for the failed entry ''

                    query_countApprizioni = f'''SELECT COUNT(*) FROM APPARIZIONE WHERE CodiceFiscalePartecipante = '{CodiceFiscale}' '''
                    result_counApparizioni = execute_query(st.session_state['connection'],query_countApprizioni)
                    df_countApparizioni = pd.DataFrame(result_counApparizioni)
                    st.success(f'''Apparizione inserita correttamente.
                                   Numero totale di partecipazioni della persona: {df_countApparizioni.values[0][0]}''')
        except Exception as e:
            st.warning(e)