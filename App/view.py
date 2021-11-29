"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf

from DISClib.ADT.graph import gr
from DISClib.Algorithms.Graphs import scc
from DISClib.Algorithms.Graphs import dijsktra as djk
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa

sys.setrecursionlimit(sys.getrecursionlimit()*100)

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Encontrar puntos de interconexión aérea")
    print("3- Encontrar clústeres de tráfico aéreo")
    print("4- Encontrar la ruta más corta entre ciudades")
    print("5- Utilizar las millas de viajero")
    print("6- Cuantificar el efecto de un aeropuerto ")
    print("7- Comparar con servicio WEB externo")
    print("8- Visualizar gráficamente los requerimientos")

catalog=controller.initCatalog()

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        contador=0
        print("Cargando información de los archivos ....")
        controller.loadData(catalog)
        print("El numero de arcos del grafo es " + str(gr.numEdges(catalog["RouteGraphD"])))
        print("El numero de vertices del grafo es " + str(gr.numVertices(catalog["RouteGraphD"])))
        print("Datos cargados correctamente")
       

    elif int(inputs[0]) == 2:
        # Funcionesfor i in lt.iterator(gr.edges(catalog["RouteGraphD"])):
        #print(catalog['RouteGraphD'])
        #print(djk.Dijkstra(catalog['RouteGraphD'], "AER"))
        print('El número de componentes conectados es: ' +
        str(controller.connectedComponents(catalog)))


    elif int(inputs[0]) == 3:
        
        h= controller.requerimiento2(catalog)
        print (h)
    elif int(inputs[0]) == 4:
        
        h= controller.requerimiento3(catalog)
        print (h)


    elif int(inputs[0]) == 6:
        
        h= controller.req_5(catalog)
        print (h)

    elif int(inputs[0]) == 7:
       # for i in lt.iterator(mp.keySet(catalog["MapAirports"])): 
           # print(i)
        print(catalog["MapAirports"])
    else:
        sys.exit(0)
sys.exit(0)
