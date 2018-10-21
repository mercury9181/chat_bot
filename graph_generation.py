import pymysql

connection = pymysql.connect(host='localhost', user='root', db='bot')

a = connection.cursor()

query_place = 'select * from place'

a.execute(query_place)


def graph_gen():
    graph = {}
    data = a.fetchall()



    location_names = []

    for row in data:
        location_names.append(row[1])

    # print(location_names)
    k = 0
    for row in data:

        currList = {}
        i = 0
        j = 0

        for rowEntry in row:
            if i > 1:
                currList[location_names[j]] = rowEntry
                j += 1

            i += 1
        graph[location_names[k]] = currList
        k += 1
    g_result = graph
    # print("ami result: ")
    # print(g_result)

    return g_result

# mysql and graph generating finished

