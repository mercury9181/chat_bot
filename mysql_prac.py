import pymysql

connection= pymysql.connect(host='localhost', user='root', db='bot')

a = connection.cursor()

query = 'select * from place'

a.execute(query)


mainList = []
data = a.fetchall()


for row in data:
    currList = []

    col = 0
    for rowEntry in row:
        if col > 1:
            currList.append(rowEntry)

        col += 1
    mainList.append(currList)

print(mainList)





