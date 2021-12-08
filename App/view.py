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
import time
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
        controller.crearNoDirigido(catalog)
        print(gr.numEdges(catalog["RouteGraphNoD"]))
        
        print("*********************** Digrafo info ****************************")
        print("El numero de arcos del digrafo es " + str(gr.numEdges(catalog["RouteGraphD"])))
        print("El numero de aeropuertos cargados es " + str(mp.size(catalog["MapAirportsIATA"])))

        print("****************************** Grafo info **************************")
        
        print("El numero de arcos del grafo es " + str(gr.numEdges(catalog["RouteGraphNoD"])))
        print("El numero de aeropuertos cargados es " + str(mp.size(catalog["MapAirportsIATA"])))

        print("Datos cargados correctamente")
    elif int(inputs[0]) == 2:
       print("***************** Requerimiento 1 ****************************")
       print("Numero de aeropuertos en la red " + str(mp.size(catalog["MapAirportsIATA"])))
       print("Numero de aeropuertos conectados " + str(lt.size(gr.vertices(catalog["RouteGraphDAirlines"]))))
       print("***************** Aeropuertos con más conexiones ****************************")
       req = controller.requerimiento1(catalog)

       for i in lt.iterator(req): 
           
           variable=mp.get(catalog["MapAirportsIATA"],i["key"])
           variable1=variable["value"]
           print({"Nombre ":variable1["Name"]," Ciudad ":variable1["City"], "País": variable1["Country"], "IATA":variable1["IATA"], "Conexiones":i["value"],"Salidas":gr.outdegree(catalog["RouteGraphDAirlines"],i["key"]), "Entradas":gr.indegree(catalog["RouteGraphDAirlines"],i["key"])})
        
    elif int(inputs[0]) == 3:
        IATA1=input("Introduce codigo IATA 1: ")
        IATA2=input("Introduce codigo IATA 2: ")
        h= controller.requerimiento2(catalog,IATA1,IATA2)
        print("Hay {} SCC en el grafo.".format(lt.getElement(h,1)))
        air1=mp.get(catalog["MapAirportsIATA"],IATA1)
        air1=air1["value"]
        air2=mp.get(catalog["MapAirportsIATA"],IATA2)
        air2=air2["value"]
        print({"Nombre ":air1["Name"]," Ciudad ":air1["City"], "País": air1["Country"], "IATA":air1["IATA"]})
        print({"Nombre ":air2["Name"]," Ciudad ":air2["City"], "País": air2["Country"], "IATA":air2["IATA"]})
        print("RESP: {}".format(lt.getElement(h,2)))


    elif int(inputs[0]) == 4:

        """for i in lt.iterator(mp.keySet(catalog["City"])):
            print(i)
        Pais1=input("Introduce el indicativo del país al que corresponde la ciudad de salida: ")
        Ciudad1=input("Introduce el nombre de la ciudad de salida: ")
        Region1=input("Introduce el nombre de la región la cual la ciudad de salida pertenece")
        Pais2=input("Introduce el indicativo del país al que corresponde la ciudad de llegada: ")
        Ciudad2=input("Introduce el nombre de la ciudad de llegada: ")
        Region2=input("Introduce el nombre de la región la cual la ciudad de llegada pertenece: ")
        Ciudad1 = Ciudad1+Pais1+Region1
        Ciudad2=Ciudad2+Pais2+Region2"""
        Ciudad1="Saint-RaymondCAQuebec"
        Ciudad2="MoosburgDEBavaria"
       # print(mp.get(catalog["City"],"JiyekCNXinjiang"))
        h= controller.requerimiento3(catalog,Ciudad1,Ciudad2)
        for i in lt.iterator(h):
            print(i)
        #for i in lt.iterator(h):
        
        #stop_time = time.process_time()
        #elapsed_time_mseg = (stop_time - start_time)*1000
       # print(elapsed_time_mseg)

        
    elif int(inputs[0]) == 6:
        
        h= controller.req4(catalog)
        print (h)

    elif int(inputs[0]) == 7:
       # for i in lt.iterator(mp.keySet(catalog["MapAirports"])): 
           # print(i)
        print("Hola")

    elif int(inputs[0]) == 8:
           print(controller.req_5(catalog))
    else:
        sys.exit(0)
sys.exit(0)
