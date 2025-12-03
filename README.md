# Proyecto Librería

Esta libreria permite extraer los inventarios de ECS AWS, con python y boto3

## Características

- Conexion ECS AWS con Boto 3 
- Lista de clusters 
- Lista de servicios por cluster 
- Task definitions 


## Estructura del proyecto

```sh
.env
.gitignore
Dockerfile
README.md
requirements.txt
setup.py
src/
    library/
        conn_ECS.py
        get_scaling_conf_by_task.py
        get_task_definitions_by_service.py
        lsit_clusters.py
        save_info_CSV.py

lambda_handler.py
.env
.gitignore
.Dockerfile
requeriments.txt
```


## EJECUCION 

Ejecutar el proyecto desde la carpeta `src`:
```sh
cd src
python test\test.py\test_connection.py
```

## Docker
```sh
docker build -t libreria-app .
docker run -p 8000:8000 libreria-app
```

