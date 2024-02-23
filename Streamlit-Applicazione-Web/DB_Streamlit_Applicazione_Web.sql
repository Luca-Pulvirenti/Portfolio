/*
  Name: MySQL Sample Database DB_Quaderno3
  Realizzare la base di dati per la registrazione degli ospiti di podcast. Considerare lo schema logico riportato di
    seguito. Considerare lo schema logico riportato di seguito:

    PERSONA(CodiceFiscale, Nome, Cognome, Nazione, Età)
    PODCAST(CodPodcast, CodFiscalePresentatore)
    INFO_PODCAST(CodPodcast,Titolo, Servizio, Finito*)
    APPARIZIONE(CodiceFiscalePartecipante, CodPodcast, NumeroPuntata, DataUscita)

    Nota: i campi sottolineati identificano la chiave primaria di ciascuna relazione, mentre l’asterisco identifica un
    campo opzionale. CodPodcast è una stringa alfanumerica di 10 caratteri. NumeroPuntata è un codice numerico,
    che parte obbligatoriamente da 1.

    Nota per lo svolgimento della parte I: Nella creazione e nell’interrogazione della base di dati, per garantire
    la validità dell’elaborato consegnato, è obbligatorio attenersi alla nomenclatura usata nel testo per i nomi
    delle relazioni e degli attributi (incluso l’uso di maiuscole e minuscole).

    Sono richieste le seguenti attività:
    • Creare uno script MySQL con:
        1. Le istruzioni per la creazione della base di dati corrispondente allo schema logico indicato e la specifica
        degli opportuni vincoli;
        2. Le istruzioni per il popolamento della base di dati creata al punto precedente (almeno 5 record per la
        tabella delle persone, 2 record di podcast ed almeno 2 apparizioni)

  Link: http://www.mysqltutorial.org/mysql-sample-database.aspx
*/


/* Create the database */
CREATE DATABASE IF NOT EXISTS DB_Quaderno3;

/* Switch to the classicmodels database */
USE DB_Quaderno3;

/* Create the tables */
CREATE TABLE PERSONA (
  CodiceFiscale varchar(16) NOT NULL,
  Nome varchar(100) NOT NULL,
  Cognome varchar(100) NOT NULL,
  Nazione varchar(100) NOT NULL,
  Età integer NOT NULL,
  PRIMARY KEY (CodiceFiscale)
);

CREATE TABLE PODCAST (
  CodPodcast varchar(10),
  CodFiscalePresentatore varchar(16),
  PRIMARY KEY (CodFiscalePresentatore, CodPodcast)
);

CREATE TABLE INFO_PODCAST (
  CodPodcast varchar(10) NOT NULL,
  Titolo varchar(100) NOT NULL,
  Servizio varchar(100) NOT NULL,
  Finito boolean,
  PRIMARY KEY (CodPodcast)
);

CREATE TABLE APPARIZIONE (
    CodiceFiscalePartecipante varchar(16),
    CodPodcast varchar(10),
    NumeroPuntata int NOT NULL,
    DataUscita date NOT NULL,
    PRIMARY KEY (CodiceFiscalePartecipante,CodPodcast),
    FOREIGN KEY (CodPodcast) REFERENCES INFO_PODCAST(CodPodcast),
    FOREIGN KEY (CodiceFiscalePartecipante) REFERENCES PERSONA(CodiceFiscale)
);

/* Inserting data  */
/* Inserimento di dati nella tabella PERSONA */
INSERT INTO PERSONA (CodiceFiscale, Nome, Cognome, Nazione, Età) VALUES ('CF00001', 'Alessia', 'Rossi', 'Italia', 30);
INSERT INTO PERSONA (CodiceFiscale, Nome, Cognome, Nazione, Età) VALUES ('CF00002', 'Luca', 'Bianchi', 'Italia', 35);
INSERT INTO PERSONA (CodiceFiscale, Nome, Cognome, Nazione, Età) VALUES ('CF00003', 'Giorgia', 'Verdi', 'Italia', 28);
INSERT INTO PERSONA (CodiceFiscale, Nome, Cognome, Nazione, Età) VALUES ('CF00004', 'Marco', 'Neri', 'Italia', 33);
INSERT INTO PERSONA (CodiceFiscale, Nome, Cognome, Nazione, Età) VALUES ('CF00005', 'Elena', 'Gialli', 'Italia', 40);

