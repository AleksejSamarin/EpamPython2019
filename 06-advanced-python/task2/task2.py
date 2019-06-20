"""
E - dict(<V> : [<V>, <V>, ...])
Ключ - строка, идентифицирующая вершину графа
значение - список вершин, достижимых из данной

Сделать так, чтобы по графу можно было итерироваться(обходом в ширину)

"""


class Graph:
    def __init__(self, E):
        self.E = E

    def __iter__(self):
        return GraphIterator(self)


class GraphIterator:
    def __init__(self, graph):
        self.E = graph.E
        self.to_pass = []
        self.is_first = True
        self.first_key, self.vertices = tuple(self.E.items())[0]
        self.vertices_count = len(self.E.items())
        self.passed = [self.first_key]

    def __next__(self):
        if self.is_first:
            self.is_first = False
            return self.first_key
        while len(self.passed) < self.vertices_count and self.vertices:
            for vertice in self.vertices:
                if vertice not in self.passed:
                    self.to_pass.extend(self.E[vertice])
                    self.passed.append(vertice)
                    return vertice
            self.vertices = self.to_pass[:]
            self.to_pass.clear()
        raise StopIteration()

    def __iter__(self):
        return self


if __name__ == '__main__':
    E = {'A': ['B', 'C', 'D'], 'B': ['C'], 'C': [], 'D': ['A']}
    graph = Graph(E)

    for vertice in graph:
        print(vertice)
