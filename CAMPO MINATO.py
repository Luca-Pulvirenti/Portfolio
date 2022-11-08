# CAMPO MINATO

# 1)Function: create a table with elements set to True(= there is a mine),
# or False(= there is no mine)
# - create a table with all values set to False
# - replace false with true randomly within the table

# 3) Create a dummy table to show the user

# 2) Create a function that prints the dummy table

# 4) Allow the user to choose to click any position in the table
# - take row and column as input

# 5) perform a check on the box to see if a mine is in that position or not
# - create an if in which to check if the chosen box is set to False or True
# - if it is true the player has lost
# - if it is false the player continues to play:
# - function: transform the element selected by the user into the number
# of mines that are in the boxes adjacent to the chosen position:
# - implement a loop where we parse from row (-1,3) to table (-1,3)
# with respect to the position of the main element
# - we will need to perform a check on the adjacent boxes to see if we are in the edges
# - also implement a counter that increments each time the parsed position equals True
# - replace the false element with the number of mines or replace it with 0

# 5) the player will win only when there are no boxes left set to False
# - run a check on the entire table to see if the player has won.


from random import randint

# Function: create a table with elements set to True(= there is a mine), or False(= there is no mine)


def crea_campo_minato(nr, nc, nm):
    campo = []
    for i in range(nr):
        # - create a table with all values set to False
        nuova_riga_vuota = [False] * nc
        campo.append(nuova_riga_vuota)

    # - replace false with true randomly within the table.
    for g in range(nm):
        campo[randint(0, nr-1)][randint(0, nc-1)] = True
    return campo


# 3) Create a dummy table to show to the user.
def crea_campo(nr, nc):
    campo2 = []
    for i in range(nr):
        nuova_riga_vuota = ["."] * nc
        campo2.append(nuova_riga_vuota)
    return campo2


# 2) Create a function that prints the dummy table
def printa_tabella(tabella):

    numero_colonne = len(tabella[0])
    numero_righe = len(tabella)

    for l in range(numero_righe):
        for j in range(numero_colonne):
            print(f"{tabella[l][j]:2}", end=" ")
        print()


# Functions to facilitate code checking
'''''
def printa_tabella_minata(tabella):

    numero_colonne= len(tabella[0])
    numero_righe = len(tabella)

    for l in range(numero_righe):
        for j in range(numero_colonne):
            print( tabella[l][j], end=" ")

        print()
'''''

'''''
def printa_tabella_mine(tabella):
    numero_colonne = len(tabella[0])
    numero_righe = len(tabella)

    for l in range(numero_righe):
        for j in range(numero_colonne):
            if tabella[l][j]:
                elemento= "X"
            else:
                elemento= "."
            print(elemento, end=" ")
        print()
'''''


# Function: transform the element selected by the user into the number of mines
# that are in the boxes adjacent to the chosen position
def conta_mine_adiacenti(posizione_riga, posizione_colonna, campo, campo_minato):
    contatore = 0
    for f in range(-1, 2):
        for h in range(-1, 2):
            if posizione_riga + f >= 0 and\
                posizione_riga + f < len(campo)\
                and posizione_colonna + h >= 0\
                    and posizione_colonna + h < len(campo):

                if f == 0 and h == 0:
                    pass
                elif campo_minato[posizione_riga + f][posizione_colonna + h]:
                    contatore = contatore + 1

    campo[posizione_riga][posizione_colonna] = contatore
    printa_tabella(campo)


def main():

    righe = 5
    colonne = 5
    mine = 3

    campo_minato = crea_campo_minato(righe, colonne, mine)
    campo = crea_campo(righe, colonne)
    # printa_tabella(campo_minato)
    printa_tabella(campo)
    ct = 0
    # Finche la tabella non rimane senza neanche un false ma solo con true(mine) il giocatore continua a giocare
    while ct < (righe*colonne)-mine:
        posizione_riga = int(input("Inserirsci la riga dell' punto che vuoi sciegliere"))
        posizione_colonna = int(input("Inserirsci la colonna dell' punto che vuoi sciegliere"))
        # 5) effettuare un controllo sulla casella per verifica se in quella posizione si trova una mina oppure no
        # - creare un if in cui controllare se la casella scelta è impostata in False o True
        if campo_minato[posizione_riga][posizione_colonna]:
            campo[posizione_riga][posizione_colonna] = "X"
            print("hai perso")
            exit()
        else:
            conta_mine_adiacenti(posizione_riga, posizione_colonna, campo, campo_minato)
            ct = 0
            for s in range(righe):
                for t in range(colonne):
                    if campo[s][t] != ".":
                        ct = ct + 1
    print("hai vinto")


main()