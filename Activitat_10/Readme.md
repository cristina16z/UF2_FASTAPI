
# Inserció de dades a la Base de Dades (csv a DB)

1. Llegim el fitxer csv on estan totes les paraules amb la seva temàtica a través de la llibreria de pandas

2. Ho convertim en una llista

3. Generem un bucle (que ho realitzi tantes vegades com paraules hi han en el csv, en aquest cas 500) per a que importi la funció csv_to_db del fitxer insertData_csv_to_db on li pasem com a paràmetre d'entrada la 'i' del bucle for i la llista del fitxer csv.

4. Aquest mètode que es cridat, el que fa es trucar al fitxer de conexió per conectar-se a la base de dades, i després realitzar, executar una query què és un insert per inserir la paraula i la seva temàtica a la taula de la bdd (agafant com a referència les columnes de word i theme del csv, sigui corresponent a les de paraules i temàtica) i per últim tanca la conexió a la bdd. De forma que això ho ha amb les 500 paraules que hi han.

Com en l'arxiu de conexió té un print de verificació com que la conexió s'ha establert correctament, en la terminal surt les 500 vegades que ha realitzat tot el procés per a cada una de les paraules.

<img src="./readme_imgs/insercio_dades1.JPG"/>

<br>

Aquí podem observar com en la taula de la base de dades s'han inserit totes les paraules.

<img src="./readme_imgs/insercio_dades2.JPG"/>