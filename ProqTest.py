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
     inputtel=input("Tel: 994 ")
     if len(inputtel)<10 and inputtel.isdigit():
         pass
     else:
         print("Dogru telefon nomresi daxil edin!")
         inputtel=input("Tel: 994 ")

     telebe_obyekti=Telebe(inputkod, inputad,inputsoyad,inputemail,inputtel)
     sinif.append(telebe_obyekti)
i=1
while i<4:
    telebeYarat_listeElaveet()
    i+=1

for telebe in sinif:
    telebe.showdata()

#ada gore melumatlarin gosterilmesi
AD=input("melumatlarini gostermek istediyiniz telebenin adini daxil edin: ")
def AdaGoreMelumatlariCixar(sert):
    for j in range(len(sinif)):
        if sert(sinif[j].ad):
            print(sinif[j].kod, sinif[j].ad, sinif[j].soyad, sinif[j].email, sinif[j].tel)

AdaGoreMelumatlariCixar(lambda x: x==AD)

#koda gore melumatlarin silinmesi
KOD=int(input("Silmek istediyiniz telebenin kodunu yazin: "))
def KodaGoreMelumatlarinSilinmesi(sert):
    for k in range(len(sinif)):
        if sert(sinif[k-1].kod):
            sinif.pop(k-1)
            print("silindi")
            print("Qalan telebeler: ")
            for telebe in sinif:
                telebe.showdata()
KodaGoreMelumatlarinSilinmesi(lambda Kod: Kod==KOD)

#koda gore melumatlarin deyisdirilmesi
deyisdirilenKod=int(input("Melumatlari deyisdirmek istediyiniz telebenin kodunu yazin: "))
def MelematlariDeyisdir(sert):
    for d in range(len(sinif)):
        if sert(sinif[d].kod):
            yenikod=int(input("yeni kod: "))
            yeniad=input("yeni ad: ")
            yenisoyad=input("yeni soyad: ")
            yeniemail=input("yeni email: ")
            yenitel=input("yeni tel: ")
            sinif[d][0]=yenikod
            sinif[d][1]=yeniad
            sinif[d][2]=yenisoyad
            sinif[d][3]=yeniemail
            sinif[d][4]=yenitel
MelematlariDeyisdir(lambda z: z==deyisdirilenKod)
print(sinif)
