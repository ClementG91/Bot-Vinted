import webbrowser
import time
import os

for i in range (1000):
    url = ''
    webbrowser.open_new_tab(url)
    time.sleep(5)
    os.system("taskkill /im brave.exe /f")
    time.sleep(5)
