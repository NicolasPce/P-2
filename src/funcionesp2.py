import pandas as pd

# Función para dejar la clasficación sacada del web scraping de la liga limpia
# Le damos la tabla de wikipedia y nos la devuleve simplificada, solo con el nombre del equipo y los puntos

def clasif(x):
    ligaesp = []
    for f in x.find_all("tr"): 
        fila = [elemento for elemento in f.find_all("td")] 
        if len(fila) > 1:
            diccionario_2 = {"Equipo": fila[0].text,
                          "Puntos":int(fila[1].text)}
            ligaesp.append(diccionario_2)
    laliga1 = pd.DataFrame(ligaesp)        
    return laliga1
