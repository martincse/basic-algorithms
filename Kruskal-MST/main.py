__author__ = 'martin'

from DataStructure import Vertex
from DataStructure import EdgeSet
from DisjointSet import *
print("Kruskal Algorithm - MST")

# create set - O(|V|)
a = Vertex("A")
b = Vertex("B")
c = Vertex("C")
e = Vertex("E")
f = Vertex("F")
g = Vertex("G")
h = Vertex("H")

s = EdgeSet()
s.add(a, b, 2.3)
s.add(b, c, 1.4)
s.add(c, g, 3.7)
s.add(g, f, 2.4)
s.add(f, e, 2.8)
s.add(e, a, 2.0)
s.add(a, h, 1.8)
s.add(h, c, 2.7)
s.add(h, g, 4.0)
s.add(h, e, 2.1)
s.add(b, h, 3.9)
s.add(h, f, 3.4)

print("Input =>")
print(s)

s.sortByAsc() # O(|E| log |E|)

print("Sort by Ascending weight =>")
print(s)

E = s.list
A = EdgeSet()

for e in E:
    # O (|E| log |V|)
    uRoot = FindSet(e.u)
    vRoot = FindSet(e.v)
    if uRoot != vRoot:
      A.addNode(e)
      Union( uRoot, vRoot )

print("MST Result =>")
print(A)
