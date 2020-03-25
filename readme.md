# Proyecto Ingeniería de Software II - "Open Data"
## Plataforma de Monitores de Emprendimientos para OpenBeauchef

Este repositorio contiene el proyecto de Ingeniería de Software II (CC-5401) de la FCFM. 

## El proyecto esta estructurado de la siguiente manera:

 ```  
|-- monitor-de-emprendimientos-para-openbeauchef
|   |-- opendata
|   |   |-- settings.py
|   |   |-- urls.py
|   |   `-- wsgi.py
|   |-- emprendimientos
|   |   |-- admin.py
|   |   |-- apps.py
|   |   |-- models.py
|   |   |-- templates
|   |   |-- tests.py
|   |   |-- urls.py
|   |   `-- views.py
|   |-- ficha
|   |   |-- admin.py
|   |   |-- apps.py
|   |   |-- models.py
|   |   |-- templates
|   |   |-- tests.py
|   |   |-- urls.py
|   |   `-- views.py
|   |-- personas
|   |   |-- admin.py
|   |   |-- apps.py
|   |   |-- models.py
|   |   |-- templates
|   |   |-- tests.py
|   |   |-- urls.py
|   |   `-- views.py
|   |-- manage.py
|	|-- static
|   |-- templates
|-- README.md
|-- requirements.txt
 ```

El proyecto principal se encuentra en la carpeta monitor-de-emprendimientos-para-openbeauchef, que contiene las configuraciones globales del proyecto en ```settings.py```, las urls por defecto que mappeara django desde los request estarán en el archivo ```urls.py```.

Ademas se generan app's (emprendimientos, ficha, personas, etc.) en sus carpetas respectivas. Cada una de estas tendrá consigo:
* templates : Carpeta que contiene los archivos html correspondientes a las vistas de la app.
* urls.py : Archivo que contiene las rutas y conexiones con las funciones respuestas.
* views.py : Archivo que contiene la lógica de respuestas a las peticiones.
* models.py : Archivo que contiene las clases que representan los objetos que el ORM de django mappeara y guardara en la base de datos.

Los estáticos del projecto estarán en la carpeta ```static```

## Requisitos del proyecto
Para la correcta ejecución de este proyecto se requiere python 3 y pip. 

## Instalación del proyecto

Para instalar y hacer correr esta plataforma se recomienda el uso de un ambiente virtual, herramientas como [virtualenv](https://virtualenv.pypa.io/en/stable/) o su [wrapper](https://virtualenvwrapper.readthedocs.io/en/latest/) son altamente recomendadas, primero se deben instalar las dependencias del proyecto señaladas en el archivo ```requirements.txt```, para esto se puede utilizar el comando 
``` pip install -r path/to/requirements.txt ```
 ya con esto solo debemos crear la base de datos, lo cual se puede hacer mediante los comandos
 ``` 
 django /path/to/manage.py makemigrations
 django /path/to/manage.py migrate
 ```
