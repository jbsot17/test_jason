
#* importamos la libreria para poder conectanos 
from openpyxl import Workbook, load_workbook
import requests
from json import dumps

sheet = r'C:\Users\jbsot\Documents\Curso Python\Ejercicios\jholder.xlsx'

web = requests.get('https://jsonplaceholder.typicode.com/users')

data = web.json() #* le doy formato json
n_data = dumps(data, indent= 4)

def crear_libro(): #! create
    libro = Workbook() #! creamos el archivo de excel 
    hoja = libro.active #! activamos una hoja del archivo 
    hoja.title = 'JsonHolder' #! damos nombre a la hoja 
    encabezado = ['id', 'name', 'username', 'email', 'address', 'phone', 'website', 'company'] #! pasamos una lista para el encabezado 
    hoja.append(encabezado) #! para cargar el encabezado debemos hacer un append 
    libro.save(filename= sheet) #! le indicamos la ruta
    #! el nombre y la extension del archivo, por ultimo guardamos 
    libro.close() #! cerramos elñ archivo 


def agregar_datos(): #! update
    libro = load_workbook(filename= sheet)
    hoja = libro['JsonHolder']  #* se puede indicar de igual forma como libro.active
    
    hoja.append(libro)
    libro.save(filename= sheet)
    libro.close()









#### de manera local #####

# TODO: git tiene tres estados working - staging - repository 

#* git init "nombre repositorio"

#* git clone #trae un repositorio externo 

#* git add "nombre del archivo" # agrega archivo para el commit 

#* git add . #agrega todos los archivos que tengamos en el repositorio 

#* git commit -m "comentario obligatorio"

#* git status #muestra como se encuentra el status de los archivos dentro del repo 

#* git log --oneline # me muestra los log del archivo. para poder volver a un commit anterior. 

#* git checkout 'id' # volvemos a una rama especifica del reositorio 

#* git master # regresamos a la ultima modificacion realizada en el rerpositorio 

#print(data[0]['id'])


#for keys in data:
#   for valor in keys:
        


