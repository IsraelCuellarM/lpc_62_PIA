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
#Buscar todos los elementos que el class "card-content"
job_elements = results.find_all("div", class_="card-content")
#Por cada elemento encontrado job_elements imprimidos
for job_element in job_elements:
    print(job_element, end="\n"*2)
    