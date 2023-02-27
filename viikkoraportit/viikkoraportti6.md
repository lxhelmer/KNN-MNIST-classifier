Projekti alkaa lähestymään valmista muotoaan vaikka työtä vielä on. 

Viikolla lisäsin testausta. Laskin käsin testitapauksen jossa vertasin kahta kuvaa ja loin tämän arvon perusteelta yksikkötestin. Laskiessani arvoa sain
14 desimaalin tarkkuuden jota pidän riittävän hyvänä antamaan kuva siitä onko laskelmissa vikaa. Käsin laskiessa jo yhden etäisyyden väärä arvio muutti
vastaavasti tulosta sadasosien tasolla.

Optimointi sujuu hyvin. Kirjoitin koodiin lähimmät 25 ruutua jotka käydään nousevassa järjestyksessä läpi. Lisäksi jos seuraavan etäisyyden päässä oleva
ruutu löytyy myöhemmin käydessä etäisyyksiä läpi tiedetään sen olevan minimi ja näin saadaan yksi kovakoodattu etäisyys lisää ikään kuin ilmaiseksi.
Mahdollisesti lisään vielä yhden tai kaksi etäisyyttä pidemmälle tutkimista sillä uskon siitä olevan vielä merkittävää hyötyä. Mietin myös mahdollisuuksia
luokitella etäisyyksiä pidemmälle ja iteroida kaikkien arvojen läpi etäisyyden mukaan jos keksin tähän jonkin helpon kaavan. Tämä poistaisi myös 25 lähimmän
ruudun uudelleen iteroimisen. Nykyisellään ohjelma arvioi 6000 etäisyyttä 9-11 sekunnissa. Olisi kiva saada tätä lukua vielä hieman alemmas 5-8 sekunnin
tasolle. 

Kirjoitin myös pari muuta testiä jotka lähinnä keskittyvät siihen että suorituksen aikana käytettävät tietorakenteet ovat generoitu oikein. Tarkistin
näiden testien arvot käsin indeksi virheiden tms varalta koska koodi muuten on suhteellisen yksinkertainen.

Lisäksi refaktoroin ohjelman parempaan kuntoon sekä lisäsin merkittävästi kommentteja jotta ohjelmaa olisi helpompi ymmärtää. Toteutin suurimman osan
toiminnallisuudesta luokkina, lukuunottamatta paria toimintoa joiden koin yksinkertaisuudessaan olevan helpompi pitää pelkkinä importattavina funktioina.

Seuraavaksi optimoinnin vienti korkeammalle tasolle, dokumentoiti, merkittävä testaaminen. 

Tällä viikolla aikaa käytetty n. 20h
