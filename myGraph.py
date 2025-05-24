class Graph:

  #class variable, all methods can access it and intances 
  quantityNos = 0;
  
  # Constructor method
  def __init__(self):
    #instance variables
    self.graphNos = {} # cada instância tem seu grafo 

  def insert_nos_graph(self,no): # method, self parameter is a reference to the current object
    self.graphNos[no] = {}
    self.quantityNos = self.quantityNos + 1
  
  def insert_nos_adj(self, no, adjacente, value):
    self.graphNos[no][adjacente] = value

  #method to return a custom string it's equal to toString in java
  def __str__(self):
   return str(self.graphNos)


############################# Main #################################
graph = Graph()


while True:
  line = input().strip() # .strip() remove spaces in the beggining and end of the string " Hello world " ---> "Hello world"
  # se ler linha vazia, para de ler 
  if line == "":
    break

  if ' ' not in line:
    no = line.strip() # Guarda o nó 
    graph.insert_nos_graph(no)
  else:
    #divide a linha atráves do delimitador dos espaços
    try: 
      partes = line.split() # recebe a linha A 50 --> ['A', '50']
      adjacente = partes[0].strip() # adjacentes do nó 
      value = float(partes[1].strip()) # pesos dos adj 
      graph.insert_nos_adj(no,adjacente, value)
      

      
    except ValueError:
      print("formato inválido")


print(graph) # isso automaticamente chama a função __str__ 