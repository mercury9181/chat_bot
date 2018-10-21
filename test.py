from flask import Flask, request
from fbmq import Page
import random

from intent import parseMsg
import pymysql

page = Page(
    "EAAbDW7mU7OQBAHcQQQ9OA0fmOEcaKoZBCQ1GexGzSqedRSS8wSxPZCVM5rNNdweAZAFuQ1i0dyNw71lEPR3YEjz08GN6QRkmWE546aSZB1LEVFH8qKYYWnA64vmN2vcOyWFWmq0ko5RBQ27vsh1UWvVmjKI3cD7U4huRN63upwZDZD")

app = Flask(__name__)

main_string = ""
def dijkstra(start, goal):
    # graph generation
    connection = pymysql.connect(host='localhost', user='root', db='bot')

    a = connection.cursor()

    query_place = 'select * from place'

    a.execute(query_place)
    graph = {}
    data = a.fetchall()

    location_names = []
    main_string = ""

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
        # print('Shortest distance is ' + str(shortest_distance[goal]))
        # print('And the path is ' + str(path))
        dijkstra_result['status'] = 1
        dijkstra_result['shortest_distance'] = shortest_distance[goal]
        dijkstra_result['path'] = path

        print(dijkstra_result['path'])

        return dijkstra_result


def get_bus_list(path):
    connection = pymysql.connect(host='localhost', user='root', db='bot')

    b = connection.cursor()

    query_bus_list = 'select * from buslist'

    b.execute(query_bus_list)

    data_bus_list = b.fetchall()
    bus_list = dict()

    for row in data_bus_list:
        buses = str(row[2]).replace("'", "").replace(" ", '').split(',')
        bus_list[row[1]] = buses

    # print(bus_list)

    def find_common_bus(s, d):
        s_buses = bus_list[s]
        d_buses = bus_list[d]
        common_buses = list(set(s_buses).intersection(d_buses))

        return common_buses

    places = path
    print(len(places))
    main_string=""
    for i in range(0, len(places) - 1):
        common_bus_list = find_common_bus(places[i], places[i + 1])
        s1 = "from " + str(places[i]) + " take " + str(common_bus_list) + " bus to go to " + str(places[i + 1]) + "\n"
        main_string += s1

    return main_string



@app.route('/webhook', methods=['POST'])
def webhook():
    page.handle_webhook(request.get_data(as_text=True))
    return "ok"


@app.route('/webhook', methods=["GET"])
def fb_webhook():
    verification_code = '1234'
    verify_token = request.args.get('hub.verify_token')
    if verification_code == verify_token:
        return request.args.get('hub.challenge')


greeting_replies = ['Hi 😉', 'Hello..!', 'Wassup', 'Howdy!??', 'hey there!!', 'yo yo.!']

bye_replies = ['tata', 'thank you', 'adios,my friend', 'bye bye', 'see you again',
               'tada my friend']

default_replies = ['sorry,bujhi nai', 'o kita koilen apni??', 'ahem ahem..arekbar bolen!', 'mathar opr diye gelo!! :/',
                   'mone onk dukkho na!! ami bujhi!😶', ]


@page.handle_message
def message_handler(event):
    """:type event: fbmq.Event"""

    page_id = page.page_id
    page_name = page.page_name
    user_profile = page.get_user_profile(event.sender_id)  # return dict
    # print(user_profile)

    sender_id = event.sender_id
    message = event.message_text
    print(event.message_text)

    result = parseMsg(message)
    print(result)
    if (result.name == "search"):
        dijkstra_result = dijkstra(str(result.matches['start']), str(result.matches['goal']))
        path = dijkstra_result['path']
        bus_list=str(get_bus_list(path))
        print("D result = " + str(dijkstra_result))
        if (dijkstra_result['status'] == 0):

            page.send(sender_id, "path not found in database")
        else:
            page.send(sender_id,
                      "so " + user_profile['first_name'] + " you want to go to " + result.matches['goal'] + " from " +
                      result.matches['start'])
            page.send(sender_id, "i will be right back with ur bus information")


            page.send(sender_id, "you have to go in this route : \n" + str(path))
            page.send(sender_id, "and the distance is: " + str(dijkstra_result['shortest_distance']))
            page.send(sender_id, "now for information regarding the buses ")
            page.send(sender_id, " so..\n " + bus_list)
            page.send(sender_id, "Finally congratulation ..you will reach at your destination in the shortest way :)")



    elif (result.name == "greetings"):
        page.send(sender_id, greeting_replies[random.randint(0, len(greeting_replies))])

    elif (result.name == "bye"):
        page.send(sender_id, bye_replies[random.randint(0, len(bye_replies))])

    else:
        page.send(sender_id, "Can't understand. Try again")


@page.after_send
def after_send(payload, response):
    """:type payload: fbmq.Payload"""
    print("complete")


if __name__ == "__main__":
    app.run()
