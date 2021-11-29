import json
import pandas as pd
import numpy as np
import urllib.request
import os.path
import time

from pprint import pprint
# ----------------------------
print('INI: json2csv_ISTAC_empleo.py')
# Extracción de un cubo de datos de 4 dimensiones a partir de un Json y lo pasamos a un csv

# Definimos la ruta de los ficheros de entrada y de salida y la fecha en la que descargamos el fichero
pathIN = 'Z:\\DATOS_ISTAC\\EMPLEOS\\'
pathOUT = 'G:\\Mi unidad\\Repositorio_codigos\\Codigos_produccion\\ISTAC\\EMPLEOS\Python\\json2csv_empleos\\'
# Empleos según situaciones profesionales y ramas de actividad (CNAE-09). Municipios por islas de Canarias y trimestres.
# http://www.gobiernodecanarias.org/istac/jaxi-istac/menu.do?uripub=urn:uuid:b3b279af-26af-41f7-9292-745ccd8184e6
fichero = 'EmpleoRegistrado_hasta2008_ISTAC'
# fichero = 'EmpleoRegistrado_from2009_ISTAC'
filename = pathIN + fichero + '.json'
ficheroOUT = pathOUT + 'OUT\\tabla_out_' + fichero + '.csv'

# Leemos el json
with open(filename, 'r', encoding="utf-8") as ff:
  datos = json.load(ff)

translate_dict = []
columns = []
for item in datos["categories"]:
    columns.append(item["variable"])
    columns.append(item["variable"] + "_orig")
    translate_dict.append(dict(zip(item["codes"], item["labels"])))

rows = []
for data in datos["data"]:
    row = [data["Valor"]]
    for idx, item in enumerate(data["dimCodes"]):
        row.append(translate_dict[idx][item])
        row.append(item)
    rows.append(row)

df = pd.DataFrame(rows, columns=["Empleos"] + columns)

# df.to_csv(ficheroOUT,sep = ';',index=False)

print('FIN: json2csv_ISTAC_empleo.py')
print('FIN')