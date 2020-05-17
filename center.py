import collections

from dijkstra import dijkstra


def findCenter(graph):
    executions = 0
    paths = dict()
    graph.keys()
    totalMin = 5000
    for v1 in graph.keys():
        max = 0
        for v2 in graph.keys():
            if (v1 != v2):
                dist = dijkstra(graph, v1, v2)
                executions = executions + 1
                if dist > max:
                    max = dist
                # if max > totalMin:
                #     break
        paths[v1] = max

        if max < totalMin:
            totalMin = max
            center = v1
    return center

def findRanking(graph):
    executions = 0
    paths = dict()
    graph.keys()
    for v1 in graph.keys():
        max = 0
        for v2 in graph.keys():
            if (v1 != v2):
                dist = dijkstra(graph, v1, v2)
                executions = executions + 1
                if dist > max:
                    max = dist
        if max in paths.keys():
            paths[max].add(v1)
        else:
            paths[max] = {v1}
    return collections.OrderedDict(sorted(paths.items()))
def findDiameter(graph):
    executions = 0
    paths = dict()
    graph.keys()
    totalMin = 5000
    for v1 in graph.keys():
        max = 0
        for v2 in graph.keys():
            if (v1 != v2):
                dist = dijkstra(graph, v1, v2)
                executions = executions + 1
                if dist > max:
                    max = dist
                if max > totalMin:
                    break
        paths[v1] = max
        if max < totalMin:
            totalMin = max
    return totalMin