
"""
El controlador se encarga de mediar entre la vista y el modelo.
Existen algunas operaciones en las que se necesita invocar
el modelo varias veces o integrar varias de las respuestas
del modelo en una sola respuesta. Esta responsabilidad
recae sobre el controlador.
"""
import config as cf 
from App import model
import csv

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

def loadMovies(catalog, booksfile):
    """
    Carga cada una de las lineas del archivo de libros.
    - Se agrega cada libro al catalogo de libros
    - Por cada libro se encuentran sus autores y por cada
      autor, se crea una lista con sus libros
    """
  
    booksfile1 = cf.data_dir + booksfile
    input_file = csv.DictReader(open(booksfile1,encoding='utf-8-sig'))
    for movie in input_file:
        model.addMovie(catalog, movie)
    return catalog

def loadData(catalog, detailsfile, castingfile):
    """
    Carga los datos de los archivos en el modelo
    """
    
    catalog=loadMovies(catalog, detailsfile)
    return catalog

def getMoviesByCompany(catalog,company_name):
    return model.getMoviesByCompany(catalog,company_name)

def getlastmovie(lst):
    return model.getlastmovie(lst)

def getmovie(lst,pos):
    return model.getmovie(lst, pos)
    
def size(lst):
    return model.size(lst)

# ___________________________________________________
#  Funciones de Estetica
# ___________________________________________________
