from beolvasas import*


def loadData():
    names = []
    file = open('nevek.csv', 'r', encoding='utf-8')
    
    firstRow = file.readline()
    for row in file:
        splitted = row.split(';')
        res = names()
        res.name = splitted[0]
        res.password = splitted[1]
        
        
        names.append(res)
    
    file.close

    return names

def saveResult(res):
    file = open('nevek.csv', 'a', encoding='utf-8')
     
    file.write(f'{res.name};{res.password}')