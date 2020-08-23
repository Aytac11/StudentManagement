#yeni telebe elave edilmesi
telebe = []
telebeSayi = 0
while telebeSayi<2:
    kod = input("Telebe kodunu elave edin: ")
    while True:
        if len(kod)==3 and kod.isdigit():
            break
        else:
            kod = input("Telebe kodunu elave edin: ")
    ad = input("Telebe adini daxil edin:  ")
    soyad = input("Telebe soyadini daxil edin:  ")
    while True:
        email = input("Telebe emaili daxil edin: ")
        if ("@" in email):
            break
        else:
            print(email)
    telefon = input("Telebenin telefon nomresini daxil edin: ")
    while True:
        if len(telefon)==9 and telefon.isdigit():
            telefon="+994" +telefon
            break
        else:
            telefon = input("Telebenin telefon nomresini daxil edin:")
    telebeSayi+=1
    telebe+=[[kod, ad,soyad,email,telefon]]


#Ada gore melumatlarin gosterilmmesi
tapilanAd = input("Telebe melumatlarini elde etmek ucun adini daxil edin:")
for i in range(len(telebe)):
    telebeMelumati = telebe[i][1]
    if telebeMelumati==tapilanAd:
        for j in range(4):
            print(telebe[i][j])

#telebe melumatlari
print("Butun telebeleri goster")
telebeList = " "
for a in range(len(telebe)):
    for b in range(len(telebe[a])):
        telebeList+=telebe[a][b]+ "     "
    print(telebeList)
    telebeList = " "

# Telebe melumatarinin deyisdirilmesi
print(telebe)
tapKod = input("Melumatlari deyisdirmek istediyiniz telebenin kodunu daxil edin: ")
for i in range(len(telebe)):
    telebeKod = telebe[i][0]
    if telebeKod==tapKod:
            yeniAd = input("Yeni telebenin adını daxil edin: ")
            yeniSoyad = input("Yeni telebenin soyadini daxil edin: ")
            while True:
                yeniEmail = input("Yeni telebenin emaili daxil edin: ")
                if ("@" in email):
                    break
                else:
                    print(email)
            yeniTelefon = input("Yeni telebenin telefon nomresini daxil edin: ")
            while True:
                if telefon.isdigit():
                    telefon="+994" +telefon
                    break
                else:
                    telefon = input("Yeni telebenin telefon nomresini daxil edin:")
            telebe[i][1] = yeniAd
            telebe[i][2] = yeniSoyad
            telebe[i][3] = yeniEmail
            telebe[i][4] = yeniTelefon
print(telebe)
