import requests
from bs4 import BeautifulSoup

url = 'https://www.saude.gov.br/noticias'
'''Aqui coloca-se o url do site'''

req = requests.get(url)

soup = BeautifulSoup(req.content,'html.parser')

lista_casos = soup.find_all('h2',class_ ='tileHeadline')
''' aqui coloca-se onde/classe/o restante'''

for lista_incidentes in lista_casos:
    lista = lista_incidentes.find_all('a', href = '-envia-20-respiradores-para-sao-paulo')
    for lista_dados in lista:
       print(lista_dados.next_element)

for listaa_incidentes2 in lista_casos:
    lista2 = listaa_incidentes2.find_all('a', href ='/noticias/agencia-saude/46899-governo-do-brasil-ajuda-municipios-do-interior-do-amazonas')
    for lista_dados2 in lista2:
        print(lista_dados2.next_element)

