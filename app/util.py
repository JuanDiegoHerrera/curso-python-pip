import re
# la info va a venir de esta forma
paises=[
  {"country": "colombia",
   "Population1": 500, "Population2":550,  "Population3": 600
    }
]
print(paises[0])
dictpaises= paises[0]               # lo q sabemos es q cunado ponemos data[0] te va a tirar el dict 
llaves= dictpaises.keys()    # a partir de ese dict lo que quiero es buscar con un condicional las llaves
print(llaves) 
items= dictpaises.items() 
print("*****\n",items)


#buscapalabra= {año:poblacion for (año,poblacion)in dictpaises.items() if re.search("Population",dictpaises.items())}
#print(buscapalabra)     # no dio resultado


#clientela_10= {cliente:descuento for (cliente, descuento) in diccionario_descuentos.items() if descuento<30}

#print(clientela_10)
#[k for k, v in dict.items() if  > 60]

def get_population(data):
  dictdedato= data[0]
  print(dictdedato)

  a2022={año:poblacion for (año,poblacion) in dictdedato.items() if año in "2022 Population"}
  a2020={año:poblacion for (año,poblacion) in dictdedato.items() if año in "2020 Population"}
  a2015={año:poblacion for (año,poblacion) in dictdedato.items() if año in "2015 Population"}
  a2010={año:poblacion for (año,poblacion) in dictdedato.items() if año in "2010 Population"}
  a2000={año:poblacion for (año,poblacion) in dictdedato.items() if año in "2000 Population"}
  a1990={año:poblacion for (año,poblacion) in dictdedato.items() if año in "1990 Population"}
  a1980={año:poblacion for (año,poblacion) in dictdedato.items() if año in "1980 Population"}
  a1970={año:poblacion for (año,poblacion) in dictdedato.items() if año in "1970 Population"}
  



  

  
  #keys=  dictdedato[lol dor lol, v dictdedato.items() if "Population" in dictdedato]
  
  return a2022, a2020, a2015, a2010, a2000, a1990, a1980, a1970

  






  
#declaro variable
popu=get_population(paises)
print("===", popu)
        
a= "hola"


def population_by_country(data,country):
  result= list(filter(lambda item: item["country"]==country, data))
  return result


























