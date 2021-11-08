import pandas as pd

# Nos traemos el data set 
f = pd.read_csv("Data/players_22.csv",encoding = "ISO-8859-1")

# Seleccionamos las columnas que nos interesan
selected_columns = f[["short_name", "overall","club_name","league_name"]]
f2 = selected_columns.copy()

#Nos quedamos con los jugadores de la liga española, y eliminamos la columna que hace referencia a la liga
f3 = f2[f2["league_name"] == "Spain Primera Division"]
f3.drop(["league_name"], axis=1, inplace=True)

#Sustituimos los nombres de los equipos por los mismos códigos anteriores
f3["club_name"] = f3["club_name"].replace({'Real Sociedad':"RSO", "Real Madrid CF":"RMD", "Sevilla FC": "SEV",
                               "AtlÃ©tico de Madrid":"ATM", "Real Betis BalompiÃ©":"BET", "Getafe CF":"GET",
                               "Levante UniÃ³n Deportiva":"LEV", "Deportivo AlavÃ©s":"ALA", "Elche CF": "ELC",
                               "RC Celta de Vigo":"CEL", 'CÃ¡diz CF':"CAD", "Granada CF":"GRA", "Villarreal CF": "VIL",
                               "RCD Mallorca":"MAL", "Valencia CF":"VAL", "RCD Espanyol de Barcelona":"ESP",
                               "FC Barcelona":"FCB", "Athletic Club de Bilbao":"ATH","Rayo Vallecano": "RYV", "CA Osasuna": "OSA"}) 

# Agrupamos los jugadores en sus equipos
ATM1 = f3[f3["club_name"] == "ATM"]
FCB1 = f3[f3["club_name"] == "FCB"]
RMD1 = f3[f3["club_name"] == "RMD"]
VIL1 = f3[f3["club_name"] == "VIL"]
SEV1 = f3[f3["club_name"] == "SEV"]
RSO1 = f3[f3["club_name"] == "RSO"]
CEL1 = f3[f3["club_name"] == "CEL"]
BET1 = f3[f3["club_name"] == "BET"]
ATH1 = f3[f3["club_name"] == "ATH"]
VAL1 = f3[f3["club_name"] == "VAL"]
LEV1 = f3[f3["club_name"] == "LEV"]
GRA1 = f3[f3["club_name"] == "GRA"]
GET1 = f3[f3["club_name"] == "GET"]
ALA1 = f3[f3["club_name"] == "ALA"]
ESP1 = f3[f3["club_name"] == "ESP"]
ELC1 = f3[f3["club_name"] == "ELC"]
OSA1 = f3[f3["club_name"] == "OSA"]
CAD1 = f3[f3["club_name"] == "CAD"]
RYV1 = f3[f3["club_name"] == "RYV"]
MAL1 = f3[f3["club_name"] == "MAL"]

# Actualizamos los equipos seleccionando solos sus 11 mejores jugadores
RMD2 = RMD1.nlargest(11,'overall')
ATM2 = ATM1.nlargest(11,'overall')
FCB2 = FCB1.nlargest(11,'overall')
VIL2 = VIL1.nlargest(11,'overall')
SEV2 = SEV1.nlargest(11,'overall')
RSO2 = RSO1.nlargest(11,'overall')
CEL2 = CEL1.nlargest(11,'overall')
BET2 = BET1.nlargest(11,'overall')
ATH2 = ATH1.nlargest(11,'overall')
VAL2 = VAL1.nlargest(11,'overall')
LEV2 = LEV1.nlargest(11,'overall')
GRA2 = GRA1.nlargest(11,'overall')
GET2 = GET1.nlargest(11,'overall')
ALA2 = ALA1.nlargest(11,'overall')
ESP2 = ESP1.nlargest(11,'overall')
ELC2 = ELC1.nlargest(11,'overall')
OSA2 = OSA1.nlargest(11,'overall')
CAD2 = CAD1.nlargest(11,'overall')
RYV2 = RYV1.nlargest(11,'overall')
MAL2 = MAL1.nlargest(11,'overall')

# Le añadimos una columna con la media del equipo
RMD2['average'] = RMD2["overall"].mean()
ATM2['average'] = ATM2["overall"].mean()
FCB2['average'] = FCB2["overall"].mean()
VIL2['average'] = VIL2["overall"].mean()
SEV2['average'] = SEV2["overall"].mean()
RSO2['average'] = RSO2["overall"].mean()
CEL2['average'] = CEL2["overall"].mean()
BET2['average'] = BET2["overall"].mean()
ATH2['average'] = ATH2["overall"].mean()
VAL2['average'] = VAL2["overall"].mean()
LEV2['average'] = LEV2["overall"].mean()
GRA2['average'] = GRA2["overall"].mean()
GET2['average'] = GET2["overall"].mean()
ALA2['average'] = ALA2["overall"].mean()
ESP2['average'] = ESP2["overall"].mean()
ELC2['average'] = ELC2["overall"].mean()
OSA2['average'] = OSA2["overall"].mean()
CAD2['average'] = CAD2["overall"].mean()
RYV2['average'] = RYV2["overall"].mean()
MAL2['average'] = MAL2["overall"].mean()

