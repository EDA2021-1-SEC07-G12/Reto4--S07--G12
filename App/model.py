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
import time
from math import *
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

    catalogo['MapAirports'] = mp.newMap(numelements=3971,
                                     maptype='PROBING',
                                     comparefunction=None)
    catalogo['MapAirportsIATA'] = mp.newMap(numelements=3971,
                                     maptype='PROBING',
                                     comparefunction=None)
    catalogo["RouteGraphD"] = gr.newGraph(datastructure='ADJ_LIST',
                                              directed=True,
                                              size=3971,
                                              comparefunction=None
                                              )
    catalogo["RouteGraphNoD"] = gr.newGraph(datastructure='ADJ_LIST',
                                              directed=False,
                                              size=5,
                                              comparefunction=None
                                              )                                        
    return catalogo

# Funciones para agregar informacion al catalogo

def addRoute(catalogo,route):
    if gr.containsVertex(catalogo["RouteGraphD"] , route["Departure"]) ==False:
        gr.insertVertex(catalogo["RouteGraphD"] , route["Departure"])
    if gr.containsVertex(catalogo["RouteGraphD"] , route["Destination"]) ==False:
        gr.insertVertex(catalogo["RouteGraphD"] , route["Destination"])
    
    if gr.getEdge(catalogo["RouteGraphD"], route["Departure"], route["Destination"]) is None:
       gr.addEdge(catalogo["RouteGraphD"], route["Departure"], route["Destination"] , float(route["distance_km"]))
    return catalogo

def addRoute1(catalogo,route):
    if gr.containsVertex(catalogo["RouteGraphNoD"] , route["Departure"]) ==False:
        gr.insertVertex(catalogo["RouteGraphNoD"] , route["Departure"])
    if gr.containsVertex(catalogo["RouteGraphNoD"] , route["Destination"]) ==False:
        gr.insertVertex(catalogo["RouteGraphNoD"] , route["Destination"])
    if gr.getEdge(catalogo["RouteGraphNoD"], route["Departure"], route["Destination"]) is None:
        gr.addEdge(catalogo["RouteGraphNoD"], route["Departure"], route["Destination"] , float(route["distance_km"]))
    return catalogo

def addAirport(catalogo,Airport):
    mapa=catalogo["MapAirports"]
    mp.put(mapa, Airport["Name"], Airport)
    return catalogo

def addAirportsIATA(catalogo,Airport):
    mapa=catalogo["MapAirportsIATA"]
    mp.put(mapa, Airport["IATA"], Airport)
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

def req_3(catalogo, Ciudad1,Ciudad2):
    """
    Calcula los caminos de costo mínimo desde la estacion initialStation
    a todos los demas vertices del grafo
    """
    
    mapaCiudad=catalogo["Map"]
    ciudad1=mp.get(mapaCiudad,Ciudad1)["value"]
    ciudad2=mp.get(mapaCiudad,Ciudad2)['value']
    tupla1 = (float(ciudad1["lat"]) , float(ciudad1["lng"]))
    tupla2=(float(ciudad2["lat"]) , float(ciudad2["lng"]))
    
    llave1= DiferenciaDistancia(catalogo,tupla1)
    IATA1=lt.getElement(llave1,2)
    print(llave1)
    print(IATA1)
    print(gr.containsVertex(catalogo["RouteGraphD"], IATA1))

    llave2=DiferenciaDistancia(catalogo,tupla2)
    
    IATA2=lt.getElement(llave2,2)
    
    
    dijsktra=djk.Dijkstra(catalogo["RouteGraphD"], IATA1)
    
    return djk.pathTo(dijsktra,IATA2)
def req_4(catalogo,millas,inicio):
    km=millas*1.6
    grafo= catalogo["RouteGraphD"]
    dijsktra = djk.Dijkstra(grafo, inicio)
    camino1=0
    distancia=11111110
    distancia1=0
    for i in lt.iterator(gr.vertices(grafo)):
        if djk.hasPathTo(dijsktra, i):
            camino= lt.size(djk.pathTo(dijsktra,i))
            distancia= djk.distTo(dijsktra,i)
            
            if distancia<millas and camino>=camino1:
                
                camino1 = lt.size(djk.pathTo(dijsktra,i))
                distancia1= djk.distTo(dijsktra,i)
    print(distancia<km)
    print(camino>=camino1)
    return (distancia1, camino1)

def req_5(catalogo,IATA):
    return gr.degree(catalogo["RouteGraphD"],IATA)

# Funciones utilizadas para comparar elementos dentro de una lista


def DiferenciaDistancia(catalogo,tupla):
    mapa=catalogo["MapAirports"]
    
    valor1=111111111111111111111110
    for i in lt.iterator(mp.keySet(mapa)): 
        valor= mp.get(mapa,i)["value"]
        diferencia= DiferenciaDistancia1(tupla[0], tupla[1], float(valor["Latitude"]), float(valor["Longitude"]) )
        
        if diferencia<valor1 and gr.containsVertex(catalogo["RouteGraphD"], valor["IATA"]):
            valor1=diferencia
            Aeropuerto = valor["Name"]
            IATA=valor["IATA"]
        
    lista=lt.newList("ARRAY_LIST")
    print(Aeropuerto)
    lt.addLast(lista,Aeropuerto)
    lt.addLast(lista,IATA)
    return lista

def DiferenciaDistancia1(lat1,lon1,lat2,lon2):
    Aaltitude = 2000
    Oppsite  = 20000

    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    Base = 6371 * c
    Bearing =atan2(cos(lat1)*sin(lat2)-sin(lat1)*cos(lat2)*cos(lon2-lon1), sin(lon2-lon1)*cos(lat2)) 

    Bearing = degrees(Bearing)
    Base2 = Base * 1000
    distance = Base * 2 + Oppsite * 2 / 2
    Caltitude = Oppsite - Aaltitude
    return distance/1000
# Funciones de ordenamiento

def compararUbicacion(elemento1,elemento2):
    if elemento1["latitude"]>=elemento2["latitude"]:
        return True
    else:
        return False




