from dijkstra import dijkstra
import random

def findRandomizedCenter(graph):
    executions = 0
    paths = dict()
    graph.keys()
    totalMin = 5000
    k = random.sample(list(graph.keys()), len(graph))
    print(k)
    for v1 in k:
        max = 0
        l = random.sample(list(graph.keys()), len(graph))
        for v2 in l:
            if (v1 != v2):
                dist = dijkstra(graph, v1, v2)
                executions = executions + 1
                if dist > max:
                    max = dist
                if max > totalMin:
                    break
        paths[max] = v1
        if max < totalMin:
            totalMin = max
            center = v1
    print("dijkstra executions: ", executions)
    return center