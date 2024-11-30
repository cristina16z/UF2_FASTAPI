
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

<br>

# [Endpoints] /penjat/tematica/opcions

Amb aquest endpoint, fem que retorni totes les temàtiques sense repetits, úniques, que estan emmagatzemades a la base de dades. El funcionament és el següent:

1. S'executa una consulta SQL per extreure les temàtiques

2. Aquest resultat, es processada per una funció que ho converteix en un diccionari amb el format {"tematica": "nom_de_la_temàtica"}

3. Després a través d'una funció, recull tots aquest resultats per retornar un diccionari, iterant sobre elles

4. A través del endpoint retorna un JSON amb totes les temàtiques úniques que hi han.


<img src="./readme_imgs/read_AllTematicas.JPG"/>



<br>

# [Endpoints] /penjat/tematica/{option}

Amb aquest endpoint, fem que a partir de la temàtica que li introduïm, passem, ens mostri una paraula a l'atzar d'aquella mateixa temàtica sobre totes les que hi han (en aquest cas, hi han 100 paraules per temàtica) en la base de dades

1. S'executa una consulta SQL per extreure totes les paraules que coincideixin amb la temàtica insertada

2. Aquest resultat, es processada per una funció que ho converteix en un diccionari amb el format {"paraula": "paraula_de_la_temàtica"}

3. Després a través d'una funció, recull tots aquest resultats per retornar un diccionari, iterant sobre elles

4. A través del endpoint indiquem que retorni un JSON amb nomès una única paraula a l'atzar

<img src="./readme_imgs/read_1word.JPG"/>
