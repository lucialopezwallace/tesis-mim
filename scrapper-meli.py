# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 17:52:19 2022

@author: lulopezwalla
"""

pageUrl= "https://listado.mercadolibre.com.ar/autos-usados"
driver = webdriver.Firefox(executable_path = 'geckodriver')

from selenium import webdriver
from bs4 import BeautifulSoup
import sqlite3
import pandas as pd
from csv import writer
from datetime import datetime

#Funcion para traer un url de X pagina
def get_page_url(pageNumber, marca):
    initial_range = 1 + 48 * (pageNumber - 1)
    base_page_url = "https://autos.mercadolibre.com.ar/"
    base_page_url = base_page_url + marca + '/autos-usados_Desde_{}_ITEM*CONDITION_2230581_NoIndex_True'.format(initial_range)
    return base_page_url

#Funcion para traer los objetos de la publicacion
def publication_object(car_publication,marca):
    #Obtiene el precio
    price = car_publication.find(class_="price-tag-fraction").text
    price.replace(".",",")
    
    #Obtiene la moneda
    currency = car_publication.find(class_="price-tag-symbol").text
    
    #Obtiene la ubicación
    ubication = car_publication.find(class_="ui-search-item__location").text
    ubication = ubication.split(" - ")
    localidad = ubication[0]
    try:
        provincia = ubication[1]
    except:
        provincia = ""
    
    #Obtiene el KM
    year = car_publication.find_all(class_="ui-search-card-attributes__attribute")[0].text

    #Obtiene el Año
    km = car_publication.find_all(class_="ui-search-card-attributes__attribute")[1].text
    km = km.split(" ")
    km = km[0]
    
    #Obtiene la marca
    marca = marca
    
    #Obtiene el titulo
    title = car_publication.find(class_="ui-search-item__title").text
    
    #Me devuelve la fecha actual
    current_date = datetime.now().date()
    
    return {"precio": price,
            "currency": currency,
            "localidad": localidad,
            "provincia": provincia,
            "km": km, 
            "year": year,
            "marca": marca,
            "title": title,
            "visto": current_date}
    
    
#Funcion que recorre todas las publicaciones de una pagina
def parser_and_save_items(pageUrl,marca):
     #Voy a la pagina que quiero scrapear
     driver.get(pageUrl)
     #Obtengo su HTML
     html_code = driver.page_source
     #Creo un objeto a partir del HTML
     soup = BeautifulSoup(html_code, 'lxml')
     #Trae todas las publiaciones de la pagina actual
     all_publication = soup.find_all("li", class_="ui-search-layout__item")
     
     #Convierte las publicaciones en objetos
     df = pd.DataFrame()
     
     for car_publication in all_publication:
         # print(publication_object(car_publication))
         # Buco los atributos
         data = publication_object(car_publication,marca)
         df_new = pd.DataFrame(data,index = [0])
         df = df.append(df_new, ignore_index = True)
     
     export_data(df)
     print('exportado')

#Funcion para exportar data a un .csv
def export_data(df):
    df.to_csv('data_publications.csv',mode='a', sep=';', encoding='utf-8-sig', index=False, header=False)
         
# Itera por todas las páginas y guarda información en el csv

marcas = ['volkswagen', 'ford', 'renault', 'peugeot', 'chevrolet', 'toyota', 'fiat', 'audi', 'citroen','audi']

for marca in marcas:
    for actual_number_page in range(1,35+1):
    
        url_page = get_page_url(actual_number_page,marca)
        print(url_page)
        parser_and_save_items(url_page,marca)

