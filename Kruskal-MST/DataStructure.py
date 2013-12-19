__author__ = 'martin'

from operator import attrgetter

class Vertex:
    def __init__(self, name):
        self.Name = name.upper()
        self.Parent = self
        self.Height = 1

    def __str__(self):
            return "Name: %s Height: %d Parent: %s" % (
                self.Name,
                self.Height,
                "\n\t%s" % self.Parent if self.Parent != self else "[Circular]"
            )
class EdgeNode:
    def __init__(self, u, v, weight):
        self.u = u
        self.v = v
        self.weight = weight

    def __str__(self):
        return "\n u: %s \n v: %s \n weight: %.1f" % (self.u, self.v, self.weight)


class EdgeSet:
    def __init__(self):
        self.list = []

    def addNode(self, edgeNode):
        self.list.append(edgeNode)

    def add(self, p1, p2, weight):
        self.list.append(EdgeNode(p1, p2, weight))

    def __str__(self):
        s = ""
        for i, node in enumerate(self.list):
            s += "%d.%s\n" % (i + 1, str(node))
        return s

    def sortByAsc(self):
        self.list = sorted(self.list, key=attrgetter('weight'))

