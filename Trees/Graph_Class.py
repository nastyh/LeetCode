from collections import defaultdict
class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.adj_list = {}
        for n in nodes:
            self.adj_list[n] = []


    def add_vertex(self, value):
        self.adj_list[value] = []


    def print_graph(self):
        # return self.adj_list.items()
        for n in self.nodes:
            print(n, ' contains ', self.adj_list[n])


    def create_connections(self, n1, n2):
        if not n1 in self.adj_list:
            print(f'Value {n1} is not in Graph')
        if not n2 in self.adj_list:
            print(f'Value {n2} is not in Graph')
        if n2 not in self.adj_list[n1]:
            self.adj_list[n1].append(n2)
        else:
            print(f'Vertex {n2} is already connected to {n1}')
        if n1 not in self.adj_list[n2]:
            self.adj_list[n2].append(n1)
        else:
            print(f'Vertex {n1} is already connected to {n2}')


    def degree(self, node):  # return the number of edges that a given node has
        return len(self.adj_list[node])


class Vertex:   # Not really necessary here
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
    all_edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('C', 'E'), ('D', 'E')]
    for e in all_edges:
        g.create_connections(e[0], e[1])
    # g.create_connections('E', 'D')
    # g.create_connections('E', 'C')
    g.print_graph()
    print(g.degree('D'))
    # v = Vertex('A')
    # v.addNeighbor('B')
    # v.getConnections()
    # print(v)
