from functions import MainMenu, TortenelemMenu, SzezonbeliMeccsek, Jegyvasarlas, Jegyeim, OsszesSzereples, legjobbszezonok, legrosszabbszezon, top3szezon, legtobbgol, evszamKereso, osszesMeccs, hazaiMeccsek, vendegMeccsek, main_login_signup
from fileHandling import loadData, loadData2

print('Üdvözöljük az FC Barcelona hivatalos oldalán!')

osszesAdat = loadData()
loggedIn = 0
valasz = -1
while valasz != 5:
    valasz = int(MainMenu())
    if valasz == 1:
        torValasz = TortenelemMenu()
        if torValasz == 1:
            print(f'\tEddig {OsszesSzereples(osszesAdat)}-szer szerepeltek a bajnokságba.')
        elif torValasz == 2:
            print(f'\tEzekben az években értek el első helyezést: {legjobbszezonok()}')
        elif torValasz == 3:
            print(f'\tEzekben az években érték ek a legrosszabb helyezést: {legrosszabbszezon()}')
        elif torValasz == 4:
            print(f'\tA szezonban lőtt legtöbb gól: {legtobbgol()}')
        elif torValasz == 5:
            print(f'\tEzekben az években végeztek a dobogón: {top3szezon()}')
        elif torValasz == 6:
            bekeres = input('Kérem adja meg az évszámot: ')
            evszamKereso(bekeres)
    elif valasz == 2:
        Szezonbelivalasz = SzezonbeliMeccsek()
        if Szezonbelivalasz == 1:
            print(f'\t A következő meccsek: ')
            osszesMeccs()
        elif Szezonbelivalasz == 2:
            hazaiMeccsek()
        elif Szezonbelivalasz == 3:
            vendegMeccsek()
        elif Szezonbelivalasz == 4:
            pass
    elif valasz == 3:
        while loggedIn == 0:
            loggedIn = main_login_signup()
        Jegyvasarlas()
    elif valasz == 4:
        print(Jegyeim())
