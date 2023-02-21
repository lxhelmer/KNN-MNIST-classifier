Viikolla saatiin paljon aikaan. Ohjelma käy nyt huomattavasti nopeammin kun turhaa laskentaa on vähennetty. Ohjelman nopeus on tällähetkellä
n.13-20 sekunttia kun harjoitus kuvien määrä on 6000. Olen arvioinut optimoinnin yhteydessä tuolla 6000 määrällä koska koin sen vastaavan tarpeeksi
läheisesti kymmenesosaa. Algoritmi arvioi nyt kovakoodatusti 13, ruutua nousevassa järjestyksessä etäisyyden mukaan siten että vältytään turhalta pisteiden
läpikäynniltä jos pieni etäisyys löytyy. Aijon vielä kasvattaa tämän kovakoodattujen etäisyyksien määrän 25 lähimpään ruutuun. Uskon että tämä laskee
etäisyyksien laskemisen tarpeen hyvin vähäiseksi. Tässä vaiheessa optimointia testaus on tehtävä seuraavaksi kuntoon jotta huomaan mahdolliset virheet 
optimoinnissa. Nyt jo optimoidessa olen huomannut tilapäisesti virheiden aiheuttaneen vääriä etäisyyden arviointeja. Kun optimointia saadaan pidemmälle
tulee hyvän testauksen jälkeen saada koodin luettavuus ja sisäinen laatu korkeammalle tasolle. Epäloogisuus muuttujanimissä sekä funktioiden keskenäiset
epäloogisuudet ovat aiheuttaneet jo päänvaivaa.

Aikaa käytetty viikolla n. 18h
