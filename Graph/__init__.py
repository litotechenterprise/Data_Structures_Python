


class Graph():
    def __init__(self, undirected = True) -> None:
        self.adjacecy_list = {}
        self.undirected = undirected


    def print_graph(self):
        for v in self.adjacecy_list:
            print(f"{v}: {self.adjacecy_list[v]}")

    def add_vertex(self, vertex: str | int):
        if vertex not in self.adjacecy_list.keys():
            self.adjacecy_list[vertex] = []
            return True
        return False


    def add_edge(self, start: int | str, destination: int | str):
        self.adjacecy_list[start].append(destination)
        
        if self.undirected:
            self.adjacecy_list[destination].append(start)

    def remove_vertex(self, vertex:int | str):
        if vertex not in self.adjacecy_list.keys():
            return False
        edges = self.adjacecy_list[vertex]
        for edge in edges:
            self.adjacecy_list[edge].remove(vertex)
        del self.adjacecy_list[vertex]
        return True

    def remove_edge(self, vertex1, vertex2):
        if self.undirected is False:
            return False

        keys = self.adjacecy_list.keys()
        if vertex1 in keys and vertex2 in keys:
             if vertex2 in self.adjacecy_list[vertex1]:
                self.adjacecy_list[vertex1].remove(vertex2)

             if vertex1 in self.adjacecy_list[vertex2]:
                self.adjacecy_list[vertex2].remove(vertex1)
             return True
        
        return False


