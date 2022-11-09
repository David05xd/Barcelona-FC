from main import age

def menu():
    print('Választható funkciók: \n 1---Hány éve szerepelnek \n 2---Legeredményesebb szezon \n 3---Leggyengébb szezon \n 4---Legtöbb lőtt gól a szezonban \n 5---Eddigi Top 3 szezonok \n 6---Szezonlekérés')
    choice = int(input('Kérem válasszon opciót: '))
    if 0 < choice < 7:
        return choice
    else:
        return False

def eletkor():
    pass