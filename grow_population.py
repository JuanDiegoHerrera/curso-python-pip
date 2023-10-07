import read_csv


if __name__=="__main__":
  data= read_csv.read_csv("./app/data.csv")
  tipo_de_dato= type(data)
  print(tipo_de_dato)
  pais= input("intro un pais: ")
  argent= list(filter(lambda country :country["Country/Territory"]== pais.title(), data))
  #arg=next( item for item in data if item["Country/Territory"]=="Argentina")
  print(argent)
  def grow_population(argent):
    list(filter (lambda grow: grow[int, argent ])
    populationevol=  { popuevol: popu for (popuevol, popu) in argent.items() if "Population" in argent.keys()}
  print(grow_population(argent))
  print(grow_population)



#resultado= { country: population for (country,population) in population_2.items() if population> 70}
#print(resultado,"\n========") # solo tenes var exterioir a pupulation_2


