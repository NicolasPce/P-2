import requests
import pandas as pd
import matplotlib.pylab as plt
from bs4 import BeautifulSoup
import seaborn as sns
import os
import src.funcionesp2 as sf

# Hacemos web scraping de la clasificación de La Liga
url_liga='https://es.wikipedia.org/wiki/Primera_División_de_España_2021-22'
html_liga = requests.get(url_liga)

# soup
soup_liga = BeautifulSoup(html_liga.content, "html.parser")
liga = soup_liga.findAll("table")[-52]


# Aplicamos la función para dejar la clasificación limpia
laliga = sf.clasif(liga)


# Y reemplazamos los nombres por el código con el que queremos nombrar al equipo
laliga["Equipo"] = laliga["Equipo"].replace({'Real Sociedad\n':"RSO", "Real Madrid C. F.\n":"RMD", "Sevilla F. C.\n": "SEV",
                               "Atlético de Madrid\n":"ATM", "Real Betis Balompié\n":"BET", "Getafe C. F.\n":"GET",
                               "Levante U. D.\n":"LEV", "Deportivo Alavés\n":"ALA", "Elche C. F.\n": "ELC",
                               "R. C. Celta de Vigo\n":"CEL", 'Cádiz C. F.\n':"CAD", "Granada C. F.\n":"GRA", "Villarreal C. F.\n": "VIL",
                               "R. C. D. Mallorca\n":"MAL", "Valencia C. F.\n":"VAL", "R. C. D. Espanyol\n":"ESP",
                               "F. C. Barcelona\n":"FCB", "Athletic Club\n":"ATH","Rayo Vallecano\n": "RYV", "C. A. Osasuna\n": "OSA"}) 

 # Nos traemos el data set del fifa tratado
equipos = pd.read_csv("Data/equipos.csv",encoding = "ISO-8859-1")                              

# Juntamos la tabla de la media de valoración, con la tabla de la clasificación
LaLiga = pd.merge(laliga, equipos, left_on='Equipo', right_on='Equipo')
LaLiga.tail()

# Observamos la correlación actual
corr = LaLiga.corr()
corr

# Fijamos el tamaño de la gráfica y la visualizamos
sns.set({"figure.figsize":(20,10)})
sns.set(font_scale = 1.15)
LL = sns.scatterplot(x="Media_FIFA", y="Puntos", hue="Equipo", style="Equipo", palette="deep",data=LaLiga, s=400, legend="full")
plt.setp(LL.get_legend().get_texts(), fontsize='17')
plt.setp(LL.get_legend().get_title(), fontsize='17')

# Guardamos la gráfica
LL.figure.savefig("graph.png")
