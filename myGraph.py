class Graph:
    # class variable, all methods can access it and intances
    quantityNos = 0;

    # Constructor method
    def __init__(self):
        # instance variables
        self.graphNos = {}  # cada instância tem seu grafo

    def insert_nos_graph(self, no):  # method, self parameter is a reference to the current object
        self.graphNos[no] = {}
        self.quantityNos = self.quantityNos + 1

    def insert_nos_adj(self, no, adjacente, value):
        self.graphNos[no][adjacente] = value

    def algorithm_dijkstra_smaller_path(self):
      print(2)

    # method to return a custom string it's equal to toString in java
    def __str__(self):
        return str(self.graphNos)


############################# Main #################################
graph = Graph()

while True:
    line = input().strip()  # .strip() remove spaces in the beggining and end of the string " Hello world " ---> "Hello world"
    # se ler linha vazia, para de ler
    if line == "":
        break

    partes = line.split(maxsplit=1)  # recebe a linha A " independe do números de espaços, quebra sempre em duas linhas"  A 50 --> ['A', '50'] ou A -> ['A']
    if(len(partes) ==1):
      actual = partes[0]
      graph.insert_nos_graph(actual)
    else:
      # divide a linha atráves do delimitador dos espaços
      try:
            adjacente = partes[0].strip()  # adjacentes do nó
            value = float(partes[1].strip())  # pesos dos adj
            print(adjacente)
            print(value)
            graph.insert_nos_adj(actual, adjacente, value)



      except ValueError:
          print("formato inválido")

print(graph)  # isso automaticamente chama a função __str__
