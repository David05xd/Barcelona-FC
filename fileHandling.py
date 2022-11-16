data = []


def loadData():
    file = open('Adatbazis_Barcelona','r',encoding='utf-8')

    for row in file:
        data.append(row.strip())


file.close()

# def saveResult(res):
#     file = open('nevek.csv', 'a', encoding='utf-8')
    
#     file.write(f'{res.evszam};{res.hejezes};{res.golok}')