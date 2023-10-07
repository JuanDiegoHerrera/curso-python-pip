# si cambias el nombre de un modulo cambia despues el nombre en el codigo

import util # este es el modulo q cree
#acordate q podes traer la funcion pero le tenes q poner la ref adelante


data= [
    {"country": "colombia",
     "population": 500
    },
    {
      "country": "bolivia",
      "population": 300
    }
  ]

def run():
  keys,values = util.get_population()
  print(keys, values)
  # acordate q cunado queres ejecutar un archivo dentro de una carpeta tens q poner todo
  
  # invoco variable
  print(util.a)
  
  # por eso cualquier archivo en python se considera un modulo
  
  
 
  
  
  country= input("poner pais: ")
  result2= util.population_by_country(data,country)
  
  print(result2)





# los midulos se pueden correrer de 2 maneras,una es declarando las funciones, import libria, des´pues libreia.funcion
# la otra forma es hacerlo como scripts que es correr los archivos de forma directa vamos a la terminal, digitamos python y le damos la direccion exacta de nuestro archivo y lo ejecutamos 

# y si queres hacer ñas 2 






# este if le dice al archivo main.py q si es ejecutado desde la terminal ejecute el metodo run, pero si esjecutado desde ptro archivo esto no se va a ejecutar exepto q invoque main.run()   

if __name__=="__main__":
   run() 
