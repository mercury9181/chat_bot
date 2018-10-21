# graph = {'a': {'b': 10, 'c': 3}, 'b': {'c': 1, 'd': 2}, 'c': {'b': 4, 'd': 8, 'e': 2}, 'd': {'e': 7}, 'e': {'d': 9}}

import pymysql

connection = pymysql.connect(host='localhost', user='root', db='bot')

a = connection.cursor()
query = 'select * from place'

a.execute(query)
data = a.fetchall()
print(data)

graph = {}

location_names = []

for row in data:
    location_names.append(row[1])

print(location_names)
k = 0

for row in data:
    current_list = {}
    i = 0
    j = 0

    for row_entry in row:
        if i > 1:
            current_list[location_names[j]] = row_entry
            j += 1
        i += 1
    graph[location_names[k]] = current_list
    k +=1

print(graph)


def dijkstra(graph, start, goal):
    shortest_distance = {}
    predecessor = {}
    unseenNodes = graph
    infinity = 9999999
    path = []
    for node in unseenNodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0
    # print(shortest_distance)
    while unseenNodes:

        min_node = None
        for node in unseenNodes:
            if min_node is None:
                min_node = node
            elif shortest_distance[node] < shortest_distance[min_node]:
                min_node = node

        for child_node, weight in graph[min_node].items():
            if weight + shortest_distance[min_node] < shortest_distance[child_node]:
                shortest_distance[child_node] = weight + shortest_distance[min_node]
                predecessor[child_node] = min_node
        unseenNodes.pop(min_node)

    currentNode = goal
    while currentNode != start:
        try:
            path.insert(0, currentNode)
            currentNode = predecessor[currentNode]
        except KeyError:
            print('Path not reachable')
            break
    path.insert(0, start)
    if shortest_distance[goal] != infinity:
        print("shortest distance : ", shortest_distance[goal])
        print("path: ", path)


dijkstra(graph, 'khilgaon', 'banglamotor')
