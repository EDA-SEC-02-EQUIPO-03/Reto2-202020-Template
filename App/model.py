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
from time import process_time 
"""
En este archivo definimos los TADs que vamos a usar,
es decir contiene los modelos con los datos en memoria

"""

# -----------------------------------------------------
# API del TAD Catalogo de Peliculas
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
    t1_start = process_time()
    catalog = {'movies': None,
               'studios': None,
               'Directores': None,
               'Actores': None,
               'Generos': None,
               'Pais': None}
    #'CHAINING' 'PROBING'
    catalog['movies'] = lt.newList('ARRAY_LIST', compareMovieIds)
    catalog['studios'] = mp.newMap(10000,
                                   maptype='CHAINING',
                                   loadfactor=0.4,
                                   comparefunction=compareStudiosByName)
    catalog['Directores'] = mp.newMap(10000,
                                   maptype='CHAINING',
                                   loadfactor=2,
                                   comparefunction=compareAuthorsByName)
    catalog['Actores'] = mp.newMap(100000,
                                maptype='CHAINING',
                                loadfactor=2,
                                comparefunction=compareTagNames)
    catalog['Generos'] = mp.newMap(10000,
                                  maptype='CHAINING',
                                  loadfactor=0.7,
                                  comparefunction=compareGenresbyName)
    catalog['Pais'] = mp.newMap(1000,
                                 maptype='CHAINING',
                                 loadfactor=2,
                                 comparefunction=compareMapYear)
    t1_stop = process_time() 
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return catalog

# Funciones para agregar informacion al catalogo

def add_solo_movie(catalog, movie):
    lt.addLast(catalog['movies'], movie)
    return catalog

def addMovie_content(catalog, movie):
    """
    Esta funcion adiciona un libro a la lista de libros,
    adicionalmente lo guarda en un Map usando como llave su Id.
    Finalmente crea una entrada en el Map de años, para indicar que este
    libro fue publicaco en ese año.
    """
    
    studioname=movie['production_companies']
    addMovieStudio(catalog, studioname, movie)

    Payname=movie['production_countries']
    addMoviePay(catalog, Payname, movie)

    directo=movie['director_name']
    addMovieDirector(directo,catalog,movie)

    genres=movie['genres'].split('|')
    for genre in genres:
        addMovieGenre(catalog, genre, movie)

    actorname1=movie['actor1_name']
    actorname2=movie['actor2_name']
    actorname3=movie['actor3_name']
    actorname4=movie['actor4_name']
    actorname5=movie['actor5_name']
    addMovieActor(catalog,actorname1,movie)
    addMovieActor(catalog,actorname2,movie)
    addMovieActor(catalog,actorname3,movie)
    addMovieActor(catalog,actorname4,movie)
    addMovieActor(catalog,actorname5,movie)
    return catalog


def newDirector(name):
    direc= {'name': "","movie": None, "average_rating":0}
    direc['name']=name
    direc['movie']= lt.newList('ARRAY_LIST', compareAuthorsByName)
    return direc

def newStudio(name):
    """
    Crea una nueva estructura para modelar los libros de un autor
    y su promedio de ratings
    """
    studio = {'name': "", "movie": None,  "average_rating": 0}
    studio['name'] = name
    studio['movie'] = lt.newList('ARRAY_LIST', compareStudiosByName)
    return studio

def newGenre(name):
    """
    Crea una nueva estructura para modelar los libros de un autor
    y su promedio de ratings
    """
    genre = {'name': "", "movie": None,  "average_rating":0}
    genre['name'] = name
    genre['movie'] = lt.newList('ARRAY_LIST', compareGenresbyName)
    
    return genre

def newPay(name):
    """
    Crea una nueva estructura para modelar los libros de un autor
    y su promedio de ratings
    """
    Pay = {'name': "", "movie": None,  "average_rating":0}
    Pay['name'] = name
    Pay['movie'] = lt.newList('ARRAY_LIST', comparePaysbyName)
    
    return Pay

def newActor(name):
    actor={'name': "", "movie": None,"number_movies":0 , "average_rating": 0}
    actor['name'] = name
    actor['movie'] = lt.newList('ARRAY_LIST',compareActorsByName)
    return actor

def addMovieStudio(catalog, studioname, movie):
    """
    Esta función adiciona un libro a la lista de libros publicados
    por un autor.
    Cuando se adiciona el libro se actualiza el promedio de dicho autor
    """
    studios = catalog['studios']
    existstudio = mp.contains(studios, studioname)
    if existstudio:
        entry = mp.get(studios, studioname)
        studio = me.getValue(entry)
    else:
        studio = newStudio(studioname)
        mp.put(studios, studioname, studio)
    lt.addLast(studio['movie'], movie)

    studioavg = studio['average_rating']
    movieavg = movie['vote_average']
    if (studioavg == 0.0):
        studio['average_rating'] = float(movieavg)
    else:
        studio['average_rating'] = (studioavg + float(movieavg)) / 2

def addMovieDirector(criteria,catalog,movie):

    director= catalog['Directores']
    existgenre = mp.contains(director, criteria)
    if existgenre:
        entry = mp.get(director, criteria)
        dire = me.getValue(entry)
    else:
        dire = newDirector(criteria)
        mp.put(director, criteria, dire)
    lt.addLast(dire['movie'], movie)

    direavg= dire['average_rating']
    movieavg = movie['vote_average']
    if (direavg== 0):
            dire['average_rating'] = float(movieavg)
    else:
            dire['average_rating'] = (direavg + float(movieavg)) / 2
    return catalog

