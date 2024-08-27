


class Graph():
    def __init__(self, undirected = True) -> None:
        self.adjacecy_list = {}
        self.undirected = undirected

    def add_vertex(self, vertex: str | int):
        self.adjacecy_list[vertex] = []


    def add_edge(self, start: int | str, destination: int | str):
        self.adjacecy_list[start].append(destination)
        
        if self.undirected:
            self.adjacecy_list[destination].append(start)

    def remove_vertex(self, vertex:int | str):
        self.adjacecy_list.pop(vertex)

        for vertex  in self.adjacecy_list.keys():
            # removing vertex from the array of all other vertices
            self.adjacecy_list[vertex] = [v for v in self.adjacecy_list[vertex] if v != vertex]



