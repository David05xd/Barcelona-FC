from fileHandling import loadData

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
    option = int(input('Válassza ki a meccs időpontját (x.y.): '))
    file = open('','r',encoding='utf-8')
    for row in file:
        splittedData = row.split(';')
        if splittedData[0] == option:
            print(f'A meccs {option} -án/-én kerül megrendezésre{splittedData[1]} -ban/-ben')
            file = open('jegyeim.txt', 'a', encoding='utf-8')
            jegyekSzama = input('Hány jegyet szeretne? ')
            file.write(f'{splittedData[0]};{splittedData[1]};{jegyekSzama}')
            # --------------dátum^^^^^^^^--hely^^^^^^^^^^
            # ha kész az adatbázis be kell írni a számokat a splitted datákba
        else:
            print('Nincs ezen a napon meccs.')
    file.close()
    return

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


def OsszesSzereples(data):
    return(len(data))

#regisztracio
def login():
    user = input("Felhasználónév: ")
    passw = input("Jelszó: ")
    f = open("users.txt", "r")
    for line in f.readlines():
        us, pw = line.strip().split("|")
        if (user in us) and (passw in pw):
            print ("Login successful!")
            return True
    print ("Hibás felhasználónév/jelszó")
    return False

def signup():
    file = open('users.txt', 'a', encoding='utf-8')
    username = input('Új felhasználónév: ')
    password = input('Új jelszó: ')
    term = input('szerződés(y/n): ')
    if term == 'y':
        print('regisztráció sikeres!')
        file.write(f'{username}|{password}\n')
    elif term == 'n':
        print('Sikertelen regisztráció!')
    else:
        print('nincs ilyen opció!')


def main_login_signup():
    choice = input('a) login b) sign up ')
    logOutout = 0
    if choice == 'a':
        log = login()
        if log == True:
            pass
    elif choice == 'b':
        signup()
    else: print('nincs ilyen opció')
#regisztracio vege

def legjobbszezonok():
    file = open('Adatbazis_Barcelona.csv','r',encoding='utf-8')
    szezon = []
    for row in file:
        splittedData = row.split(';')
        if splittedData[1] == '1':
            szezon.append(int(splittedData[0]))
    file.close()
    return szezon

def legrosszabbszezon():
    file = open('Adatbazis_Barcelona.csv','r',encoding='utf-8')
    szezon = []
    for row in file:
        splittedData = row.split(';')
        if splittedData[1] == '9':
            szezon.append(int(splittedData[0]))
    file.close()
    return szezon

def top3szezon():
    file = open('Adatbazis_Barcelona.csv','r',encoding='utf-8')
    szezon = []
    for row in file:
        splittedData = row.split(';')
        if splittedData[1] == '1' or '2' or '3':
            szezon.append(int(splittedData[0]))
    file.close()
    return szezon

def legtobbgol():
    file = open('Adatbazis_Barcelona.csv','r',encoding='utf-8')
    mostGol = 0
    for row in file:
        splittedData = row.split(';')
        if int(splittedData[2]) > mostGol:
            mostGol = int(splittedData[2])
    file.close()
    return mostGol
