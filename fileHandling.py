data = []


def loadData():
    file = open('Adatbazis_Barcelona.csv','r',encoding='utf-8')

    for row in file:
        data.append(row.strip())


    file.close()