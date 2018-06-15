import hug
import mysql.connector
import json

conn = mysql.connector.connect(host="localhost", user="root", password="", database="pokemon")

#permet de lister tous les pokemons
@hug.get('/pokemons')
def listPok():
    conn = mysql.connector.connect(host="localhost", user="root", password="", database="pokemon")
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM POKEMON_TABLE""")
    result = cursor.fetchall()
    for row in result:
        return json.dumps(result)
    conn.close()


#permet d'afficher un pokemeon via son ID
@hug.get('/detailPok')
def detailPok(id):
    conn = mysql.connector.connect(host="localhost", user="root", password="", database="pokemon")
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM POKEMON_TABLE where id = %s""", [int(id)])
    response = cursor.fetchall()
    return response
    conn.close()


#PERMET DE SUPPRIMER UN POKEMON VIA SON ID
@hug.delete('/deletePok')
def deletePok(id):
    conn = mysql.connector.connect(host="localhost", user="root", password="", database="pokemon")
    cursor = conn.cursor()
    cursor.execute("""DELETE FROM POKEMON_TABLE where id = %s""", [int(id)])
    return "Element supprimé"
    conn.close()



#permet d'ajouter des pokemons
@hug.post('/addPok')
def addPok(id,name,typePok,total,hp,attack,defense,spAtack,spDefense,speed):
    conn = mysql.connector.connect(host="localhost", user="root", password="", database="pokemon")
    cursor = conn.cursor()
    data = (id,name,typePok,total,hp,attack,defense,spAtack,spDefense,speed)
    cursor.execute("""INSERT INTO pokemon_table(id,name,typePok,total,hp,attack,defense,spAtack,spDefense,speed)
         VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", [data])
    conn.commit()
    return "Element ajouté"
    conn.close()


#permet  de mettre à jour un pokemon via son ID
@hug.put('/majPok')
def majPok(id):
    conn = mysql.connector.connect(host="localhost", user="root", password="", database="pokemon")
    cursor = conn.cursor()
    data = (id, name, typePok, total, hp, attack, defense, spAtack, spDefense, speed)
    cursor.execute(""""UPDATE POKEMON_TABLE SET 
          nom = %s ,
          typePok = %s ,
          total =  %s,
          hp = %s,
          attack = %s,
          defense = %s,
          spAtack = %s ,
          spDefense = %s,
          speed = %s
          WHERE id = %s """, [data])

    conn.commit()
    return "Mise à jour effectué"
    conn.close()





