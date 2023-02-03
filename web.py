import requests
import psycopg2
import csv
from bs4 import BeautifulSoup


url ='https://www.jumia.ci/mlp-black-friday-h-temple-des-tout-petits/'

reponse = requests.get(url)

if reponse.ok:
    soup = BeautifulSoup(reponse.text, "html.parser")
    les_articles = soup.findAll('article')
    [print(str(article.text) + '\n\n') for article in les_articles]

    chemin = r"C:\Users\HP\PycharmProjects\bs4\produit-bébé.csv"

    with open(chemin, "w",  encoding="utf-8") as f:
        for article in les_articles:
            f.write(f"{article.text}\n\n")






url1 ='https://www.jumia.ci/telephone-tablette/'

reponse1 = requests.get(url1)

if reponse1.ok:
    soup = BeautifulSoup(reponse1.text, "html.parser")
    les_articles1 = soup.findAll('article')
    [print(str(article.text) + '\n\n') for article in les_articles1]

    chemin = r"C:\Users\HP\PycharmProjects\bs4\Téléphone-tablette.csv"

    with open(chemin, "w",  encoding="utf-8") as f:
        for article in les_articles1:
            f.write(f"{article.text}\n\n")


url2 ='https://www.jumia.ci/epicerie/'

reponse2 = requests.get(url2)

if reponse2.ok:
    soup = BeautifulSoup(reponse2.text, "html.parser")
    les_articles2 = soup.findAll('article')
    [print(str(article.text) + '\n\n') for article in les_articles2]

    chemin = r"C:\Users\HP\PycharmProjects\bs4\epicerie.csv"

    with open(chemin, "w",  encoding="utf-8") as f:
        for article in les_articles2:
            f.write(f"{article.text}\n\n")


url3 ='https://www.jumia.ci/electronique/'

reponse3 = requests.get(url3)

if reponse1.ok:
    soup = BeautifulSoup(reponse3.text, "html.parser")
    les_articles3 = soup.findAll('article')
    [print(str(article.text) + '\n\n') for article in les_articles3]

    chemin = r"C:\Users\HP\PycharmProjects\bs4\electronic.csv"

    with open(chemin, "w",  encoding="utf-8") as f:
        for article in les_articles3:
            f.write(f"{article.text}\n\n")


url4 ='https://www.jumia.ci/maison-cuisine-jardin/'

reponse4 = requests.get(url4)

if reponse4.ok:
    soup = BeautifulSoup(reponse4.text, "html.parser")
    les_articles4 = soup.findAll('article')
    [print(str(article.text) + '\n\n') for article in les_articles4]

    chemin = r"C:\Users\HP\PycharmProjects\bs4\maison-cuisine-jardin.csv"

    with open(chemin, "w",  encoding="utf-8") as f:
        for article in les_articles4:
            f.write(f"{article.text}\n\n")


url5 ='https://www.jumia.ci/telephone-tablette/'

reponse5 = requests.get(url5)

if reponse1.ok:
    soup = BeautifulSoup(reponse5.text, "html.parser")
    les_articles5 = soup.findAll('article')
    [print(str(article.text) + '\n\n') for article in les_articles5]

    chemin = r"C:\Users\HP\PycharmProjects\bs4\beaute-hygiene-sante.csv"

    with open(chemin, "w",  encoding="utf-8") as f:
        for article in les_articles5:
            f.write(f"{article.text}\n\n")


conn = psycopg2.connect(
    host="127.0.0.1",
    database="Scrapp",
    user="postgres",
    password="admin"
)
cur = conn.cursor()

# Ouvrir le fichier CSV et lire les données
f =  r"C:\Users\HP\PycharmProjects\bs4\beaute-hygiene-sante.csv"
with open(f, "r",  encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        query = "INSERT INTO customers (nom, prix) VALUES (%s, %s)"
        data = (row[1], row[0])
        cur.execute(query, data)

conn.commit()

# Fermer la connexion
cur.close()
conn.close()





