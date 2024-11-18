## SWAGGER - Body-Fields

Incorrecto porque superar el máximo número de carácteres que es 10 en la descricpción del item, y cómo consecuencia salta ése mensaje.

<img src="./Readme_imgs/bodyFields2_ErrorCaracteres_Postman.JPG"/>

<br>

Incorrecto por poner un número igual o inferior a 0 en el precio del item, ya que en el código tiene gt = 0, que significa gratter than = 0, es decir, que tiene que ser mayor a 0.

<img src="./Readme_imgs/bodyFields3_ErrorPrice_Postman.JPG"/>

<br>

Cuando introducimos los datos correctamente sin incumplir ninguna restricción, salta el código 200 conforme ha sido un éxito la petición.

<img src="./Readme_imgs/bodyFields1_200_Postman.JPG"/>

## POSTMAN - Body-Nested Models