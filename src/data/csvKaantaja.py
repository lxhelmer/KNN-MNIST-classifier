from csv import writer, reader
import os

def kirjoita_tiedostoon(array,file):
    with open(os.path.join("data/",file), 'a') as tiedosto:
        kirjoitettava = writer(tiedosto)
        kirjoitettava.writerow(array)
        tiedosto.close()

def lue_tiedostosta(file):
    pistejoukot = []
    with open(os.path.join("data/",file), 'r') as tiedosto:
        luettava = reader(tiedosto)
        for rivi in luettava:
            rivilist = []
            if len(rivi[1:-1]) > 1:
                for entry in rivi:
                    pari = []
                    for numero in entry[1:-1].split(", "):
                        pari.append(int(numero))
                    rivilist.append(pari)
            else:
                rivilist.append(int(rivi[0]))
            pistejoukot.append(rivilist)

    return pistejoukot

