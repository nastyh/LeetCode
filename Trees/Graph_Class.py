from collections import defaultdict
class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.adj_list = defaultdict(list)

        for n in nodes:
            self.adj_list[n] = []

    def print_graph(self):
        # return self.adj_list.items()
        for n in self.nodes:
            print(n, ' contains ', self.adj_list[n])

    def add_vertex(self, value):
        self.adj_list[value] = []

    def create_connections(self, n1, n2):
        if not n1 in self.adj_list:
            print(f'Value {n1} not in Graph')
        if not n2 in self.adj_list:
            print(f'Value {n2} not in Graph')
        self.adj_list[n1].append(n2)
        self.adj_list[n2].append(n1)

class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self, nbr, weight = 0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connected to ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo


if __name__ == '__main__':
    g = Graph(['A', 'B', 'C', 'D', 'E'])
    g.add_vertex('F')
    g.create_connections('A', 'E')
    g.print_graph()
    # v = Vertex('A')
    # v.addNeighbor('B')
    # v.getConnections()
    # print(v)
