print("derse hosgeliniz") #terminale içindeki değeri yazdırı


int_değisken = 0 #değişkene integer değerini atma
string_değisken = "Burak" #değişkene string değerini atma
float_degisken = 3.14 #değişkene float değerini atma
bool_degisken = True #değişkene bool değerini atma


#Mantıksal Operatörler

# Eşittir ==
i = 0 == 3
print(i)

# Eşit değildir !=
i = 0 != 3
print(i)

# Büyüktür >
i = 0 > 3
print(i)

# Küçüktür <
i = 0 < 3
print(i)

# Büyük eşittir >=
i = 0 >= 3

# Küçük eşittir >=
i = 0 <= 3


#Matematiksel Operatörler

# Toplama +
sayi = 1 + 6
print(sayi)

#Not Toplama işlemde string değerleride toplayabilirsiniz
isim = "kerem" + "ali"
print(isim)

# Çıkarma -
sayi = 1 - 6
print(sayi)

# Çarpma *
sayi = 1 * 6
print(sayi)

# Bölme /
sayi = 1 / 6
print(sayi)

# Tam Bölme //
sayi = 1 // 6
print(sayi)

# Üs Alma **
sayi = 2 ** 6
print(sayi)

# Mod %
sayi = 2 % 6
print(sayi)


# Python’da kullanıcıdan herhangi bir veri alıp, yazdığımız programları tek taraflı olmaktan kurtarmak için input() adlı bir fonksiyondan faydalanıyoruz.
s = input("Lütfen bir sayi giriniz: ")
print(s)


# Veri türünü değiştirmek için int(), str(), float(), bool() adlı fonksiyonlardan faydalanıyoruz.
sayi = "34"

sayi = int(sayi)
print(sayi)

sayi = float(sayi)
print(sayi)

sayi = str(sayi)
print(sayi)

sayi = bool(sayi)
print(sayi)


# Kullanıcıdan 2 değer alıp bu iki değeri toplayan ve terminale yazan uygulama
sayi1 = input("Toplama işlemi için ilk sayıyı girin: ")
sayi2 = input("Toplama işlemi için ikinci sayıyı girin: ")
sayi1 = int(sayi1)
sayi2 = int(sayi2)
print(sayi1, "+", sayi2, "=", sayi1 + sayi2)


# Kullanıcıdan 2 değer alıp birinci değeri ikinci değerden çıkartan ve terminale yazan uygulama
sayi1 = input("Toplama işlemi için ilk sayıyı girin: ")
sayi2 = input("Toplama işlemi için ikinci sayıyı girin: ")
sayi1 = int(sayi1)
sayi2 = int(sayi2)
print(sayi1, "-", sayi2, "=", sayi1 - sayi2)


# Kare Alan ve Çevre Hesaplama
kenar=int(input("Kenar uzunluğunu giriniz:"))
cevre=kenar*4
alan=kenar**2
print("Karenin Çevresi:", cevre)
print("Karenin Alanı:", alan)


# Girilen Saniye Değerini Saate Dönüştürme
saniye=int(input("Saniye Giriniz:"))
saat=saniye//3600
saniye=saniye%3600
dakika=saniye//60
saniye=saniye%60
print("Girdiğiniz Saniyenin Saat Dönüşümü:",saat,"sa",dakika,"dk",saniye,"sn")


#İf-Else-Elif

# İf bloğu programımızın içinde herhangi bir yerde belli bir koşulu kontrol edecek isek kullanılan bloklardır.

yas = int(input("Yaşınızı giriniz: "))

if yas >= 18:
    print("Ehliyet alabilirsiniz")


# Else blokları if koşulu sağlanmadığı zaman (False) çalışan bloklardır.

yas = int(input("Yaşınızı giriniz: "))

if yas >= 18:
    print("Ehliyet alabilirsiniz")
else:
    print("Ehliyet alamazsınız")


# Elif blokları if koşulu sağlanmadığı zaman (False) yeni bir sorgu yapmamızı sağlayan bloklardır.

islem = int(input("Yaşınızı giriniz: "))

if islem == 1:
    print("1. islem")
elif islem == 2:
    print("2. islem")
elif islem == 3:
    print("3. islem")
else:
    print("böylebir işlem bulunamadı!")



#İki sayı karşılaştırma

a=int(input("1. Sayıyı Giriniz: "))
b=int(input("2. Sayıyı Giriniz: "))
if a>b:
 print("Birinci sayı büyük!")
elif a<b:
 print("İkinci sayı büyük!")
else:
 print("Sayılar eşit!")


# Takdir&Teşekkür Durumu
 ortalama = float(input("Not ortalamanızı giriniz: "))
 if ortalama >= 85:
     print("Takdir Belgesi Alamaya Hak Kazandınız!")
 elif ortalama >= 70:
     print("Teşekkür Belgesi Alamaya Hak Kazandınız!")
 elif ortalama >= 50:
     print("Sınıfı Geçtiniz")
 else:
     print("Sınıf tekrarı...")