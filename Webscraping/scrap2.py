#Nombre: Israel Cuéllar Méndez.
#Matricula: 2077688.
#Importar módulos
import requests
from bs4 import BeautifulSoup
#Obtener la información HTML de la URL
URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)
#Analizamos el contanido HTML con BeautifulSoup
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")
#Formateamos la salida del objeto results de BeautifilSoup
print(results.prettify())
