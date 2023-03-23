import webbrowser  # Importation de la bibliothèque pour contrôler le navigateur Web
import time  # Importation de la bibliothèque pour mesurer le temps et mettre en pause le programme
import os  # Importation de la bibliothèque pour exécuter des commandes système
import json  # Importation de la bibliothèque pour travailler avec des fichiers JSON

with open('urls.json', 'r') as f:  # Ouvre le fichier 'urls.json' en mode lecture
    # Charge le contenu du fichier dans la variable "urls" sous forme de liste
    data = json.load(f)

urls = data['urls']
for i in range(30):
    for url in urls: # Parcourt chaque URL dans la liste "urls"
        try:
            webbrowser.open_new(url) # Ouvre un nouvel onglet dans le navigateur par défaut et affiche l'URL correspondante
        except:
            print(f"Erreur : impossible d'ouvrir l'URL {url}")
        time.sleep(5)  # Met en pause le programme pendant le temps calculé précédemment

# Tue le processus du navigateur en cours d'utilisation
os.system("taskkill /im brave.exe /f")
