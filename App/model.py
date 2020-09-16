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
import config
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert config

"""
En este archivo definimos los TADs que vamos a usar,
es decir contiene los modelos con los datos en memoria

"""

# -----------------------------------------------------
# API del TAD Catalogo de Libros
# -----------------------------------------------------
def movieList(datastructure,cmpfunction):
    lst=lt.newList(datastructure,cmpfunction)
    return lst
    
def newCatalog():
    """ Inicializa el catálogo de libros

    Crea una lista vacia para guardar todos los libros

    Se crean indices (Maps) por los siguientes criterios:
    Autores
    ID libros
    Tags
    Año de publicacion

    Retorna el catalogo inicializado.
    """
    catalog = {'Movies': None,
               'studios': None,
               'Directores': None,
               'Actores': None,
               'Generos': None,
               'Pais': None}

    catalog['movies'] = lt.newList('SINGLE_LINKED', compareMovieIds)
    catalog['studios'] = mp.newMap(200,
                                   maptype='CHAINING',
                                   loadfactor=0.4,
                                   comparefunction=compareAuthorsStudiosByName)
    catalog['Directores'] = mp.newMap(200,
                                   maptype='CHAINING',
                                   loadfactor=0.4,
                                   comparefunction=compareAuthorsByName)
    catalog['Actores'] = mp.newMap(1000,
                                maptype='CHAINING',
                                loadfactor=0.7,
                                comparefunction=compareTagNames)
    catalog['Generos'] = mp.newMap(1000,
                                  maptype='CHAINING',
                                  loadfactor=0.7,
                                  comparefunction=compareTagIds)
    catalog['Pais'] = mp.newMap(500,
                                 maptype='CHAINING',
                                 loadfactor=0.7,
                                 comparefunction=compareMapYear)

    return catalog


# Funciones para agregar informacion al catalogo
def addmovie(lst,movie):
    lt.addLast(lst,movie)

def addMovie(catalog, movie):
    """
    Esta funcion adiciona un libro a la lista de libros,
    adicionalmente lo guarda en un Map usando como llave su Id.
    Finalmente crea una entrada en el Map de años, para indicar que este
    libro fue publicaco en ese año.
    """
    lt.addLast(catalog['movies'], movie)
    
    studioname=movie['production_companies']
 
    addMovieStudio(catalog, studioname,movie)


def newStudio(name):
    """
    Crea una nueva estructura para modelar los libros de un autor
    y su promedio de ratings
    """
    studio = {'name': "", "movie": None,  "average_rating": 0}
    studio['name'] = name
    studio['movie'] = lt.newList('ARRAY_LINKED', compareAuthorsStudiosByName)
    return studio


def addMovieStudio(catalog, studioname, movie):
    """
    Esta función adiciona un libro a la lista de libros publicados
    por un autor.
    Cuando se adiciona el libro se actualiza el promedio de dicho autor
    """
    studios = catalog['studios']
    existauthor = mp.contains(studios, studioname)
    if existauthor:
        entry = mp.get(studios, studioname)
        studio = me.getValue(entry)
    else:
        studio = newStudio(studioname)
        mp.put(studios, studioname, studio)
    lt.addLast(studio['movie'], movie)

    studioavg = studio['average_rating']
    movieavg = movie['vote_average']
    if (studioavg == 0.0):
        studio['average_rating'] = float(studioavg)
    else:
        studio['average_rating'] = (studioavg + float(movieavg)) / 2

# ==============================
# Funciones de consulta
# ==============================
def getMoviesByCompany(catalog,company_name):
    movie=mp.get(catalog['studios'], companyname)
    if movie:
        return me.getValue(movie)
    return None

def getKey(mapa,key):
    return mp.get(mapa,key)

def size(lst):
    return lt.size(lst)
    
def getmovie(lst,pos):
    movie=lt.getElement(lst,pos)
    return movie 
    
def getlastmovie(lst):
    movie=lt.lastElement(lst)
    return movie

# ==============================
# Funciones de Comparacion
# ==============================



def compareMovieIds(id1, id2):
    """
    Compara dos ids de libros
    """
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1


def compareAuthorsStudiosByName(keyname, studio):
    """
    Compara dos nombres de autor. El primero es una cadena
    y el segundo un entry de un map
    """
    studioentry = me.getKey(studio)
    if (keyname == studioentry):
        return 0
    elif (keyname > studioentry):
        return 1
    else:
        return -1


def compareAuthorsByName(keyname, author):
    """
    Compara dos nombres de autor. El primero es una cadena
    y el segundo un entry de un map
    """
    authentry = me.getKey(author)
    if (keyname == authentry):
        return 0
    elif (keyname > authentry):
        return 1
    else:
        return -1


def compareTagNames(name, tag):
    tagentry = me.getKey(tag)
    if (name == tagentry):
        return 0
    elif (name > tagentry):
        return 1
    else:
        return -1


def compareTagIds(id, tag):
    tagentry = me.getKey(tag)
    if (int(id) == int(tagentry)):
        return 0
    elif (int(id) > int(tagentry)):
        return 1
    else:
        return 0


def compareMapYear(id, tag):
    tagentry = me.getKey(tag)
    if (id == tagentry):
        return 0
    elif (id > tagentry):
        return 1
    else:
        return 0


def compareYears(year1, year2):
    if (int(year1) == int(year2)):
        return 0
    elif (int(year1) > int(year2)):
        return 1
    else:
        return 0




# Funciones para agregar informacion al catalogo





