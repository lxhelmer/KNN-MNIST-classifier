# TIRAPROJEKTI / Algorithms and data structures project course

MNIST luokittelu KNN metodia käyttäen.

### Esimerkkituloste

[img](https://github.com/lxhelmer/KNN-MNIST-classifier/blob/main/example.png)

# Ohjelman käyttö

Toimiakseen mnist tiedostot tulee ladata ja sijoittaa alemman kuvan mukaisesti projektikansion ulkopuolelle omiin kansioihinsa alla olevan mallin mukaan.
Tiedostot tulee myös purkaa .gz muodosta.

```shell

tira
├── test
|   ├── t10k-images.idx3-ubyte
|   └── t10k-labels.idx1-ubyte
├── train
|   ├── nimikkeet.csv
|   ├── rajat.csv
|   ├── train-images.idx3-ubyte
|   └── train-labels.idx1-ubyte
└── tiralabra
    └── src
```

Asenna ohjelman vaatimat riippuvuudet poetryllä

```shell 
poetry install
```

Ohjelman käyttämistä helpottaa poetryn virtuaaliympäristön käyttö. Sen voi ottaa käyttöön komennolla:

```shell 
poetry shell
```

Ohjelman voi käynnistää komennolla:

```shell 
poetry run invoke start
```

Ohjelman testit voi ajaa komennolla:

```shell
 poetry run invoke test
```

Ohjelman koodin laadun voi tarkastaa komennolla:

```shell
poetry run invoke lint
```

Ohjelman testikattavuuden voi tarkistaa komennolla:

```shell 
poetry run invoke coverage-report
```

Kun ohjelmaa käytetään poetry virtuaaliympäristössä "poetry run" osa ei ole välttämätön. 


Ohjelma tulostaa jokaiselle kuvalle listan

(a<sub>1</sub>,a<sub>2</sub>,a<sub>3</sub>,a<sub>4</sub>,a<sub>5</sub>,a<sub>6</sub>,a<sub>7</sub>,a<sub>8</sub>,a<sub>9</sub>,a<sub>10</sub>)

missä a<sub>n</sub> kertoo n numeroa esittävien kuvien määrän k lähiten testikuvaa vastaavan kuvan joukossa. Tästä näkee kuinka varma arvio oli. 
Lisäksi tulostetaan arvioiden yhteen laskettu tarkkuus siihen asti.

Lopuksi ohjelma tulostaa kootun listan kuvien esittämistä numeroista sekä algoritmin niille antamista luokitteluista


Ohjelma koostuu kahdesta pääluokasta ja näitä tukevista apufunktioista. Apufunktioina on toteutettu sellaiset ohjelman osat joiden käyttäminen
luokkainstansseina olisi ollut luettavuuden ja toimintalogiikan kannalta merkittävästi heikompi ratkaisu. Tällaisia ovat esimerkiski mnist datan muokkaamiseen käytetyt
funktiot.

# Rakenne

![image](https://user-images.githubusercontent.com/49132322/225993774-6a0ebc6d-2a50-4ae9-a9b7-e1989bf62206.png)


Ohjelman toimintaa on nopeutettu optimoimalla listakutsujen määrää. Koska mnist kuvat ovat keskitettyjä voidaan pienintä pisteen a ja pistejoukon B
välistä etäisyyttä lähteä etsimään pisteen a lähimmistä ruuduista. Tätä tehdään 44 pisteen a lähimmän ruudun verran. Tämä riittää melkein aina löytämään
lyhimmän etäisyyden. Etsintä tehdään siten että etäisyyden löytyessä tiedetään sen olevan pienin jolloin haku voidaan lopettaa. Vaihtoehtoratkaisuna kokeilin
etäisyyksiin perustuvaa binääripuu hakua mutta se oli hitaampi sillä yksittäisessä haussa on vain n. 100 arvoa, eikä binääripuu ole niin pienellä
solmu määrällä tehokkaampi. Koodi sisältää myös aiheesta riippumatonta optimointia. Etäisyyksien laskeminen on jaettu 6 prosessille jotta koodi voi hyödyntää
samanaikaista suoritusta. Tämä nopeutti koodin toimintaa n. 25-40%. Koska yksittäisen etäisyyden laskeminen ei ole riippuvainen muista etäisyyksistä voidaan
60 000 etäisyyden arvioiminen jakaa 10 000 etäisyyden lohkoihin. 6 prosessin tuottamat tulokset kerätään yhteiseen listaan minkä arvoja käytetään lopullisessa
arvioinnissa.

Ohjelman aikavaativuus on O(n) + O(k log n). Ensimmäinen O(n) on knn etäisyyksien laskemisen aikavaativuus ja toinen osa O(k log n) on k pienimpien
alkioiden valitsemisen aikavaativuus. Aikavaativuus on kuitenkin hämäävä sillä se sisältää erittäin suuria kertoimia joita ei oteta huomioon O-notaatiossa.
knn etäisyyksien laskemisessa jokaista tehtyä arviota kohti O(n) aikavaatimuksen koodia toistetaan 60 000 * 783 = 47 040 000 kertaa. Tämä tekee koodista todellisuudessa
varsin hidasta vaikka O-notaation kompleksisuus on matala. Erityisesti nopeuteen vaikuttaa se että koodi sisältää paljon listojen tutkimista mikä on pythonissa
luonnostaan hidasta.
Etäisyyksien järjestäminen on toteutettu kekojärjestämällä aikavaativuudella O(n) jonka jälkeen
k pienintä valitaan keosta ajassa O(k log n). Koodin tämä osa selkeästi nopeampi kuin etäisyyksien laskeminen sillä suoritettava koodi ei sisällä
oikeastaan ollenkaan ensimmäisen osan kaltaista "piilokerrannaisuutta".

Mahdollisesti parempi tapa kuvata aikavaativuutta on O(n*d) + O(k log n) missä d on harjoitusdatan laajuutta kuvaava muuttuja. d voisi olla esim.
vertailtavien objektien tai yksittäisten vertailtavien ominaisuuksien määrä. Nämä muuttujat ovat kuitenkin mnist datan kohdalla vakiot joten tällainen
merkintä olisi siinä mielessä virheellinen. 

Lähteenä projektille käytin [A Modified Hausdorff Distance for Object Matching](https://citeseerx.ist.psu.edu/doc/10.1.1.1.8155) paperia. Tosin kuvat paperista poiketen eivät olleet 'edge map' muodossa.

# Testaaminen

![image](https://user-images.githubusercontent.com/49132322/225994650-198ec2b2-1d15-4143-a752-c8d537060c60.png)


Ohjelmisto sisältää normaalit yksikkötestit, jotka pitävät huolta että koodi toimii oikein eikä siihen ainakaan lisätä optimoidessa uusia virheitä. 
Yksikkötestien testiarvot on laskettu osittain koneellisesti ja osittain käsin. Koneellisesti lasketut arvot on tarkistettu käsin hyvällä tasolla.
Testit tarkistavat eri matemaattisten funktioiden tuloksia ja muokatun hausdorff etäisyyden osatuloksia.

Otin tutkittavaksi pariksi MNIST testikuvien joukosta kuvan numero 20 ja harjoituskuvien joukosta kuvan numero 19. Valinta oli käytännössä
sattumanvarainen. Laskin kyseisten kuvien välisen muokatun hausdorff etäisyyden "A Modifed Hausdorff Distance for Object Matching" julkaisun mukaan käsin.
Käytin tätä vertailuna sille toimiko m_hausdorff_etaisyys funktio oikein. Tein myös näihin kuviin perustuvia testejä, jotka tarkistivat toimiko eri
esitysmuotojen generoiminen oikein. Tätä varten tarkistin näille tapauksille generoidut esitykset käsin.

Lisäksi toteutin testausta joka tutkii koko algoritmin toimintaa kun luokitellaan testijoukon tunnettua kuvaa numero 20. Tämä testaaminen on varsin hidasta
sillä koko algoritmi suoritetaan kerran. Tällä kuitenkin saadaan testattua antaako algoritmi oikean luokitelman arvolle joka on ennen optimointia
luokiteltu oikein sekä onko luokittelun "varmuus" muuttunut. Testien suorittaminen vie noin minuutin.A Mo di ed Hausdor Distance for Ob ject Matching


Tutkin eri optimointitekniikoiden merkitystä koodin nopeudelle. Vaihtoehtoina oli optimoinnille oli listakutsujen määrän minimoiminen sekä nopeiden python kirjastojen kuten numpy ja scipy käyttö. Lopputuloksena päädyin näiden yhdistelemiseen. 

Numpy listojen käyttäminen oli joillekkin operaatioille merkittävästi (10x-100x) nopeampaa kuin samojen operaatioiden toteuttaminen pythonin listoilla.
Tämä ei kuitenkaan pätenyt lista 'lookup' tapahtumiin perustuvaan listakutsujen minimointiin sillä tämä oli numpy listojen kohdalla merkittävästi
hitaampaa. Numpy listoille olisi toiminut hyvin scipyn etäisyys functio, mutta tällä oli kova minimi raja jota en pystynyt kiertämään. Päädyin käyttämään
Numpy listoja, jotka myöhemmin muutetaan normaaleiksi python listoiksi. Lopullinen arvioiden nopeus 60 000 harjoitus tapauksella oli n.35-60 sekunttia.
Ilman multiprosessointia n.60-90s. Eri luokiteltavien kuvien välillä oli merkittävästi eroa.


Algoritmin luokittelun kannalta merkittävää oli k arvo. Tutkin optimaalia k arvoa toteuttamalla pidempiä testausputkia, jolloin sain laskettua 50-150 
arvion perusteella algoritmin prosentuaalisen tarkkuuden. Paras saavuttamani tarkkuus oli n.97% k arvolla 11. Luokitteluja läpikäydessäni arvioin 
empiirisesti optimaalin n.6-7. Useissa rajatapauksissa 6 tai 7 kohdalla algoritmin äänestysvalinta teki vielä oikean valinnan, mutta suuremmilla k arvoilla
rajatapauksen väärä arvo vei voiton. Yleisiä rajatapauksia olivat 9-4 ja 9-6. Kuitenkin pisimmässä k=7 testissä saavutin vain tarkkuuden 95%. Tosin arvioituja numeroita oli vain 80 mikä teki muutamankin kuvan virheestä merkittävän. Olisin halunnut muodostaa kaavion virheestä suhteessa k arvoon, mutta kurssin puitteissa tähän ei ollut mahdollisuutta pitkien suoritusaikojen takia. 



[Määrittelydokumentti](https://github.com/lxhelmer/tiralabra/blob/main/docs/M%C3%A4%C3%A4rittelydokumentti.md)

[Käyttöohje](https://github.com/lxhelmer/tiralabra/blob/main/docs/K%C3%A4ytt%C3%B6ohje.md)

[Testausdokumentti](https://github.com/lxhelmer/tiralabra/blob/main/docs/Testausdokumentti.md)

[Toteutusdokumentti](https://github.com/lxhelmer/tiralabra/blob/main/docs/Toteutusdokumentti.md)



[viikkoraportti1](https://github.com/lxhelmer/tiralabra/blob/main/viikkoraportit/viikkoraportti1.md)

[viikkoraportti2](https://github.com/lxhelmer/tiralabra/blob/main/viikkoraportit/viikkoraportt2.md)

[viikkoraportti3](https://github.com/lxhelmer/tiralabra/blob/main/viikkoraportit/viikkoraportti3.md)

[viikkoraportti4](https://github.com/lxhelmer/tiralabra/blob/main/viikkoraportit/viikkoraportti4.md)

[viikkoraportti5](https://github.com/lxhelmer/tiralabra/blob/main/viikkoraportit/viikkoraportti5.md)

[viikkoraportti6](https://github.com/lxhelmer/tiralabra/blob/main/viikkoraportit/viikkoraportti6.md)


