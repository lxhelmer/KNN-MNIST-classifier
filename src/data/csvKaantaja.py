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
            for entry in rivi:
                rivilist.append(entry[1:-1].split())
            pistejoukot.append(rivilist)

    return pistejoukot

