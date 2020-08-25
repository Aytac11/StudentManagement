users=[]
class User:
    def __init__(self,_ad,_soyad,_username,_password):
        self.ad=_ad
        self.soyad=_soyad
        self.username=_username
        self.password=_password
    def showdata(self):
        print(f"Ad: {self.ad}, Soyad: {self.soyad}, Username: {self.username}, Password: {self.password}")

def userYarat():
    inputad=input("Ad: ")
    inputsoyad=input("Soyad: ")
    inputusername=input("Username: ")
    inputpassword=input("Password: ")
    users.append(User(inputad,inputsoyad,inputusername,inputpassword))

def qeydiyyat():
    userSayi=int(input("User sayini teyin edin:"))
    for say in range(userSayi):
        print(f"{say+1}-ci useri daxil edin")
        userYarat()

def butunIstifadecileriGoster():
     for user in users:
          user.showdata()


def adaGoreMelumatlarinGosterilmesi():
    telebOlunanAd=input("Melumatlarini gormek istediyiniz userin adini daxil edin: ")
    for i in range(len(users)):
        if telebOlunanAd==users[i].ad:
            print(f"Ad: {users[i].ad}, Soyad: {users[i].soyad}, Username: {users[i].username},Password:{users[i].password}")
            break
    else:
        print("Bu adda user yoxdur!")


def adiEnUzunOlanIstifadeciniTap():
    for j in range(len(users)):
        maxlen=len(users[j].ad)
        for k in range(len(users)):
            if len(users[k].ad)>maxlen:
                Max=users[k].ad
                print(f"Adi en uzun olan istifadeci: {Max}")




def soyadindaOvOlanlariGoster():
    for a in range(len(users)):
        if "ov" in users[a].soyad:
            print(f"Soyadinda 'ov' olan istifadecinin Adi: {users[a].ad}, Soyadi: {users[a].soyad}")
            break
    else:
        print("Bele soyadi olan yoxdur!")



def passworduEnUzunIstifadeci():
    for b in range(len(users)):
        enuzunpassword=len(users[b].password)
        for x in range(len(users)):
            if len(users[x].password)>enuzunpassword:
                maxuzun=users[x].password
                print(f"Passwordu en uzun olan istifadeci: {maxuzun}")


print("""
==========================================================================
Aparmaq istediyiniz emeliyyatinnomresini secin:
==========================================================================
0.Proqrami dayandir
1.Qeydiyyat prosesine baslayin
2.Ada gore userin melumatlarini gosterin
3.Adi en uzun olan userin melumatlarini gosterin
4.Soyadinda 'ov' olan istifadecileri gosterin
5.Passwordu en uzun olan istifadecinin melumatlarini gosterin
6.Butun userlari goster
==========================================================================
==========================================================================
""")

while True:
    n =int(input("Emeliyyat nomresini daxil edin: "))
    if n==0:
        print("Tesekkurler")
        break
    elif n==1:
        qeydiyyat()
    elif n==2:
        adaGoreMelumatlarinGosterilmesi()
    elif n==3:
        adiEnUzunOlanIstifadeciniTap()
    elif n==4:
        soyadindaOvOlanlariGoster()
    elif n==5:
        passworduEnUzunIstifadeci()
    elif n==6:
        butunIstifadecileriGoster()
    else:
        break

