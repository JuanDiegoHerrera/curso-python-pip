import main


print(main.data) # volvimos a sacar data de run

#print("example=> ",main.data), esto se remplazo por la funcion run

# no solo te va a imprimir data sino al ejecutar example.py tambien te va a ejecutar main.py
# pero eso esta mal hay q modularizarlo, una forma de hacerlo es volverlo una fucion explicita, entonces no se va a ejecutar simplemente por hacer la importacion

main.run()


''''
ahora si queres ejecutarlo como un scrip, osea en la terminal

Como se puede hacer para esto:
se quiere poder ejecutar main desde la consola, si la necesidad de un tercer archivo
para resolverlo es usar:

if __name__:
  run()

# esto esta en el archivo main al final

esto lo haces para q no se pueda ejecutar la ejecucion de main a partir de example u otro archivo dif a main'''