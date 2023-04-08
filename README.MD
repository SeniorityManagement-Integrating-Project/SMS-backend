# SMS-backend 

Proyecto creado con `Python 3.10.10`

## Instalación de dependencias

`pip install -r requirements.txt`

**Nota:** Cuando se instale una nueva dependencia se tiene que ejecutar el comando: `pip freeze > requirements.txt`
para agregarla al archivo de requerimientos.

**Nota 2:** Es importante aislar el entorno virtual de los paquetes del espacio del usuario global del sistema, para no
estar inyectándole dependencias innecesarias al proyecto.

## Ejecutando el proyecto

Estando en la raíz del proyecto ejecutamos: `uvicorn src.main:app --reload`