import requests
# requests librería para hacer consultas a otros servidores web desde python
# fakeapi.platzi.com = servidor platzi de una api de tienda una tienda online


def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories') # acá definimos hacia a dónde vamos a hacer la solicitud
    print(r.status_code) # estatus code http
    print(r.text) # información que nos trae el api
    print(type(r.text)) # tipo de información/datos generalmente str
    categories = r.json() # para convertir la información a una lista/diccionario python y poder iterar
    for category in categories: # para imprimir una lista que contenga sólo los titulos
        print(category['name'])
