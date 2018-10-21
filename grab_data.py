import pymysql

from test import dijkstra

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


places = ['khilgaon', 'banglamotor', 'farmgate', 'mirpur']
print(len(places))
main_string = ""
for i in range(0, len(places) - 1):

    common_bus_list = find_common_bus(places[i], places[i + 1])
    s1 = "from " + str(places[i]) + " take " + str(common_bus_list) + " bus to go to " + str(places[i + 1]) + "\n"
    main_string += s1

print(main_string)
