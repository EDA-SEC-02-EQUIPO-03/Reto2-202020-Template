"""
 * Copyright 2020, Departamento de sistemas y Computación
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
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

import sys
import config
from DISClib.ADT import list as lt
from DISClib.DataStructures import listiterator as it
from App import controller as co
assert config


"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones y por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Ruta a los archivos
# ___________________________________________________
def ejecutar_cargar_datos():
    ruta_casting="themoviesdb/AllMoviesCastingRaw.csv"
    #"themoviesdb/AllMoviesCastingRaw.csv"
    #"themoviesdb/MoviesCastingRaw-small.csv" 
    ruta_details="themoviesdb/AllMoviesDetailsCleaned.csv"
    #"themoviesdb/AllMoviesDetailsCleaned.csv"
    #"themoviesdb/SmallMoviesDetailsCleaned.csv"
    catalog=co.initCatalog()
    co.loadData(catalog,ruta_details,ruta_casting)
    return catalog 
#fin
# ___________________________________________________

#  Funciones para imprimir la inforamación de
#  respuesta.  La vista solo interactua con
#  el controlador.
# ___________________________________________________

def ejecutar_getMoviesbyCompany(catalog,company_name):
    movies=co.getMoviesByCompany(catalog,company_name)
    print("Las peliculas de la compañia de producción son: \b")
    for i in range(1,lt.size(movies["movie"])+1):
        print(lt.getElement(movies["movie"],i)['title'],"\b")
        print(lt.getElement(movies["movie"],i)['vote_average'],"\b")
    print('estas tienen una calificación promedio de de',str(movies["average_rating"]) )

def ejecutar_Conocer_a_un_director(criteria,catalog):
    
    counter=co.conocer_un_director(criteria,catalog)
    print("Las peliculas del director ",criteria,"son ",counter[1]," las cuales se nombraran en el siguiente listado: \n")
    for k in  range(1,lt.size(counter[0])+1):
            print(lt.getElement(counter[0],k))
    print("Las anteriores tienen un promedio de votación de: ",counter[2])
    return 0 
def ejecutar_Conocer_a_un_actor():

    return 0

def ejecutar_Entender_un_género_cinematográfico(catalog, genre_name):
    movies=co.getMoviesByGenre(catalog,genre_name)
    print("Las peliculas de la compañia de producción son: \b")
    for i in range(1,lt.size(movies["movie"])+1):
        print(lt.getElement(movies["movie"],i)['title'],"\b",lt.getElement(movies["movie"],i)['vote_count'])
    print('estas tienen una Votacion promedio de',str(movies["vote_count"]) )

def ejecutar_getMoviesbyPay(catalog,Pay_name):
    movies=co.getMoviesByPay(catalog,Pay_name)
    print("Las peliculas de la compañia de producción son: \b")
    for i in range(lt.size(movies["movie"])):
        Elemento=lt.getElement(movies["movie"],i)
        if Elemento['release_date']=="":
            año="No Especificado"
        else:
            año=str(Elemento['release_date'].replace('-','/').split('/')[2])
        print(Elemento['title'],'______',año,'______',Elemento['director_name'])
        print('')
        
    print('estas tienen una calificación promedio de de',str(movies["average_rating"]))

# ___________________________________________________
#  Menu principal
# ___________________________________________________
def printMenu():
    """
    Imprime el menu de opciones
    """
    print("\nBienvenido")
    print("1- Cargar Datos")
    print("2-  Descubrir productoras de cine")
    print("3- Conocer un director")
    print("4- Conocer un actor")
    print("5- Entender un género cinematográfico")
    print("6- Encontrar películas por país")
    print("0- Salir")
    
def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados

    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
    Args: None
    Return: None 
    """

    while True:
        printMenu() #imprimir el menu de opciones en consola
        inputs =input('Seleccione una opción para continuar\n') #leer opción ingresada
        if len(inputs)>0:

            if int(inputs[0])==1: #opcion 1
                'Cargando datos'
                catalog = ejecutar_cargar_datos()

            elif int(inputs[0])==2: #opcion 2
                company_name= input("Escriba el nombre de la compañia que quiere conocer ")
                ejecutar_getMoviesbyCompany(catalog,company_name)
                
            elif int(inputs[0])==3: #opcion 3
                criteria=input("Nombre del director que desea conocer: \n")
                ejecutar_Conocer_a_un_director(criteria,catalog)
            elif int(inputs[0])==4: #opcion 4
                print("0")
            elif int(inputs[0])==5: #opcion 5
                genre_name=input("Escriba el nombre del Genero que quiere conocer ")
                ejecutar_Entender_un_género_cinematográfico(catalog, genre_name)
            
            elif int(inputs[0])==6: #opcion 6
                Pay_name=input("Escriba el nombre del Pais que quiere conocer ")
                ejecutar_getMoviesbyPay(catalog,Pay_name)
              
            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)
                
if __name__ == "__main__":
    main()