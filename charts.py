import matplotlib.pyplot as plt 



#grafico= "./app/data.csv".pyplot(kind= "bar")
# casi me  sale

def generate_bar_chart(labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.show()


def generate_pie_chart(labels,values):
  fig,ax= plt.subplots()
  ax.pie(values, labels= labels)# esta igualdad es por una regla de la libreria
  ax.axis("equal")
  plt.show()







if __name__ =="__main__":
  
  labels=["a","b","c"]
  values= [10,40,800]
  #generate_bar_chart(labels,values)
  generate_pie_chart(labels,values)
  
