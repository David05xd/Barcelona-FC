
def TortenelemMenu():
    option = -1
    while option < 1 or option > 6:
        print('1 - Hány éve szerepelnek')
        print('2 - Legeredményesebb szezon')
        print('3 - Leggyengébb szezon')
        print('4 - Legtöbb lőtt gól a szezonban')
        print('5 - Eddigi Top 3 szezonok')
        print('6 - Szezonlekérés')
        print('7 - Vissza a főmenübe')
        option = int(input('Válasszon a fentiek közül: '))
    return option

def SzezonbeliMeccsek():
    option = -1
    while option < 1 or option > 6:
        print('1 - ')
        print('2 - ')
        print('3 - ')
        print('4 - ')
        print('5 - ')
        print('6 - ')
        print('7 - ')
        option = int(input('Válasszon a fentiek közül: '))
    return option

def Jegyvasarlas():
    option = -1
    while option < 1 or option > 6:
        print('1 - ')
        print('2 - ')
        print('3 - ')
        print('4 - ')
        print('5 - ')
        print('6 - ')
        print('7 - ')
        option = int(input('Válasszon a fentiek közül: '))
    return option

def Jegyeim():
    option = -1
    while option < 1 or option > 6:
        print('1 - ')
        print('2 - ')
        print('3 - ')
        print('4 - ')
        print('5 - ')
        print('6 - ')
        print('7 - ')
        option = int(input('Válasszon a fentiek közül: '))
    return option

def MainMenu():
    option = -1
    while option < 1 or option > 5:
        print('1 - Klubtörténelem')
        print('2 - Szezonbeli meccsek')
        print('3 - Jegyvásárlás')
        print('4 - Jegyeim')
        print('5 - Kilépés')
        option = int(input('Válasszon a fentiek közül: '))
    return option
