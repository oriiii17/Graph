class Graph:
    def __init__(self):
        self._data = {}
    #constructor

    def addVertex(self, key):
        if key not in self._data:
            self._data[key] = set()
    #menambah vertex

    def vertex(self):
        for key, value in self._data.items():
            print(key, end = ' ')
        print()
    #mencetak seluruh vertex

    def addEdge(self, x, y):
        if x in self._data and y in self._data:
            self._data[x].add(y)
            self._data[y].add(x) #hanya digunakan jika graph tidak berarah
    #menambah edge antara vertex x dan y

    def edge(self):
        listEdge = set()
        for key, value in self._data.items():
            for item in self._data[key]:
                if key+item not in listEdge and item+key not in listEdge:
                    listEdge.add(key+item)
            for item in listEdge:
                print(item, end = ' ')
            print()
    #mencetak seluruh edge yang ada

    def findPath(self, x, y):
        visited = []
        self.dfs(x, y, visited)
    #mencari jalur dari vertex x menuju y

    def dfs(self, node, y, visited):
        visited.append(node)
        if node == y:
            print(visited)
        else:
            for item in self._data[node]:
                if item not in visited:
                    self.dfs(item, y, visited)


graph = Graph()
graph.addVertex('a')
graph.addVertex('b')
graph.addVertex('c')
graph.addVertex('d')
graph.addEdge('a', 'b')
graph.addEdge('a', 'c')
graph.addEdge('a', 'd')
graph.addEdge('b', 'd')
graph.addEdge('c', 'd')
graph.vertex()
graph.edge()