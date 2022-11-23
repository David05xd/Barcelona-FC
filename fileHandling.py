from Eredmeny import Eredmeny

def loadData():
    file = open('feremcvaros/Adatbazis_Barcelona.csv','r',encoding='utf-8')

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