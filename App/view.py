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
    ruta_casting="Data/themoviesdb/MoviesCastingRaw-small.csv" 
    ruta_details="Data/themoviesdb/SmallMoviesDetailsCleaned.csv"
    ar1=co.loadcsvfile(ruta_casting)
    ar2=co.loadcsvfile(ruta_details)
    print("El número de películas cargadas",len(ar2))
    print("Información de la primera y ultima pelicula:")
    print("La primera pelicula se llama ",0," y tiene como fecha de estreno\n",0,
          ". Su promedio de votación es de",0,", el numero de votos que obtuvo fue \n",0,
          " y el idioma de la pelicula es el ",0,".")
    print("La segunda pelicula se llama ",0," y tiene como fecha de estreno\n",0,
          ". Su promedio de votación es de",0,", el numero de votos que obtuvo fue \n",0,
          " y el idioma de la pelicula es el ",0,".")
# ___________________________________________________
#  Funciones para imprimir la inforamación de
#  respuesta.  La vista solo interactua con
#  el controlador.
# ___________________________________________________
 
def ejecutar_Descubrir_productoras_de_cine():

    return 0 
def ejecutar_Conocer_a_un_director():

    return 0
def ejecutar_Conocer_a_un_actor():

    return 0

def ejecutar_Entender_un_género_cinematográfico():
    return 0

def ejecutar_Encontrar_películas_por_país():
    return 0

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