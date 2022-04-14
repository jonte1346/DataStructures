import sys


N, Q = (int(x) for x in input().split())

nodes = []
for n in range(N):
    word = input()
    nodes.append(word)

queries = []
for n in range(Q):
    queries.append(input().split())

for i in nodes:
    print(i)
for k in queries:
    print(k)

class Node:

    def __init__(self, node, neighbours):
        self.node = node
        self.neigbours = neighbours
        self.visited = False

def BFS(startNode, endNode):
    #startNode.visited = True
    list = [startNode]
    print(startNode + " -> "+ endNode)



for startWord, endWord in queries:
    BFS(startWord, endWord)



