from heapq import  heappush, heappop

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
        if adjacente not in self.graphNos:
            self.insert_nos_graph(adjacente)
        self.graphNos[no][adjacente] = value

    # Algorithm Dijkstra
    def algorithm_dijkstra_smaller_path(self, origem):

        ## Inicialização dos vértices
        dist = {no: float('inf') for no in self.graphNos} # dicionário que guarda a menor distância entre o vértice de origem e os demais
        dist[origem] = 0;
        previous = {no: None for no in self.graphNos} # dicionário que guarda o vértice anterior no menor caminho encontrado
        fila = [] ## Fila que ira guardar (distância, vértice)
        heappush(fila, (0, origem)) ## inicia a fila com a origem e distância zero

        # loop principal do algorithm dijkstra
        while len(fila) != 0:
            distAtaul, verticeAtual = heappop(fila)

            if distAtaul != dist[verticeAtual]:
                continue

            #relaxamento dos vértices
            for vizinho, peso in self.graphNos[verticeAtual].items():
                newDistance = dist[verticeAtual] + peso

                if newDistance < dist[vizinho]:
                    dist[vizinho] = newDistance
                    previous[vizinho] = verticeAtual
                    heappush(fila, (newDistance, vizinho))

        self.distancias = dist
        self.previous = previous
        self.origem = verticeAtual


    def status(self):
        for i in self.nosList:
            print(i)
    # method to return a custom string it's equal to toString in java
    def __str__(self):
        if not (hasattr(self, 'distancias')):
            return "Error"
        result = ""
        for no, distance in self.distancias.items():
            if no == self.origem:
                continue
            result += f"{no}: {distance}\n"
        return result


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
            graph.insert_nos_adj(actual, adjacente, value)



      except ValueError:
          print("formato inválido")


for i in graph.graphNos.keys():
    graph.algorithm_dijkstra_smaller_path(i)
    print(f"Origem: {i}")
    print(graph)
    print("\n")

print(graph)  # isso automaticamente chama a função __str__
