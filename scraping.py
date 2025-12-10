import requests
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator

url = "https://www.bbc.com/news/articles/cwyx83n00k6o"

respuesta = requests.get(url)

if respuesta.status_code != 200:
    print("Error al acceder a la página:", respuesta.status_code)
    exit()

soup = BeautifulSoup(respuesta.text, "html.parser")

titulo = soup.find("h1").get_text(strip=True)

parrafos = soup.find_all("p")

parrafos_extraidos = [p.get_text(strip=True) for p in parrafos[:5]]

traductor = GoogleTranslator(source='en', target='es')

titulo_traducido = traductor.translate(titulo)
parrafos_traducidos = [traductor.translate(p) for p in parrafos_extraidos]

print("\n TÍTULO ORIGINAL ")
print(titulo)

print("\n EL TÍTULO FUE TRADUCIDO ")
print(titulo_traducido)

print("\n PÁRRAFOS TRADUCIDOS ")
for i, p in enumerate(parrafos_traducidos, 1):
    print(f"\nPárrafo {i}:")
    print(p)
