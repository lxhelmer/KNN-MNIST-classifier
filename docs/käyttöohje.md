# Ohjelman käyttö

Toimiakseen mnist tiedostot tulee ladata ja sijoittaa alemman kuvan mukaisesti projektikansion ulkopuolelle omiin kansioihinsa alla olevan mallin mukaan.



```shell

tira
├── test
|   ├── t10k-images.idx3-ubyte
|   └── t10k-labels.idx1-ubyte
├── train
|   ├── nimikkeet.csv
|   ├── rajat.csv
|   ├── train-images.idx3-ubyte
|   └── train-labels.idx1-ubyte
└── tiralabra
    └── src
```

Ohjelma tarviksee toimiakseen tarvittavat .csv tiedostot. Ne voi generoida seuraavalla komennolla.

```shell poetry invoke gen ```

Ohjelman voi käynnistää komennolla 

```shell poetry invoke start ```

Ohjelma valitsee 10 satunnaista kuvaa testi sarjasta joiden esittämän numeron se luokittelee. 

Ohjelma tulostaa jokaiselle kuvalle listan

(a<sub>1</sub>,a<sub>2</sub>,a<sub>3</sub>,a<sub>4</sub>,a<sub>5</sub>,a<sub>6</sub>,a<sub>7</sub>,a<sub>8</sub>,a<sub>9</sub>,a<sub>10</sub>)

missä a<sub>n</sub> kertoo n numeroa esittävien kuvien määrän 11 lähiten testikuvaa vastaavan kuvan joukossa. Tästä näkee kuinka varma arvio oli. 
Lisäksi tulostetaan arvioiden yhteen laskettu tarkkuus. $$ oikeat arviot \over kaikki arviot $$
