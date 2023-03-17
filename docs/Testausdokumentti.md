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
