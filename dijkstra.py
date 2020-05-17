def dijkstra(graph, start, goal):

    shortest_distance = {}
    track_predecessor = {}
    unseenNodes = graph.copy()

    for node in unseenNodes:
        shortest_distance[node] = 5000

    shortest_distance[start] = 0

    while unseenNodes:
        min_distance_node = None

        for node in unseenNodes:
            if min_distance_node is None:
                min_distance_node = node
            elif shortest_distance[node] < shortest_distance[min_distance_node]:
                min_distance_node = node

        path_options = graph[min_distance_node].items()

        for child_node, weight in path_options:
            if child_node in shortest_distance.keys():
                if weight + shortest_distance[min_distance_node] < shortest_distance[child_node]:
                    shortest_distance[child_node] = weight + shortest_distance[min_distance_node]
                    track_predecessor[child_node] = min_distance_node

        unseenNodes.pop(min_distance_node)

    return shortest_distance[goal]