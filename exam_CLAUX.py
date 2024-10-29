from pymongo import MongoClient
from pprint import pprint
import re 

### Connection à la base de don
client = MongoClient(
    host="127.0.0.1",
    port = 27017,
    username = "datascientest",
    password = "dst123"
)


sample = client['sample']
books = sample['books']

print("Afficher la liste des bases de données disponibles.")
print(client.list_database_names())
print("--------------------------\n")

print("Afficher la liste des collectionsibles dans cette base de données")
print(client.list_database_names())
print("--------------------------\n")

print("Afficher un des documents de cette collection ")
pprint(books.find_one())
print("--------------------------\n")

print("Afficher le nombre de documents dans cette collection")
print(books.count_documents({}))
print("--------------------------\n")

print(" Afficher le nombre de livres avec plus de 400 pages, affichez ensuite le nombre de livres ayant plus de 400 pages ET qui sont publiés.")
for i in list(books.find({"$and": [{"pageCount" : {"$gt": 400}},{"status" : "PUBLISH"}]})):
    pprint(i)

print(" Afficher le nombre de livres ayant le mot-clé Android dans leur description (brève ou longue).")
print(books.count_documents({"$or": [{"shortDescription" :  {"$regex" : "Android" }}, {"longDescription":  {"$regex" : "Android" }}]}))
