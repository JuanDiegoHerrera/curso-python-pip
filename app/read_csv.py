import csv


''''
el delimiter es el simbolo por el cual estan separados los datos, o la forma en  vienen separados los datos, los csv en general es por comas'''



def read_csv(path):
  with open(path,"r") as csvfile:
    reader= csv.reader(csvfile, delimiter= ",")
    header= next(reader) #porque reader es un iterable
    data=[]
    for row in reader: 
      iterable= zip(header, row) # une header y row wn un array de tuplas 1ero col y despues row
      
      
      
      country_dict= {key: value for key, value in iterable}
      data.append(country_dict)
    return data

if __name__== "__main__":
  data= read_csv("./app/data.csv") # queda como un array de datos

# hay q trasform en un diccionario
  print(data[0])
  





