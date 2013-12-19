__author__ = 'martin'
from queue import Queue


class Vertex:
    def __init__(self, name):
        self.name = name
        self.in_degree_set = set()
        self.out_degree_set = set()

    def __str__(self):
        return "Name: %s\tin-degrees:%s\tout-degrees: %s" % (
            self.name,
            ",".join(v.name for v in self.in_degree_set) if len(self.in_degree_set) > 0 else "-",
            ",".join(v.name for v in self.out_degree_set) if len(self.out_degree_set) > 0 else "-"

        )

    def add_out_degree(self, vertex):
        self.out_degree_set.update([vertex])

    def add_in_degree(self, vertex):
        self.in_degree_set.update([vertex])

    def remove_in_degree(self, vertex):
        self.in_degree_set.remove(vertex)

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(('name', self.name))


def add_edge(u, v):
    u.add_out_degree(v)
    v.add_in_degree(u)


def topological_sort(V):
    Q = Queue()
    for u in set(V):
        if len(u.in_degree_set) == 0:
            Q.put(u)

    Output = []
    while not Q.empty():
        u = Q.get()
        Output.append(u)

        for v in u.out_degree_set:
            v.remove_in_degree(u)
            if len(v.in_degree_set) == 0:
                Q.put(v)
    return Output

# main
print("=> Topological Sort")

v0 = Vertex("0")
v1 = Vertex("1")
v2 = Vertex("2")
v3 = Vertex("3")
v4 = Vertex("4")
v5 = Vertex("5")
v6 = Vertex("6")
v7 = Vertex("7")
v8 = Vertex("8")
v9 = Vertex("9")

add_edge(v0, v1)
add_edge(v0, v6)
add_edge(v0, v4)
add_edge(v1, v2)
add_edge(v2, v7)
add_edge(v2, v5)
add_edge(v3, v8)
add_edge(v4, v5)
add_edge(v5, v9)
add_edge(v6, v3)
add_edge(v6, v2)
add_edge(v7, v8)
add_edge(v8, v9)

graph = [v0, v6, v1, v4, v3, v2, v5, v7, v8, v9]

print("=> Vertices in Graph")
print("\n".join("%d. %s" % (kv[0] + 1, kv[1]) for kv in list(enumerate(graph))))

output = topological_sort(graph)
print("=> Output:")
print(",".join(v.name for v in output))