/*
  Name: MySQL Sample Database DB_Quaderno3
  Create the database for registering podcast guests. Consider the logical schema shown
    below. Consider the logical schema below:

    PERSONA(CodiceFiscale, Nome, Cognome, Nazione, Età)
    PODCAST(CodPodcast, CodFiscalePresentatore)
    INFO_PODCAST(CodPodcast,Titolo, Servizio, Finito*)
    APPARIZIONE(CodiceFiscalePartecipante, CodPodcast, NumeroPuntata, DataUscita)

    Note: the underlined fields identify the primary key of each relation, while the asterisk identifies an
    optional field. CodPodcast is a 10-character alphanumeric string. CodPodcast is a numeric code,
    which must start from 1.

    Note for Part I: When creating and querying the database, to ensure
    validity of the delivered work, it is mandatory to follow the nomenclature used in the text for the names
    of relations and attributes (including the use of upper and lower case).

    The following activities are required:
    - Create a MySQL script with:
        1. The instructions for creating the database corresponding to the indicated logical schema and specifying
        of the appropriate constraints;
        2. The instructions for populating the database created in the previous step (at least 5 records for the
        people table, 2 podcast records and at least 2 appearances)

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
