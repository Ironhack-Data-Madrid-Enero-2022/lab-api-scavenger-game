import json
import requests as req
import os
from dotenv import load_dotenv
token = open ("../token.txt").readlines()[0]
params = {"Authorization": f"token {token}"}
# Vamos a crear una funcion que nos mire los lenguajes en todos los forks de cada lab,
def finding_languages(lab_name, URL_BASE='https://api.github.com/repos/Ironhack-Data-Madrid-Enero-2022', par = params):
    """ This function aims to detect all the languages used in the forks of a certain repo in git hub.
    Inputs: all the inputs should be strings,
    lab_name ----> Name of the repo we want to acces and study; URL_BASE ----------> Should have the following structure:
    https://api.github.com/repos/USERNAME
    par is the headers we need for authentification, it is not always necesary.
    """
    URL = URL_BASE+f'/{lab_name}/forks' # Nos creamos el endpoint para acceder a todos los forks de cada lab
    langs = req.get(URL, headers = par)
    lang_list = list()
    for fork in langs.json():
        if fork['fork'] == True: # Será siempre cierto porque estamos en forks...
            lang_list.append(fork['language']) # Añadimos el lenguaje usado en nuestra lista de languages, podriamos hacer un diccionario y añadir el usuario que lo usa, pero es innecesario para lo que necesitamos
        
    return set(lang_list) # Creamos un set para evitar valores repetidos

# Primo encontramos todos los repos del usuario que estamos estudiando,
URL ='https://api.github.com/users/Ironhack-Data-Madrid-Enero-2022/repos' # Con el endpoint ..+/repos nos salen todas
get_repos_list = req.get(URL, headers = params) # ahora que los tenemos los guardamos en una lista,
lista_repos = [i['name'] for i in get_repos_list.json()]
#print(lista_repos)
resultado = dict() # Crearemos un diccionario vacio para almacenar la info
for lab in lista_repos:
    resultado[lab] = [i for i in finding_languages(lab) if i] # nos quitamos de enchima los None con la list coprehension
resultado_lista =  list(set(j for a in resultado.values() for j in a))
print(resultado_lista)