from csv import writer, reader
import os

class CsvKaantaja:
    def __init__(self):
        pass

    def kirjoita_tiedostoon(self,array,file):
        with open(os.path.join(os.path.dirname(__file__),file), 'a') as tiedosto:
            kirjoitettava = writer(tiedosto)
            kirjoitettava.writerow(array)
            tiedosto.close()

    def lue_tiedostosta(self,file):
        pistejoukot = []
        with open(os.path.join(os.path.dirname(__file__),file), 'r') as tiedosto:
            luettava = reader(tiedosto)
            for rivi in luettava:
                rivilist = []
                if file == "ruudut.csv":
                    ruutu = []
                    for ruudukko_rivi in rivi:
                        ret_rivi = []
                        for entry in ruudukko_rivi[1:-1].split(", "):
                            if(entry == "True"):
                                ret_rivi.append(True)
                            else:
                                ret_rivi.append(False)
                        ruutu.append(ret_rivi)
                    pistejoukot.append(ruutu)
                elif len(rivi[1:-1]) > 1:
                    for entry in rivi:
                        pari = []
                        for numero in entry[1:-1].split(", "):
                            pari.append(int(numero))
                        rivilist.append(pari)
                    pistejoukot.append(rivilist)
                else:
                    rivilist.append(int(rivi[0]))
                    pistejoukot.append(rivilist) 
        #print (pistejoukot)
        return pistejoukot

