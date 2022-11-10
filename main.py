from functions import MainMenu, TortenelemMenu, SzezonbeliMeccsek, Jegyvasarlas, Jegyeim
# from fileHandling import loadData


print('Üdvözöljük az FC Barcelona hivatalos oldalán!')


valasz = -1
while valasz != 5:
    valasz = int(MainMenu())
    if valasz == 1:
        TortenelemMenu()
    elif valasz == 2:
        SzezonbeliMeccsek()
    elif valasz == 3:
        Jegyvasarlas()
    elif valasz == 4:
        Jegyeim()


# names = loadData()

#if Torimenu() == False:
#    print('')
