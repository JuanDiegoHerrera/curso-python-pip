import read_csv
import util
import charts 

paises= read_csv.read_csv("./app/data.csv")


# lo q hay q hacer es conseguir en nombre del pais y tambien el word population percentaje

def word_pop_percent_by_country(paises):
  nombre_paises=[]
  w_porcent= []
  for pais in paises: # aca ya entre en la lista
    
    nombre_paises.append(pais["Country/Territory"])
    w_porcent.append(pais["World Population Percentage"])
  return   nombre_paises, w_porcent
   
     # aca tengo q entrar y recorrer los dict
 # print(nombre_paises)
 # print(w_porcent)
''''
   if pais.keys()== "Country/Territory":
      nombre_paises+= pais.values()
    if pais.keys()== "Word Population Porcentage":
      wporcent+= pais[""]
'''
#resultado= { country: population for (country,population) in population_2.items() if population> 70} #buscar en los dicts 

countrys_names, w_percent= word_pop_percent_by_country(paises)
print(countrys_names)
print(w_percent)
#ahora

charts.generate_pie_chart(countrys_names, w_percent)














