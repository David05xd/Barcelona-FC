from functions import MainMenu, TortenelemMenu, SzezonbeliMeccsek, Jegyvasarlas, Jegyeim, OsszesSzereples, legjobbszezonok, legrosszabbszezon, top3szezon, legtobbgol
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
        if TortenelemMenu() == 3:
            print(f'Ezekben az években érték ek a legrosszabb helyezést: {legrosszabbszezon()}')
        if TortenelemMenu() == 4:
            print(f'A szezonban lőtt legtöbb gól: {legtobbgol()}')
        if TortenelemMenu() == 5:
            print(f'Ezekben az években végeztek a dobogón: {top3szezon()}')
    elif valasz == 2:
        SzezonbeliMeccsek()
    elif valasz == 3:
        Jegyvasarlas()
    elif valasz == 4:
        Jegyeim()
