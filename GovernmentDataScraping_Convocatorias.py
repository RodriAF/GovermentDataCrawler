# This code is meant to be used for Convocatorias because it has unique BDNS codes

# Import the libraries needed
from urllib import request
from bs4 import BeautifulSoup
from urllib.error import HTTPError
import pandas as pd
import numpy as np
import os
​
# Get the direction where the dataset is
os.getcwd()
os.chdir()

# Loading the dataset
convocatorias = pd.read_csv('convocatoriasINDEX.csv',header = 0,low_memory=False)
​
# Get only the column with the BDNS code
codigos1 = convocatorias.codigo_bdns;codigos1 
​
# This solves the verifying access problem
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
​
    
# Creating output dataframe and columns
## Skip or Comment this part if it's not the first time the code is executed
data = pd.DataFrame(codigos1)
    
data['importe_total'] = ''
data['tipo_beneficiario'] = ''
data['sector_beneficiario'] = ''
data['region_impacto'] = ''
data['finalidad'] = ''
​
## If it's not the first time the code is executed and there is already data saved
data = pd.read_csv('convocatorias_complete.csv',header = 0,low_memory=False)


# Counter for progress
n = 0 # Substitute this n for the last n saved
codigos1[n:]
# n = # if n != 0
for i in codigos1[n:].index: 
# si n=0 empieza desde el principio, si n es otro numero empieza desde donde lo dejaste
        
        
    url = 'https://www.pap.hacienda.gob.es/bdnstrans/GE/es/convocatoria/' + str(codigos1[i])
        
    
        
    try:
        rawpage = request.urlopen(url) # Open the url
    except HTTPError as err:
        if err.code == 404:
            print(codigos1[i]," not found")
               
    else:
        #Extract only the article of the page
        contenido = BeautifulSoup(rawpage, "lxml").article
            
        # Assigning values
        importe_total = contenido.find_all('div',attrs = 'bloque')[7]
        data.importe_total[i] = 'NaN'
        if importe_total.find('p') is not None:
            data.importe_total[i] = importe_total.find('p').get_text()
        
        tipo_beneficiario = contenido.find_all('div',attrs = 'bloque')[10]
        data.tipo_beneficiario[i] = 'NaN'
        if tipo_beneficiario.find('li') is not None:
            data.tipo_beneficiario[i] = tipo_beneficiario.find('li').get_text()
                
        sector_beneficiario = contenido.find_all('div',attrs = 'bloque')[11]
        data.sector_beneficiario[i] = 'NaN'
        if sector_beneficiario.find('li') is not None:
            data.sector_beneficiario[i] = sector_beneficiario.find('li').get_text()
​
            
        region_impacto = contenido.find_all('div',attrs = 'bloque')[12]
        data.region_impacto[i] = 'NaN'
        if region_impacto.find('li') is not None:
            data.region_impacto[i] = region_impacto.find('li').get_text()
            
            
        finalidad = contenido.find_all('div',attrs = 'bloque')[13]
        data.finalidad[i] = 'NaN'
        if finalidad.find('p') is not None:
            data.finalidad[i] = finalidad.find('p').get_text()
​
    n += 1
    print(round(n / len(data.index) * 100, 4),'%')
        
# Saving the data
data.to_csv("convocatorias_complete.csv")