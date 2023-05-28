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
#Buscar todos los elementos que el h2 contenga en su texto
#la palabra python
python_jobs = results.find_all(
    "h2", string=lambda text:"python" in text.lower()
)
#Buscar cada elemento que tenga referencia de python_jobs
#y almacenarlo en python_jobs_elements
python_jobs_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]
#Mostrar información de python_jobs_elements
for job_element in python_jobs_elements:
    title_element = job_element.find("h2",class_="title")
    company_element = job_element.find("h3",class_="company")
    location_element = job_element.find("p",class_="location")
    #De la lista de elementos con la etiqueta "a" buscamos
    #el primer elemento que incluya href
    link_url = job_element.find_all("a")[1]["href"]
    print(company_element.text.strip())
    print(location_element.text.strip())
    print(title_element.text.strip())
    #Imprimimos la salida con link_url
    print(f"Apply Here: {link_url}\n")