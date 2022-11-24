from functions import MainMenu, TortenelemMenu, SzezonbeliMeccsek, Jegyvasarlas, Jegyeim, OsszesSzereples, legjobbszezonok, legrosszabbszezon, top3szezon, legtobbgol, evszamKereso
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
            print(f'\tEzekben az években értek el első helyezést: {legjobbszezonok()}')
        if TortenelemMenu() == 3:
            print(f'\tEzekben az években érték ek a legrosszabb helyezést: {legrosszabbszezon()}')
        if TortenelemMenu() == 4:
            print(f'\tA szezonban lőtt legtöbb gól: {legtobbgol()}')
        if TortenelemMenu() == 5:
            print(f'\tEzekben az években végeztek a dobogón: {top3szezon()}')
        if TortenelemMenu() == 6:
            bekeres = input('Kérem adja meg az évszámot: ')
            evszamKereso(bekeres)
    elif valasz == 2:
        if SzezonbeliMeccsek() == 1:
            print(f'\t A következő meccsek: {osszesMeccs()}')
    elif valasz == 3:
        Jegyvasarlas()
    elif valasz == 4:
        print(Jegyeim())
