from graph_generation import graph_gen



def dijkstra(start, goal):
    graph = graph_gen()
    dijkstra_result = {}
    shortest_distance = {}
    predecessor = {}
    unseenNodes = graph
    infinity = 9999999
    path = []
    for node in unseenNodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0

    while unseenNodes:
        minNode = None
        for node in unseenNodes:
            if minNode is None:
                minNode = node
            elif shortest_distance[node] < shortest_distance[minNode]:
                minNode = node

        for childNode, weight in graph[minNode].items():
            if weight + shortest_distance[minNode] < shortest_distance[childNode]:
                shortest_distance[childNode] = weight + shortest_distance[minNode]
                predecessor[childNode] = minNode
        unseenNodes.pop(minNode)

    currentNode = goal
    while currentNode != start:
        try:
            path.insert(0, currentNode)
            currentNode = predecessor[currentNode]
        except KeyError:
            dijkstra_result['status'] = 0

            return dijkstra_result
            # break
    path.insert(0, start)
    if shortest_distance[goal] != infinity:
        print('Shortest distance is ' + str(shortest_distance[goal]))
        print('And the path is ' + str(path))
        dijkstra_result['status'] = 1
        dijkstra_result['shortest_distance'] = shortest_distance[goal]
        dijkstra_result['path'] = path
        # print(dijkstra_result)

        # print(dijkstra_result['path'])

        # print(path)


        return dijkstra_result

#print(dijkstra('khilgaon', 'mirpur'))