# Ahora nos quedamos con sólo una línea (lo que queremos es la media del equipo)
RMD3 = RMD2.nlargest(1,'overall')
ATM3 = ATM2.nlargest(1,'overall')
FCB3 = FCB2.nlargest(1,'overall')
VIL3 = VIL2.nlargest(1,'overall')
SEV3 = SEV2.nlargest(1,'overall')
RSO3 = RSO2.nlargest(1,'overall')
CEL3 = CEL2.nlargest(1,'overall')
BET3 = BET2.nlargest(1,'overall')
ATH3 = ATH2.nlargest(1,'overall')
VAL3 = VAL2.nlargest(1,'overall')
LEV3 = LEV2.nlargest(1,'overall')
GRA3 = GRA2.nlargest(1,'overall')
GET3 = GET2.nlargest(1,'overall')
ALA3 = ALA2.nlargest(1,'overall')
ESP3 = ESP2.nlargest(1,'overall')
ELC3 = ELC2.nlargest(1,'overall')
OSA3 = OSA2.nlargest(1,'overall')
CAD3 = CAD2.nlargest(1,'overall')
RYV3 = RYV2.nlargest(1,'overall')
MAL3 = MAL2.nlargest(1,'overall')

# Elimnamos las columnas del nombre del mejor jugador del equipo y de su media, 
# quedandonosos sólo con las columnas del código del equipo y la media del mismo

RMD3.drop(["short_name"] , axis=1, inplace=True)
RMD3.drop(["overall"] , axis=1, inplace=True)
FCB3.drop(["short_name"] , axis=1, inplace=True)
FCB3.drop(["overall"] , axis=1, inplace=True)
ATM3.drop(["short_name"] , axis=1, inplace=True)
ATM3.drop(["overall"] , axis=1, inplace=True)
VIL3.drop(["short_name"] , axis=1, inplace=True)
VIL3.drop(["overall"] , axis=1, inplace=True)
SEV3.drop(["short_name"] , axis=1, inplace=True)
SEV3.drop(["overall"] , axis=1, inplace=True)
RSO3.drop(["short_name"] , axis=1, inplace=True)
RSO3.drop(["overall"] , axis=1, inplace=True)
CEL3.drop(["short_name"] , axis=1, inplace=True)
CEL3.drop(["overall"] , axis=1, inplace=True)
BET3.drop(["short_name"] , axis=1, inplace=True)
BET3.drop(["overall"] , axis=1, inplace=True)
ATH3.drop(["short_name"] , axis=1, inplace=True)
ATH3.drop(["overall"] , axis=1, inplace=True)
VAL3.drop(["short_name"] , axis=1, inplace=True)
VAL3.drop(["overall"] , axis=1, inplace=True)
LEV3.drop(["short_name"] , axis=1, inplace=True)
LEV3.drop(["overall"] , axis=1, inplace=True)
GRA3.drop(["short_name"] , axis=1, inplace=True)
GRA3.drop(["overall"] , axis=1, inplace=True)
GET3.drop(["short_name"] , axis=1, inplace=True)
GET3.drop(["overall"] , axis=1, inplace=True)
ALA3.drop(["short_name"] , axis=1, inplace=True)
ALA3.drop(["overall"] , axis=1, inplace=True)
ESP3.drop(["short_name"] , axis=1, inplace=True)
ESP3.drop(["overall"] , axis=1, inplace=True)
ELC3.drop(["short_name"] , axis=1, inplace=True)
ELC3.drop(["overall"] , axis=1, inplace=True)
OSA3.drop(["short_name"] , axis=1, inplace=True)
OSA3.drop(["overall"] , axis=1, inplace=True)
CAD3.drop(["short_name"] , axis=1, inplace=True)
CAD3.drop(["overall"] , axis=1, inplace=True)
RYV3.drop(["short_name"] , axis=1, inplace=True)
RYV3.drop(["overall"] , axis=1, inplace=True)
MAL3.drop(["short_name"] , axis=1, inplace=True)
MAL3.drop(["overall"] , axis=1, inplace=True)

# Juntamos todos los equipos
equipos = pd.concat([RMD3, ATM3, FCB3, SEV3, VIL3, RSO3, RYV3, CEL3, BET3, ATH3, VAL3, LEV3, GRA3, GET3, ALA3, ESP3, ELC3, OSA3, CAD3, MAL3])

# Cambiamos el nombre a la columnas, para que coincida el nombre con la tabla de la clasificación
equipos = equipos.rename(columns={'club_name': 'Equipo', 'average': 'Media_FIFA'})

# Guardamos el data set
equipos.to_csv(r'Data/equipos.csv', index = False)