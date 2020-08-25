sinif=[]
class Telebe:
    def __init__(self,_kod,_ad,_soyad,_email,_tel):
        self.kod=_kod
        self.ad=_ad
        self.soyad=_soyad
        self.email=_email
        self.tel=_tel

    def showdata(self):
        print(f"Kod: {self.kod}, Ad: {self.ad}, Soyad: {self.soyad}, Email: {self.email}, Tel: {self.tel}")

def telebeYarat_listeElaveet():
     inputkod=int(input("Kod: "))
     if 100<inputkod<999:
         pass
     else:
         print("Dogru kodu elave et!")
         inputkod=int(input("Kod: "))
     inputad=input("Ad:")
     if inputad.isalpha():
         pass
     else:
         print("Soyad herflerden ibaret olmalidir!")
         inputad=input("Ad:")
     inputsoyad=input("Soyad: ")
     if inputsoyad.isalpha():
         pass
     else:
         print("Ad herflerden ibaret olmalidir!")
         inputsoyad=input("Soyad:")
     inputemail=input("Email: ")
     if "@" in inputemail:
         pass
     else:
         print("Dogru emaili elave edin!")
         inputemail=input("Email: ")
     inputtel=input("Tel: +994 ")
     if len(inputtel)<10 and inputtel.isdigit():
         pass
     else:
         print("Dogru telefon nomresi daxil edin!")
         inputtel=input("Tel: +994 ")

     telebe_obyekti=Telebe(inputkod, inputad,inputsoyad,inputemail,inputtel)
     sinif.append(telebe_obyekti)

def melumatlariDaxilEt():
    say=int(input("Telebe sayini daxil edin: "))
    i=0
    while i<say:
        telebeYarat_listeElaveet()
        i+=1


#ada gore melumatlarin gosterilmesi

def AdaGoreMelumatlariCixar():
    AD=input("melumatlarini gostermek istediyiniz telebenin adini daxil edin: ")
    for j in range(len(sinif)):
        if sinif[j].ad==AD:
            print(f"Kod: {sinif[j].kod}, Ad: {sinif[j].ad}, Soyad: {sinif[j].soyad}, Email: {sinif[j].email}, Tel: {sinif[j].tel}")



#koda gore melumatlarin silinmesi

def KodaGoreMelumatlarinSilinmesi():
    KOD=int(input("Silmek istediyiniz telebenin kodunu yazin: "))
    for k in range(len(sinif)):
        if sinif[k-1].kod==KOD:
            sinif.pop(k-1)
            print("silindi")
            print("Qalan telebeler: ")
            for telebe in sinif:
                telebe.showdata()


#koda gore melumatlarin deyisdirilmesi

def MelematlariDeyisdir():
    deyisdirilenKod=int(input("Melumatlari deyisdirmek istediyiniz telebenin kodunu yazin: "))
    for d in range(len(sinif)):
        if sinif[d].kod==deyisdirilenKod:
            yenikod=int(input("yeni kod: "))
            if 100<yenikod<999:
                pass
            else:
                print("Dogru kodu elave et!")
                yenikod=int(input("Kod: "))
            yeniad=input("yeni ad: ")
            if yeniad.isalpha():
               pass
            else:
                print("Soyad herflerden ibaret olmalidir!")
                yeniad=input("Ad:")
            yenisoyad=input("yeni soyad: ")
            if yenisoyad.isalpha():
                pass
            else:
               print("Ad herflerden ibaret olmalidir!")
               yenisoyad=input("Soyad:")
            yeniemail=input("yeni email: ")
            if "@" in yeniemail:
                pass
            else:
                print("Dogru emaili elave edin!")
                yeniemail=input("Email: ")
            yenitel=input("yeni tel: ")
            if len(yenitel)<10 and yenitel.isdigit():
                 pass
            else:
                 print("Dogru telefon nomresi daxil edin!")
                 yenitel=input("Tel: +994 ")

            sinif[d].kod=yenikod
            sinif[d].ad=yeniad
            sinif[d].soyad=yenisoyad
            sinif[d].email=yeniemail
            sinif[d].tel=yenitel


def telebeMelumatlariniGoster():
     for telebe in sinif:
          telebe.showdata()


print("""
==========================================================================
Aparmaq istediyiniz emeliyyatinnomresini secin:
==========================================================================
0.Proqrami dayandir
1.Qeydiyyat prosesine baslayin
2.Ada gore userin melumatlarini gosterin
3.Koda gore melumatlari silin
4.Koda gore melumatlari silin
5.Butun telebe melumatlarini gosterin
==========================================================================
==========================================================================
""")

while True:
    n =int(input("Emeliyyat nomresini daxil edin: "))
    if n==0:
        print("Tesekkurler")
        break
    elif n==1:
        melumatlariDaxilEt()
    elif n==2:
        AdaGoreMelumatlariCixar()
    elif n==3:
        KodaGoreMelumatlarinSilinmesi()
    elif n==4:
        MelematlariDeyisdir()
    elif n==5:
        telebeMelumatlariniGoster()
    else:
        break