/* Inserimento di dati nella tabella PODCAST */
INSERT INTO PODCAST (CodPodcast, CodFiscalePresentatore) VALUES ('PC001', 'CF00001');
INSERT INTO PODCAST (CodPodcast, CodFiscalePresentatore) VALUES ('PC002', 'CF00002');
INSERT INTO PODCAST (CodPodcast, CodFiscalePresentatore) VALUES ('PC003', 'CF00003');
INSERT INTO PODCAST (CodPodcast, CodFiscalePresentatore) VALUES ('PC004', 'CF00004');
INSERT INTO PODCAST (CodPodcast, CodFiscalePresentatore) VALUES ('PC005', 'CF00005');

/* Inserimento di dati nella tabella INFO_PODCAST */
INSERT INTO INFO_PODCAST (CodPodcast, Titolo, Servizio, Finito) VALUES ('PC001', 'Conversazioni sui BTC', 'Spotify', 0);
INSERT INTO INFO_PODCAST (CodPodcast, Titolo, Servizio, Finito) VALUES ('PC002', 'Storie di Scienza', 'Apple Podcasts', 1);
INSERT INTO INFO_PODCAST (CodPodcast, Titolo, Servizio, Finito) VALUES ('PC003', 'Dialoghi sulla Musica', 'Google Podcasts', 0);
INSERT INTO INFO_PODCAST (CodPodcast, Titolo, Servizio, Finito) VALUES ('PC004', 'Racconti di Viaggio', 'Amazon Music', 0);
INSERT INTO INFO_PODCAST (CodPodcast, Titolo, Servizio, Finito) VALUES ('PC005', 'Tecnologia e Innovazione', 'YouTube', 1);


/* Inserimento di dati nella tabella APPARIZIONE */
INSERT INTO APPARIZIONE (CodiceFiscalePartecipante, CodPodcast, NumeroPuntata, DataUscita) VALUES ('CF00001', 'PC001', 3, '2023-01-29');
INSERT INTO APPARIZIONE (CodiceFiscalePartecipante, CodPodcast, NumeroPuntata, DataUscita) VALUES ('CF00002', 'PC002', 3, '2023-02-19');
INSERT INTO APPARIZIONE (CodiceFiscalePartecipante, CodPodcast, NumeroPuntata, DataUscita) VALUES ('CF00003', 'PC003', 1, '2023-03-01');
INSERT INTO APPARIZIONE (CodiceFiscalePartecipante, CodPodcast, NumeroPuntata, DataUscita) VALUES ('CF00001', 'PC003', 2, '2023-03-08');
INSERT INTO APPARIZIONE (CodiceFiscalePartecipante, CodPodcast, NumeroPuntata, DataUscita) VALUES ('CF00002', 'PC004', 1, '2023-03-15');
INSERT INTO APPARIZIONE (CodiceFiscalePartecipante, CodPodcast, NumeroPuntata, DataUscita) VALUES ('CF00004', 'PC004', 2, '2023-03-22');
INSERT INTO APPARIZIONE (CodiceFiscalePartecipante, CodPodcast, NumeroPuntata, DataUscita) VALUES ('CF00005', 'PC005', 1, '2023-04-01');
INSERT INTO APPARIZIONE (CodiceFiscalePartecipante, CodPodcast, NumeroPuntata, DataUscita) VALUES ('CF00003', 'PC005', 2, '2023-04-08');