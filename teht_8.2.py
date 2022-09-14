import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='cool',
         autocommit=True
         )

def nimi():
    print("1 - syötä uusi")
    print("0 - lopetus")
    valinta = -1
    while valinta < 0 or valinta > 2:
        valinta = int(input("Valitse: "))
    return valinta


def lisääUusi(nimi):
    etunimi = input("Uusi nimi : ")
    nimi[etunimi] = nimi