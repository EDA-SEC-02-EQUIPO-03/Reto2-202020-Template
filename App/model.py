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
# API del TAD Catalogo de Peliculas
# -----------------------------------------------------
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
    catalog = {'movies': None,
               'companies': None}

    catalog['movies'] = lt.newList('ARRAY_LIST')
    catalog['production_company'] = mp.newMap(500,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=comparemovieIds)

    return catalog


def newCompany(name)
    company = {'name': "", "movies": None,  "average_rating": 0}
    company['name'] = name
    company['movies'] = lt.newList('SINGLE_LINKED', compareid)
    return company
# Funciones para agregar informacion al catalogo

def addmoviecompany(catalog,company_name,movie)
    companies=catalog['companies']
    existcompany= mp.contains(companies,company_name)
    if existcompany:
        entry= mp.get(companies,company_name)
        company=me.getValue(entry)
    else:
        company=newCompany(company_name)
        mp.put(companies,company_name,company)
    lt.addLast(company['movies'],movie)
        
    compavg = company['average_rating']
    movieavg = movie['average_rating']
    n=lt.size(company['movies'])
    if (compavg == 0.0):
        company['average_rating'] = float(movieavg)
    else:
        company['average_rating'] = ((compavg*(n/(n+1)) )+ (float(movieavg)/(n+1))) 


    


# ==============================
# Funciones de consulta
# ==============================
def size(lst):
    return lt.size(lst)
    
def getMoviesByCompany(catalog,company_name):
    movie=mp.get(catalog['company'], companyname)
    if movie:
        return me.getValue(movie)
    return None
    
def getlastmovie(lst):
    movie=lt.lastElement(lst)
    return movie

# ==============================
# Funciones de Comparacion
# ==============================
def compareid(id1, id2):
    """
    Compara dos ids de libros, id es un identificador
    y entry una pareja llave-valor
    """
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1