def addMovieGenre(catalog, genrename, movie):
    """
    Esta función adiciona un libro a la lista de libros publicados
    por un autor.
    Cuando se adiciona el libro se actualiza el promedio de dicho autor
    """
    genres = catalog['Generos']
    existgenre = mp.contains(genres, genrename)
    if existgenre:
        entry = mp.get(genres, genrename)
        genre = me.getValue(entry)
    else:
        genre = newGenre(genrename)
        mp.put(genres, genrename, genre)
    lt.addLast(genre['movie'], movie)

    genreavg = genre['average_rating']
    movieavg = movie['vote_count']
    if (genreavg == 0.0):
        genre['average_rating'] = float(movieavg)
    else:
        genre['average_rating'] = (genreavg + float(movieavg)) / 2
    return catalog

def addMovieActor(catalog, actorname, movie):

    actors=catalog['Actores']
    existactor=mp.contains(actors,actorname)
    if existactor:
        entry = mp.get(actors,actorname)
        Actor= me.getValue(entry)
    else:
        Actor=newActor(actorname)
        mp.put(actors,actorname,Actor)
    lt.addLast(Actor['movie'],movie)

    actoravg = Actor['average_rating']
    movieavg = movie['vote_average']
    numbermov= Actor['number_movies']
    if (actoravg == 0.0):
        Actor['average_rating'] = float(movieavg)
    else:
        Actor['average_rating'] = ((actoravg*numbermov) + float(movieavg)) / (numbermov+1)
    Actor['number_movies']+=1


def addMoviePay(catalog, Payname, movie):
    """
    Esta función adiciona un libro a la lista de libros publicados
    por un autor.
    Cuando se adiciona el libro se actualiza el promedio de dicho autor
    """
    Pays = catalog['Pais']
    existpay = mp.contains(Pays, Payname)
    if existpay:
        entry = mp.get(Pays, Payname)
        pay = me.getValue(entry)
    else:
        pay = newPay(Payname)
        mp.put(Pays, Payname, pay)
    lt.addLast(pay['movie'], movie)

    Payavg = pay['average_rating']
    movieavg = movie['vote_count']
    if (Payavg == 0.0):
        pay['average_rating'] = float(movieavg)
    else:
        pay['average_rating'] = (Payavg + float(movieavg)) / 2

# ==============================
# Funciones de consulta
# ==============================
def getMoviesByCompany(catalog,company_name):
    movie=mp.get(catalog['studios'], company_name)
    if movie:
        return me.getValue(movie)
    return None

def getMoviesByGenre(catalog,genre_name):
    movie=mp.get(catalog['Generos'], genre_name)
    if movie:
        return me.getValue(movie)
    return None

def getMoviesByActor(catalog,actor_name):
    movie=mp.get(catalog['Actores'], company_name)
    if movie:
        return me.getValue(movie)
    return None

def getMoviesByPays(catalog,Pay_name):
    movie=mp.get(catalog['Pais'], Pay_name)
    if movie:
        return me.getValue(movie)
    return None

def getKey(mapa,key):
    return mp.get(mapa,key)

def size(lst):
    return lt.size(lst)

def getMoviesByCompany(catalog,company_name):
    movie=mp.get(catalog['studios'], company_name)
    if movie:
        return me.getValue(movie)

def addLast(lst, element):
    return lt.addLast(lst, element)

def getMoviesByActor(catalog,actor_name):
    movie=mp.get(catalog['Actores'], actor_name)
    if movie:
        return me.getValue(movie)
    
def getlastmovie(lst):
    movie=lt.lastElement(lst)
    return movie

def getmovie(lst,pos):
    return lt.getElement(lst, pos)

def getMoviesByDirector(catalog,director):
    movie=mp.get(catalog['Directores'], director)
    if movie:
        return me.getValue(movie)
    return None

def insertelement(lst, element, pos):
    return lt.insertElement(lst, element, pos)

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

def compareStudiosByName(keyname, studio):
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

def compareActorsByName(keyname, actor):
    """
    Compara dos nombres de autor. El primero es una cadena
    y el segundo un entry de un map
    """
    actorentry = me.getKey(actor)
    if (keyname == actorentry):
        return 0
    elif (keyname > actorentry):
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

def compareGenresbyName(keyname, genre):
    genreentry = me.getKey(genre)
    if (keyname == genreentry):
        return 0
    elif (keyname > genreentry):
        return 1
    else:
        return -1

def compareMapYear(id, tag):
    tagentry = me.getKey(tag)
    if (id == tagentry):
        return 0
    elif (id > tagentry):
        return 1
    else:
        return 0

def comparePaysbyName(keyname, Pay):
    Payentry = me.getKey(Pay)
    if (keyname == Payentry):
        return 0
    elif (keyname > Payentry):
        return 1
    else:
        return -1

def compareDirectorsByName(keyname, director):
    """
    Compara dos nombres de autor. El primero es una cadena
    y el segundo un entry de un map
    """
    direentry = me.getKey(director)
    if (keyname == direentry):
        return 0
    elif (keyname > direentry):
        return 1
    else:
        return -1


# Funciones para agregar informacion al catalogo





