from functions import MainMenu, TortenelemMenu, SzezonbeliMeccsek, Jegyvasarlas, Jegyeim, OsszesSzereples
from fileHandling import loadData


print('Üdvözöljük az FC Barcelona hivatalos oldalán!')


valasz = -1
while valasz != 5:
    valasz = int(MainMenu())
    if valasz == 1:
        if TortenelemMenu() == 1:
            print(f'Eddig {OsszesSzereples()}-szer szerepeltek a bajnokságba.')
    elif valasz == 2:
        SzezonbeliMeccsek()
    elif valasz == 3:
        Jegyvasarlas()
    elif valasz == 4:
        Jegyeim()


