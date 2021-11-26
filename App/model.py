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
from DISClib.Algorithms.Graphs import prim as pr
from DISClib.Algorithms.Graphs import bellmanford as bf
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
                "RouteGraphD":None,
                "Map":None,
                "RouteGraphNoD":None


                }

    catalogo['Map'] = mp.newMap(numelements=3971,
                                     maptype='PROBING',
                                     comparefunction=None)
    catalogo["RouteGraphD"] = gr.newGraph(datastructure='ADJ_LIST',
                                              directed=True,
                                              size=3971,
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
    if not gr.containsVertex(catalogo["RouteGraphD"], route["Departure"]):
        gr.insertVertex(catalogo["RouteGraphD"] , route["Departure"])
    
    if not gr.containsVertex(catalogo["RouteGraphD"], route["Destination"]):
        gr.insertVertex(catalogo["RouteGraphD"] , route["Destination"])

    #if gr.getEdge(catalogo["RouteGraphD"], route["Departure"], route["Destination"]) == None:
        #gr.addEdge(catalogo["RouteGraphD"], route["Departure"], route["Destination"] , route["distance_km"])
        
       
    return catalogo


def addRoute1(catalogo,route):
    valor= mp.get(catalogo["Map"], route["Departure"])
    valor1= mp.get(catalogo["Map"], route["Destination"])
    if lt.isPresent(valor["value"], route["Destination"]) and lt.isPresent(valor1["value"], route["Departure"]):
        gr.insertVertex(catalogo["RouteGraphNoD"] , route["Departure"])
        gr.insertVertex(catalogo["RouteGraphNoD"] , route["Destination"])
        if gr.getEdge(catalogo["RouteGraphNoD"], route["Departure"], route["Destination"])==None:
            gr.addEdge(catalogo["RouteGraphNoD"], route["Departure"], route["Destination"] , int(route["distance_km"]))
    
    return catalogo
def addRoutes(catalogo,ruta):
    mapa=catalogo["Map"]
    if not mp.contains(mapa,ruta["Departure"]):
        lista=lt.newList("ARRAY_LIST")
        lt.addLast(lista,ruta["Destination"])
        mp.put(mapa, ruta["Departure"], lista)
    else:
        valor = mp.get(mapa,ruta["Departure"])["value"]
        if not lt.isPresent(valor,ruta["Destination"]):
            lt.addLast(valor,ruta["Destination"])
            
        mp.put(mapa, ruta["Departure"], valor)


    
    
    
    return catalogo


def addEdge(catalogo,route):
    
    if gr.getEdge(catalogo["RouteGraphD"], route["Departure"], route["Destination"]) == None:
        gr.addEdge(catalogo["RouteGraphD"], route["Departure"], route["Destination"] , route["distance_km"])
    
    return catalogo
# Funciones para creacion de datos

# Funciones de consulta


def req_1(catalogo):
    """
    Calcula los componentes conectados del grafo
    Se utiliza el algoritmo de Kosaraju
    """
    
    return scc.connectedComponents(scc.KosarajuSCC(catalogo['RouteGraphD']))

def req_2(catalogo ,IATA1,IATA2):
    catalogo['components'] = scc.KosarajuSCC(catalogo['RouteGraphD'])

    return scc.stronglyConnected(catalogo["components"], IATA1,IATA2)

def connectedComponents(analyzer):
    """
    Calcula los componentes conectados del grafo
    Se utiliza el algoritmo de Kosaraju
    """
    Variable=  scc.KosarajuSCC(analyzer['RouteGraphD'])
    return scc.connectedComponents(Variable)

def req_3(catalogo, origen,destino):
    pr.PrimMST(catalogo['RouteGraphD'])
    return pr.PrimMST(catalogo['RouteGraphD'])


def req_4(catalogo,millas):
    km=millas*1.6


def req_5(catalogo,IATA):
    return gr.degree(catalogo["RouteGraphD"],IATA)

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento

def compararUbicacion(elemento1,elemento2):
    if elemento1["latitude"]>=elemento2["latitude"]:
        return True
    else:
        return False




