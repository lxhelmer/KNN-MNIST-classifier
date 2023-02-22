from csvKaantaja import CsvKaantaja
class CsvGeneraattori:
    
    def __init__():
        self._kirjoita_tiedostoon = CsvKaantaja.kirjoita_tiedostoon

    def luo_harjoituscsvt():
        for i in range(0, 60000):
            kuvat = lataa_kuvat(harjoitus_polku)
            nimikkeet = lataa_nimikkeet(harjoitus_polku)
            showinconsole(kuvat[0,:,:])
            print(i)
            self.kirjoita_tiedostoon(pistejoukko(kuvat[i,:,:]),"kordinaatit.csv")
            self.kirjoita_tiedostoon(ruudut(kuvat[i,:,:]), "ruudut.csv")
            self.kirjoita_tiedostoon([nimikkeet[i]],"nimikkeet.csv")



