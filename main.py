from functions import MainMenu, TortenelemMenu, SzezonbeliMeccsek, Jegyvasarlas, Jegyeim, OsszesSzereples, legjobbszezonok
from fileHandling import loadData

print('Üdvözöljük az FC Barcelona hivatalos oldalán!')

osszesAdat = loadData()

valasz = -1
while valasz != 5:
    valasz = int(MainMenu())
    if valasz == 1:
        if TortenelemMenu() == 1:
            print(f'\tEddig {OsszesSzereples(osszesAdat)}-szer szerepeltek a bajnokságba.')
        if TortenelemMenu() == 2:
            print(f' Ezekben az években értek el első helyezést: {legjobbszezonok()}')
    elif valasz == 2:
        SzezonbeliMeccsek()
    elif valasz == 3:
        Jegyvasarlas()
    elif valasz == 4:
        Jegyeim()
