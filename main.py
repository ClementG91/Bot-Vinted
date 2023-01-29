import webbrowser
import time
import os

for i in range (1000):
    url = 'https://www.vinted.fr/femmes/accessoires/bijoux/boucles-doreilles/2431920694-boucle-doreilles'
    webbrowser.open_new_tab(url)
    time.sleep(5)
    os.system("taskkill /im brave.exe /f")
    time.sleep(5)
