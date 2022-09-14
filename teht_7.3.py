def valitse():
    print("1 - syötä uusi")
    print("2 - haku")
    print("3 - lopeta")

def lisääUusi(asemat):
    icao = input("Aseman ICAO-koodi : ")
    nimi = input("Aseman nimi : ")
    asemat[icao] = nimi

def hae(asemat):
    icao = input("Aseman ICAO-koodi : ")
    if icao in asemat:
        print(asemat[icao])
    else:
        print("Tuntematon ICAO-koodi")

lentoasemat = {}
valinta = valitse()
while valinta != 0:
    if valinta == 1:
        lisääUusi(lentoasemat)
    elif valinta ==2:
        hae(lentoasemat)
    valinta = valitse()