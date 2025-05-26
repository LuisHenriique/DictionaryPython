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
        self.graphNos[no][adjacente] = value # insere na chave no o dicionario adjacente com seu respectivo valor de peso

    # Algorithm Dijkstra
    def algorithm_dijkstra_smaller_path(self, origem):
        self.origem = origem
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

    # method to return a custom string it's equal to toString in java
    def __str__(self):
        if not (hasattr(self, 'distancias')):
            return "Error"
        result = ""
        for no, distance in self.distancias.items():
            if no == self.origem:
                continue

            # Reconstroi o caminho
            path = []
            actual = no
            while actual is not None:
                if(actual != self.origem):
                    path.append(actual)
                actual = self.previous[actual]
            path.reverse() # revertendo para deixar na ordem

            path_str = " --> ".join(path)
            result += f"{self.origem} para {no}\n	Distancia: {str(distance).replace('.', ',')}\n	Caminho:  --> {path_str}\n"
        result+="---------------------------------------------"
        return result


############################# Main #################################
graph = Graph() # instanciando o objeto Graph

while True:
    try:
        line = input().strip()  # .strip() remove spaces in the beginning and end of the string " Hello world " ---> "Hello world"
    except EOFError:
        break
    # se ler linha vazia, para de ler
    if line == "":
        break

    partes = line.split(maxsplit=1)  # recebe a linha A " independe do números de espaços, quebra sempre em duas linhas"  A 50 --> ['A', '50'] ou A -> ['A']
    if(len(partes) ==1):
      actual = partes[0]
      graph.insert_nos_graph(actual) # insertions this NO like a key

    else:

      try:
            adjacente = partes[0].strip()  # adjacentes do nó
            value = float(partes[1].strip())  # peso da aresta entre o nó antecessor e sucessor
            graph.insert_nos_adj(actual, adjacente, value)



      except ValueError:
          print("formato inválido")


keys = list(graph.graphNos.keys())
for idx, i in enumerate(keys):
    graph.algorithm_dijkstra_smaller_path(i)
    print(graph, end="")

    if idx != len(keys) - 1:
        print()



