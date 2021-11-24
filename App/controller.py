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
        
        model.addRoutes(catalog,Airport)
       # model.addEdge(catalog,Airport)
      
    
        
# Inicialización del Catálogo de libros

# Funciones para la carga de datos

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
def requerimiento1(catalog):
    r=model.req1(catalog)
    return r

def requerimiento2(catalog, codigo1, codigo2):
    r=model.req2(catalog, codigo1, codigo2)
    return r


