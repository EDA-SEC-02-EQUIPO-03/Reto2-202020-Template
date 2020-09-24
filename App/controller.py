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

import config as cf
from App import model
import csv
from time import process_time


"""
El controlador se encarga de mediar entre la vista y el modelo.
Existen algunas operaciones en las que se necesita invocar
el modelo varias veces o integrar varias de las respuestas
del modelo en una sola respuesta. Esta responsabilidad
recae sobre el controlador.
"""

# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________

def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    # catalog es utilizado para interactuar con el modelo
    return model.newCatalog()

# __________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________

def loadMovies(catalog, booksfile, castingfile):
    """
    Carga cada una de las lineas del archivo de libros.
    - Se agrega cada libro al catalogo de libros
    - Por cada libro se encuentran sus autores y por cada
      autor, se crea una lista con sus libros
    """
    t1_start = process_time()
    booksfile1 =cf.data_dir + booksfile 
    booksfile2 = cf.data_dir + castingfile
    input_file = csv.DictReader(open(booksfile1,encoding='utf-8-sig'))
    input_file2 = csv.DictReader(open(booksfile2,encoding='utf-8-sig'))
    j=1 

    for movie in input_file:
        catalog=model.add_solo_movie(catalog,movie)
    lst=catalog['movies'] 
    for casting in input_file2:
        if casting["id"] == model.getmovie(lst,j)["id"]:
                for column in casting:
                    if column != "id":
                        model.getmovie(lst,j)[column]=casting[column]
        j+=1
        
    for full_movie in lst['elements']:
        model.addMovie_content(catalog,full_movie)
  
    t1_stop = process_time()    
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return catalog
 
def loadData(catalog, detailsfile, castingfile):
    """
    Carga los datos de los archivos en el modelo
    """
    
    catalog=loadMovies(catalog, detailsfile, castingfile)
    return catalog

def getMoviesByCompany(catalog,company_name):
    return model.getMoviesByCompany(catalog,company_name)

def getMoviesByGenre(catalog, genre_name):
    return model.getMoviesByGenre(catalog, genre_name)

def getMoviesByPay(catalog, Pay_name):
    return model.getMoviesByPays(catalog, Pay_name)

def getlastmovie(lst):
    return model.getlastmovie(lst)

def getmovie(lst,pos):
    return model.getmovie(lst, pos)
    
def size(lst):
    return model.size(lst)
def conocer_un_director(criteria,catalog):
    return model.conocer_a_un_director(criteria,catalog)

# ___________________________________________________
#  Funciones de Estetica
# ___________________________________________________

