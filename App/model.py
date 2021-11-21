"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT.graph import gr
from DISClib.Algorithms.Graphs import scc
from DISClib.Algorithms.Graphs import dijsktra as djk
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():
    """ Inicializa el catalogo
    Crea un grafo dirigido el cual tiene la totalidad de
    aeropuertos y sus rutas dirigidas
    """
    catalogo = {
                "AirportGraph":None


                }

    catalogo["RouteGraphD"] = gr.newGraph(datastructure='ADJ_LIST',
                                              directed=True,
                                              size=9000,
                                              comparefunction=None
                                              )
    catalogo["RouteGraphNoD"] = gr.newGraph(datastructure='ADJ_LIST',
                                              directed=False,
                                              size=14000,
                                              comparefunction=None
                                              )                                        
    return catalogo

# Funciones para agregar informacion al catalogo

def addRoute(catalogo,route):
    #if not gr.containsVertex(catalogo["AirportGraph"] , airport):
   # gr.insertVertex(catalogo["AirportGraph"] , Route["Name"])
   print(route)
    #return None
# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento

def compararUbicacion(elemento1,elemento2):
    if elemento1["latitude"]>=elemento2["latitude"]:
        return True
    else:
        return False