import read_csv
import util
import charts 

paises= read_csv.read_csv("./app/data.csv")
print(paises)

def run(paises): 
  pais= input("intro un pais: ")
  data_pais= list(filter(lambda country :country["Country/Territory"]== pais.title(), paises))
  print(data_pais)

  evol_population= util.get_population(data_pais)
  print(evol_population)
  #dict_evol_pop= evol_population[0]
  labels=[]
  values=[]
  for dicts in evol_population:
    labels+= dicts.keys()
    values+= dicts.values()
    print(labels)
    print(values)
    #labels+= dicts.keys()
    #values+= dicts.values()
  graf_population = charts.generate_bar_chart(labels,values)






run(paises)



''''
 for dicts in evol_population:
    labels+= dicts.keys()
    values+= dicts.values()
    print(labels)
    print(values)

'''









