## Readme

### Crear Proyecto

1. Crear y activar un entorno virtual
2. Instalar los requirements.txt
3. Crear un proyecto y su core
4. Configurar settings 
5. Correr servidor


### Configuracion de Tokens 

1. Configurar REST_FRAMEWORK settings
2. Importar rest_framework_simplejwt
3. Agregar urls de api tokens
4. Realizar un migracion
5. Crear un superusuario

### Realizando pruebas

Testear en Postman 

        [POST] 
        http://localhost:8000/api/token/
        {
            "username": "aranibar",
            "password": "aranibar"
        }

Insetar el Refresh obtenido - Resultado: "Access" : "xxxxx"

        [POST] 
        http://127.0.0.1:8000/api/token/refresh/
        {
            "refresh": "XXXXXXXXXXXXXXXXXXXXXXX"
        }

