from Eredmeny import Eredmeny, Meccsek

def loadData():
    file = open('Adatbazis_Barcelona.csv','r',encoding='utf-8')

    results = []

    for row in file:
        
        e = Eredmeny()
        splitted = row.strip().split(';')
        e.evszam = str(splitted[0])
        e.helyezes = str(splitted[1])
        e.lottgol = str(splitted[2])
        
        results.append(e)

    file.close()
    return results

def loadData2():
    file = open('meccsek.csv','r',encoding='utf-8')

    results = []

    for row in file:
        
        e = Meccsek()
        splitted = row.strip().split(';')
        e.datum = str(splitted[0])
        e.hejszin = str(splitted[1])
        
        results.append(e)

    file.close()
    return results