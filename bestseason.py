data = []

def bestseason():
    maximum = 0
    for szam in data:
        if szam > maximum:
            maximum = szam 
    print(maximum)
