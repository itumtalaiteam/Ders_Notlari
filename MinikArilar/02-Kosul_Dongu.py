# pi = 3.14
# pi = 3 + 0.14

# yasimiz = 16
# print(pi+yasimiz)


# yasim = 18
# ehliyet_alabilir_miyim = yasim >= 18
# genc_miyim = yasim < 25
# print(ehliyet_alabilir_miyim)
# print(genc_miyim)

# print("yasinizi girer misiniz?")
# yas = input()
# # yas = "16"
# yas = int(yas) # yas = 16


# on_yil_sonrasinin_yasi = yas + 10

# print(on_yil_sonrasinin_yasi)


# kullanici_adi = "ardakahriman"
# sifrem = "itumtal"

# # print("sifrenizi giriniz")
# girilen_kullanici_adi = input("kullanici adinizi giriniz: ")
# girilen_sifre = input("sifrenizi giriniz: ")

# kullanici_adlari_esit_mi = "ardakahriman" == "ardakahriman"
# sifreler_esit_mi = "itumtal" == "girilen_sifre"

# ikisinin_kontrolu = kullanici_adlari_esit_mi and sifreler_esit_mi



# print(ikisinin_kontrolu)




# kontrol = True and True => True
# kontrol = True and False => False
# kontrol = False and True => False
# kontrol = False and False => False

# en_sevdigin_renk = input("en sevdigin rengi soyle: ")

# kontrol = en_sevdigin_renk == "pembe" or  en_sevdigin_renk == "mavi"


# print(kontrol)




# kullanici_adi = "ardakahriman"
# sifrem = "itumtal"


# girilen_kullanici_adi = input("kullanici adinizi giriniz: ")
# girilen_sifre = input("sifrenizi giriniz: ")

# kullanici_adlari_esit_mi = girilen_kullanici_adi == kullanici_adi
# sifreler_esit_mi = girilen_sifre == sifrem

# ikisinin_kontrolu = kullanici_adlari_esit_mi and sifreler_esit_mi


# if ikisinin_kontrolu:
#     print("Hosgeldin",kullanici_adi)
# else:
#     print("sifren yada kullanici adin hatali")


# sayi1 = input("bir sayi giriniz: ")
# sayi1 = int(sayi1)

# kalan = sayi1 % 2

# if kalan == 0:
#     print("girilen sayi cifftir")
# else:
#     print("sayi tektir")


# sayi1 = input("sayiyi girin: ")


# sayi1 = int(input("sayiyi girin: "))

# if sayi1>0:
#     print("pozitif")
# elif sayi1<0:
#     print("negatif")
# else:
#     print("sayi sifirdir")


#sayac = 0


# while sayac < 3:
#     print("merhaba",sayac)
#     sayac = sayac + 1

# print("dongu sonlandi")

# kullanıcı_adı = "itü"
# kullanıcı_şifresi = "1234"

# while True:
#     girilen_ad = input("Kullanıcı adı giriniz: ")
#     girilen_şifre = input("Kullanıcı Şifresi Giriniz: ")
#     if girilen_ad == kullanıcı_adı and girilen_şifre == kullanıcı_şifresi:
#         print("Hoş geldiniz")
#         break
#     else: 
#         print("Tekrar dene")

# sonuc = 1

# sayi = int(input("sayiyi giriniz: "))


# while sayi>1:
#     sonuc = sonuc * sayi
#     sayi = sayi - 1
# print(sonuc)



sayaç = 1

sayi = int(input("sayiyi giriniz: "))


while sayaç <= sayi:
    if (sayaç % 3 == 0) and (sayaç % 5 == 0):
        print("FizzBuzz ", sayaç)
    elif(sayaç % 3 == 0):
        print("Fizz ", sayaç)
    elif(sayaç % 5 == 0):
        print("Buzz ", sayaç)

# listeler
# for dongusu
# fonksiyonlar
#  min, max fonksiyonları




