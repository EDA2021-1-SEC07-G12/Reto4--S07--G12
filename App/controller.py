﻿"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *  Prueba
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

from typing_extensions import final
import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""
def initCatalog():
    catalog= model.newCatalog()
    return catalog


def loadData(catalog):
    loadAirport(catalog)

def loadAirport(catalog):
    airportFile = cf.data_dir + 'routes_full.csv'
    input_file = csv.DictReader(open(airportFile, encoding='utf-8'))
    for Airport in input_file:
        
        model.addRoute(catalog,Airport)
       # model.addRoute1(catalog,Airport)
        model.addEdge(catalog,Airport)
      
    
        
# Inicialización del Catálogo de libros

# Funciones para la carga de datos

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
def requerimiento1(catalog):
    
    return model.req_1(catalog)

def requerimiento2(catalog):
    IATA1=input("Introduce codigo IATA 1: ")
    IATA2=input("Introduce codigo IATA 2: ")
     
    return model.req_2(catalog,IATA1,IATA2)

def requerimiento3(catalog):
    origen=input("Introduce ciudad de origen: ")
    final=input("Introduce ciudad de destino: ")
     
    return model.req_3(catalog,origen,final)



def req_5(catalog):
    iata=input("Inserte aeropuerto afectado ")
    return model.req_5(catalog,iata)
def connectedComponents(analyzer):
    """
    Numero de componentes fuertemente conectados
    """
    return model.req_1(analyzer)