# Ohjelman käyttö

Toimiakseen mnist tiedostot tulee ladata ja sijoittaa alemman kuvan mukaisesti projektikansion ulkopuolelle omiin kansioihinsa alla olevan mallin mukaan.
Tiedostot tulee myös purkaa .gz muodosta.

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

Asenna ohjelman vaatimat riippuvuudet poetryllä

```shell poetry install```

Ohjelman käyttämistä helpottaa poetryn virtuaaliympäristön käyttö. Sen voi ottaa käyttöön komennolla:

```shell poetry shell```

Ohjelman voi käynnistää komennolla:

```shell poetry run invoke start ```

Ohjelman testit voi ajaa komennolla:

```shell poetry run invoke start ```

Ohjelman koodin laadun voi tarkastaa komennolla:

```shell poetry run invoke lint ```

Ohjelman testikattavuuden voi tarkistaa komennolla:

```shell poetry run invoke coverage-report ```

Kun ohjelmaa käytetään poetry virtuaaliympäristössä "poetry run" osa ei ole välttämätön. 

Ohjelma valitsee 10 satunnaista kuvaa testi sarjasta joiden esittämän numeron se luokittelee. 

Ohjelma tulostaa jokaiselle kuvalle listan

(a<sub>1</sub>,a<sub>2</sub>,a<sub>3</sub>,a<sub>4</sub>,a<sub>5</sub>,a<sub>6</sub>,a<sub>7</sub>,a<sub>8</sub>,a<sub>9</sub>,a<sub>10</sub>)

missä a<sub>n</sub> kertoo n numeroa esittävien kuvien määrän k lähiten testikuvaa vastaavan kuvan joukossa. Tästä näkee kuinka varma arvio oli. 
Lisäksi tulostetaan arvioiden yhteen laskettu tarkkuus siihen asti.
