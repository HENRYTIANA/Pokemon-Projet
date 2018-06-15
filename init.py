import requests
from bs4 import BeautifulSoup
import mysql.connector

conn = mysql.connector.connect(host="localhost",user="root",password="", database="pokemon")
cursor = conn.cursor()

url= "https://pokemondb.net/pokedex/all"

response =requests.get(url)
html = str(response.content)
soup = BeautifulSoup(html,"html.parser")

tab = soup.find(id="pokedex")
for link in tab.find_all("tr"):
    tab = []
    for l in link.find_all("td"):
        tab.append(l.text)
    if len(tab) != 0:
        cursor.execute(
        """INSERT INTO pokemon_table (id, nom, typePok,total,hp,attack,defense,spAtk,spDef,speed) VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s,%s)""",
        tab)
    else:
        print ("insert terminé")
conn.commit()
conn.close()


