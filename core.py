import random
from center import findCenter, findDiameter, findRanking

# example graphs
graphA = {
    'a':{'b':3, 'j':4, 'g': 1},
    'b':{'a':3, 'd':10},
    'c':{'q':5, 'h':3},
    'd':{'b':10, 'j':3, 'h':6},
    'e':{'g':14, 'f':2, 'i':2, 'z':2},
    'f':{'i':3, 'e':2, 'g':8, 'h':4},
    'g':{'f':8, 'e':14, 'j':6, 'a':1},
    'h':{'c':3, 'f':4, 'd':6},
    'i':{'e':2, 'f':3},
    'j':{'d':3, 'g':6, 'a':4},
    'k':{'z':10},
    'l':{'z':3, 'm':6},
    'm':{'l':6, 'p':8, 'o':4, 'n':2},
    'n':{'o':11, 'm':2},
    'o':{'m':4, 'n':11},
    'p':{'m':8},
    'q':{'c':5, 'r':7},
    'r':{'s':13, 't':1, 'q':7},
    's':{'r':13},
    't':{'r':1},
    'z':{'e':2, 'k':10, 'l':3}
}

graphB = {
    'a':{'c':2},
    'b':{'c':4},
    'c':{'a':2, 'b':4, 'd':3},
    'd':{'c':3, 'g':1, 'i':9},
    'e':{'g':7},
    'f':{'g':3},
    'g':{'e':7, 'f':3, 'd':1},
    'h':{'i':1, 'k':2},
    'i':{'d':9,'h':1, 'j':3, 'k':1},
    'j':{'i':3, 'k':5},
    'k':{'j':5, 'i':1, 'h':2, 'l':3},
    'l':{'k':3, 'n':5, 't':7},
    'm':{'n':8, 'o':1},
    'n':{'m':8, 'o':3, 'l':5},
    'o':{'n':3, 'm':1, 'q':1},
    'p':{'q':7},
    'q':{'o':1, 's':21, 'r':13, 'p':7},
    'r':{'q':13},
    's':{'q':21},
    't':{'l':7, 'u':6, 'w':1},
    'u':{'t':6},
    'w':{'t':1, 'y':3},
    'y':{'w':3, 'z':2},
    'z':{'y':2, 'aa':9},
    'aa':{'z':9, 'ab':7, 'ac':5},
    'ab':{'aa':7, 'ad':6},
    'ac':{'ad':1, 'aa':5},
    'ad':{'ac':1, 'ab':6}
}

graphC = {
    'a':{'b':5, 'ai':4},
    'b':{'a':5, 'ac':4, 'c':5},
    'c':{'b':5, 'ab':4, 'd':5},
    'd':{'c':5, 'e':6, 'g':8},
    'e':{'f':3, 'd':6},
    'f':{'e':3, 'g':8},
    'g':{'d':8, 'h':6, 'i':4, 'w':3, 'y':4,'f':8},
    'h':{'g':6},
    'i':{'g':4, 'j':3, 'k':3, 'l':4},
    'j':{'i':3},
    'k':{'i':3},
    'l':{'i':4, 'm':2, 'n':2, 'o':7},
    'm':{'l':2},
    'n':{'l':2},
    'o':{'l':7, 'p':4, 't':3, 'u':3, 'r':1},
    'p':{'o':4},
    'q':{'r':4},
    'r':{'q':4, 'o':1, 's':3},
    's':{'r':3, 'u':4, 'y':8, 'z':9, 'af':3},
    't':{'o':3, 'w':4, 'u':3},
    'u':{'s':4, 'y':5, 't':3, 'o':3},
    'w':{'g':3, 't':4},
    'y':{'aa':4, 'g':4, 'u':5, 's':8, 'z':3},
    'z':{'y':3, 's':9, 'ad':3, 'ac':4},
    'aa':{'ab':2, 'y':4},
    'ab':{'aa':2, 'c':4},
    'ac':{'b':4, 'z':4},
    'ad':{'z':3, 'ai':4, 'ae':4},
    'ae':{'ad':4, 'af':4},
    'af':{'ae':4, 's':2, 'ag':3},
    'ag':{'ah':4, 'af':3},
    'ah':{'ag':4, 'ai':4},
    'ai':{'ad':4, 'ah':4, 'a':4}
}

def avgEdgeWeight(graph):
    count = 0
    sum = 0
    for vertex in graph.keys():
        for weight in graph[vertex].values():
            sum+=weight
            count+=1
    return sum/count
ranomOrder = True
iterationLimit = 140
megeLimit = 3
graph = graphC
avgEdgeWeight = avgEdgeWeight(graph)
print(avgEdgeWeight)
print("ranking: ", findRanking(graph))
unseenNodes = list(graph.keys())
#unseenNodes = ['ad']
counter = 0


def selectNode():
    global selectedNode
    if ranomOrder:
        selectedNode = random.choice(unseenNodes)
        unseenNodes.remove(selectedNode)
    else:
        selectedNode = unseenNodes.pop(0)

    return selectedNode


def createLocalGraph():
    localGraph = dict()
    localGraph[selectedNode] = graph.get(selectedNode)
    for neighbour in neighbours:
        if neighbour in graph.keys():
            localGraph[neighbour] = graph[neighbour]
            del graph[neighbour]
    del graph[selectedNode]
    return localGraph


def findLocalGraphNeighbours():
    localGraphNeighbours = set()
    for localNode in localGraph.keys():
        localChilds = localGraph[localNode]
        for child in localChilds:
            if child not in localGraph.keys():
                localGraphNeighbours.add(child)
    return localGraphNeighbours


def modifyConnections():
    global extNeigh
    for extNeigh in localGraphNeighbours:
        for extConn in list(graph[extNeigh]):
            if extConn in localGraph.keys():
                weight = graph[extNeigh][extConn]
                del graph[extNeigh][extConn]
                graph[extNeigh][mergedNode] = weight + localGraphDiameter
    graph[mergedNode] = dict()


while unseenNodes:
    # stop condition
    if counter > iterationLimit:
        break
    # select node and delete from unseen nodes. Random or not.
    selectedNode = selectNode()
    counter = counter+1

    # find neighbours for selected node, but only when
    # connection edge weight is smaller than avg edge weight
    if graph.get(selectedNode) is None:
        continue
    neighbours = graph.get(selectedNode).copy()
    for neighbour in set(neighbours.keys()):
        if graph[selectedNode][neighbour] > avgEdgeWeight:
            del neighbours[neighbour]

    if not neighbours:
        continue

    # create local graph and delete local graph vertexes from global graph
    localGraph = createLocalGraph()

    # find local graph neighbours in global graph
    localGraphNeighbours = findLocalGraphNeighbours()

    # find diameter of local graph
    localGraphDiameter = findDiameter(localGraph)
    # create merged node name
    mergedNode = '-'.join(localGraph.keys())
    # modify connections in global graph. replace connections to local graph internal vertexes
    # and replace with connection to whole local graph with modified weigh as
    # new weight = old weight + local graph diameter
    modifyConnections()

    # add connections between new merged vertex and external neighbours
    for extNeigh in localGraphNeighbours:
        graph[mergedNode][extNeigh] = graph[extNeigh][mergedNode]


print("center: ", findCenter(graph))
print("optimal ranking: ", findRanking(graph))