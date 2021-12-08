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
from DISClib.ADT import orderedmap as om

from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import selectionsort as sl
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
    catalogo['City'] = mp.newMap(numelements=3971,
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
    catalogo["RouteGraphDAirlines"] = gr.newGraph(datastructure='ADJ_LIST',
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

    if gr.containsVertex(catalogo["RouteGraphDAirlines"] , route["Departure"]) ==False:
        gr.insertVertex(catalogo["RouteGraphDAirlines"] , route["Departure"])
    if gr.containsVertex(catalogo["RouteGraphDAirlines"] , route["Destination"]) ==False:
        gr.insertVertex(catalogo["RouteGraphDAirlines"] , route["Destination"])
    if gr.getEdge(catalogo["RouteGraphD"] , route["Departure"] , route["Destination"]) is None:
        gr.addEdge(catalogo["RouteGraphD"], route["Departure"], route["Destination"] , float(route["distance_km"]))
    gr.addEdge(catalogo["RouteGraphDAirlines"], route["Departure"], route["Destination"] , float(route["distance_km"]))


    """Agregar vertices a no dirigido"""

    return catalogo
    

def CreateNoDir(catalogo):

    grafodir=catalogo["RouteGraphD"]

    for i in lt.iterator(gr.vertices(grafodir)):
        adjacentes= gr.adjacents(grafodir,i)
        for j in lt.iterator(adjacentes):
            adjacentes1= gr.adjacents(grafodir,j)
            if lt.isPresent(adjacentes1,i):
                if gr.containsVertex(catalogo["RouteGraphNoD"] , i) ==False:
                    gr.insertVertex(catalogo["RouteGraphNoD"], i)
                if gr.containsVertex(catalogo["RouteGraphNoD"] , j) ==False:
                    gr.insertVertex(catalogo["RouteGraphNoD"], j)
                if gr.getEdge(catalogo["RouteGraphNoD"] , i , j)==None and gr.getEdge(catalogo["RouteGraphNoD"] , j , i)==None:
                    gr.addEdge(catalogo["RouteGraphNoD"], i,j, gr.getEdge(catalogo["RouteGraphD"] , i , j)["weight"])

    return catalogo

def AddRoute2(catalog,route):
    gradoDir=catalog["RouteGraphD"]

def addAirport(catalogo,Airport):
    mapa=catalogo["MapAirports"]
    mp.put(mapa, Airport["Name"], Airport)
    return catalogo

def addCity(catalogo,City):
    mapa=catalogo["City"]
    
    string=City["city_ascii"]+City["iso2"] + City["admin_name"]
        
    
    mp.put(mapa, string, City)
    return catalogo
def addAirportsIATA(catalogo,Airport):
    mapa=catalogo["MapAirportsIATA"]
    mp.put(mapa, Airport["IATA"], Airport)
    return catalogo
# Funciones para creacion de datos

# Funciones de consulta


def req_1(catalogo):
    grafo= catalogo["RouteGraphDAirlines"]
    lista=lt.newList("ARRAY_LIST")
    mapa=mp.newMap(numelements=gr.numVertices(grafo),
                                     maptype='PROBING',
                                     comparefunction=None)
    for i in lt.iterator(gr.vertices(grafo)):
        adjacentes = gr.indegree(grafo,i)
        adjacentes1 = gr.outdegree(grafo,i)

        mp.put(mapa,i,adjacentes1+adjacentes)
    for j in lt.iterator(gr.vertices(grafo)):
        llave = mp.get(mapa,j)
        lt.addLast(lista,llave)

    lista = sa.sort(lista,adyacentes)
    return lt.subList(lista,1,5)

def req_2(catalogo ,IATA1,IATA2):
    
    kosajaru =scc.KosarajuSCC(catalogo['RouteGraphD'])

    strong = scc.connectedComponents(kosajaru)

    conectados=scc.stronglyConnected(kosajaru,IATA1,IATA2)

    retorno=lt.newList("ARRAY_LIST")
    lt.addLast(retorno,strong)
    lt.addLast(retorno,conectados)

    return retorno


def req_3(catalogo, Ciudad1,Ciudad2):
    """
    Calcula los caminos de costo mínimo desde la estacion initialStation
    a todos los demas vertices del grafo
    """
    
    mapaCiudad=catalogo["City"]
    ciudad1=mp.get(mapaCiudad,Ciudad1)["value"]
    ciudad2=mp.get(mapaCiudad,Ciudad2)['value']
    tupla1 = (float(ciudad1["lat"]) , float(ciudad1["lng"]))
    tupla2=(float(ciudad2["lat"]) , float(ciudad2["lng"]))
    
    llave1= DiferenciaDistancia(catalogo,tupla1)
    IATA1=lt.getElement(llave1,2)
    print(llave1)
    print(IATA1)
    print(llave1)
    
    llave2=DiferenciaDistancia(catalogo,tupla2)
    
    IATA2=lt.getElement(llave2,2)
    print(llave2)
    dijsktra=  djk.Dijkstra(catalogo["RouteGraphNoD"], IATA1)
    
    return  djk.pathTo(dijsktra, IATA2)
    
    
    

    
def req_4(catalogo,millas,inicio):
    km=millas*1.6
    grafo= catalogo["RouteGraphNoD"]
    vertices=gr.vertices(grafo)
    dijsktra = pr.PrimMST(grafo)


    for i in lt.iterator(vertices):
        print(djk.distTo(dijsktra,i))
        #"print(djk.pathTo(dijsktra,))
    #print(dijsktra)
    """camino1=0
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
    return (distancia1, camino1)"""

def req_5(catalogo,IATA):
    digrafo=catalogo["RouteGraphD"]
    grafo=catalogo["RouteGraphNoD"]
    print(lt.size(gr.adjacents(catalogo["RouteGraphD"], IATA)))
    numRoutes= gr.outdegree(digrafo,IATA) + gr.indegree(digrafo,IATA)
    numRoutes1=gr.degree(grafo,IATA) 
    arcos= gr.numEdges(digrafo) - numRoutes
    arcos1=gr.numEdges(grafo)-numRoutes1
    return arcos1
    #print((gr.numVertices(catalogo["RouteGraphNoD"], gr.numEdges(catalogo["RouteGraphNoD"]))))
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


def adyacentes(elemento1,elemento2):
    if elemento1["value"]>=elemento2["value"]:
        return 1
    else:
        return 0