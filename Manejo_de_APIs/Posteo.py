import requests
import json

#
#Nombre: Israel Cuéllar Méndez.
#Matricula: 2077688.

if __name__ == '__main__':
    url = "https://httpbin.org/post"
    argumentos = {'nombre':'Israel','matricula':'2077688','curso':'Programacion para Ciberseguridad'}

    response = requests.post(url, params=argumentos)

    if response.status_code == 200:
        print(response.content)