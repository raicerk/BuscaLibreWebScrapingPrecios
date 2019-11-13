# BuscaLibreWebScrapingPrecios


```shell
docker run --network=mentores-ti-api_default -p:5000:5000  -v /home/raicerk/DesarrollosBuscaLibreWebScrapingPrecios:/script --rm python sh -c "pip install -r /script/requirements.txt && python /script/app.py"
```

## Entorno de desarrollo y dependencias

Para activar el Virtual Enviroment

```shell
python3 -m venv venv && . ./venv/bin/activate
```

Para instalar las dependencias de la aplicación
```shell
python3 -m pip install -r requirements.txt