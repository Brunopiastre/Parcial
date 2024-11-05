# Parcial

Proyecto de Análisis de Secuencias de ADN Mutante

Este proyecto implementa una API REST diseñada para analizar secuencias de ADN y determinar si corresponden a mutantes. La API permite a los usuarios enviar secuencias para su evaluación y obtener estadísticas sobre el total de secuencias procesadas y los resultados de detección.
Requisitos

    Python 3.10 o superior
    Flask
    SQLAlchemy

Instrucciones para Ejecutar el Proyecto

Paso 1:
Instala las dependencias necesarias ejecutando el siguiente comando en tu terminal:
    pip install -r requirements.txt

Paso 2:
Inicia la aplicación ejecutando el archivo principal:
    python app.py

Paso 3:
Abre Postman y carga el archivo de colección ubicado en la carpeta collection.

Paso 4:
En Postman, selecciona la solicitud POST para enviar una secuencia de ADN y verificar si pertenece a un mutante. Ingresa la secuencia en formato JSON en el cuerpo de la solicitud y envíala.

Paso 5:
Para obtener estadísticas, selecciona la solicitud GET en Postman para ver el conteo de mutantes y no mutantes almacenados en la base de datos.


Postman se ejecutara en esta URL: http://127.0.0.1:5000/

Como esta dockreizado y hosteado con render solo hace falta abrir postman y poner las siguientes url:
Para realizar POST
https://parcial-x63a.onrender.com/mutant
Para realizar GET
https://parcial-x63a.onrender.com/stats