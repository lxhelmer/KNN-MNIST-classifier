![image](https://user-images.githubusercontent.com/49132322/225994650-198ec2b2-1d15-4143-a752-c8d537060c60.png)


Ohjelmisto sisältää normaalit yksikkötestit jotka pitävät huolta että koodi toimii oikein eikä siihen ainakaan lisätä optimoidessa uusia virheitä. 
Yksikkötestien testiarvot on laskettu osittain koneellisesti ja osittain käsin. Koneellisesti lasketut arvot on tarkistettu käsin hyvällä tasolla.

Otin tutkittavaksi pariksi MNIST testikuvien joukosta kuvan numero 20 ja harjoituskuvien joukosta kuvan numero 19. Valinta oli käytännössä
sattumanvarainen. Laskin kyseisten kuvien välisen muokatun hausdorff etäisyyden "A Modifed Hausdorff Distance for Object Matching" julkaisun mukaan käsin.
Käytin tätä vertailuna sille toimiko m_hausdorff_etaisyys funktio oikein. Tein myös näihin kuviin perustuvia testejä jotka tarkistivat toimiko eri
esitysmuotojen generoiminen oikein. Tätä varten tarkistin näille tapauksille generoidut esitykset käsin.

Lisäksi toteutin testausta joka tutkii koko algoritmin toimintaa kun luokitellaan testijoukon tunnettua kuvaa numero 20. Tämä testaaminen on varsin hidasta
sillä koko algoritmi suoritetaan kerran. Tällä kuitenkin saadaan testattua antaako algoritmi oikean luokitelman arvolle joka on ennen optimointia
luokiteltu oikein sekä onko luokittelun "varmuus" muuttunut. Testien suorittaminen vie noin minuutin.
