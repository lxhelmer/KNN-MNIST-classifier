Ohjelma koostuu kahdesta pääluokasta ja näitä tukevista apufunktioista. Apufunktioina on toteutettu sellaiset ohjelman osat joiden käyttäminen
luokkainstansseina olisi ollut luettavuuden kannalta merkittävästi heikompi ratkaisu. Tällaisia ovat esimerkiski mnist datan muokkaamiseen käytetyt
funktiot.

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

