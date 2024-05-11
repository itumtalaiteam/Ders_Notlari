# 12

# 12 1'e tam bolunur
# 12 2'e tam bolunur
# 12 3'e tam bolunur
# 12 4'e tam bolunur
# 12 6'e tam bolunur
# 12 12'e tam bolunur


# toplam tam bolen sayisi: 6

# sayi = int(input("sayiyi giriniz: "))
# sayac = 1
# bolen_sayisi = 0

# karekok = sayi**0.5
# if  karekok== int(karekok):
#     bitis_noktasi = int(karekok)
# else:
#     bitis_noktasi = int(karekok)+1



# while sayac <= bitis_noktasi:
#     if sayac == karekok:
#         print(sayi, sayac, "'e tam bolunur ve bu sayi girilen sayinin karekokudur")
#         bolen_sayisi += 1
#     elif sayi % sayac == 0:
#         print(sayi, sayac, "'e tam bolunur")
#         print(sayi,int(sayi/sayac), "'e tam bolunur")

#         bolen_sayisi += 2
    
#     sayac = sayac + 1
    
# print("toplam tam bolen sayisi:", bolen_sayisi)



# for sayac in range(1,10,1):
#     print(sayac)

# for sayac in range(1,10+1,1):
#     print(sayac,sayac**2)

# sayac = 0

# while True:
#     sayac +=1 
    
#     if sayac==5:
#         continue
#     print(sayac)
#     if sayac>10:
#         break




# burak = ["burak","berber",101,True,"11A"]
# print(burak)

# burak.append("Rize")
# print(burak)

# burak.insert(2,"10A")
# print(burak)

# print(burak[0])

# siniftaki_elemanlar = []
# siniftaki_elemanlar.append("ayse")
# siniftaki_elemanlar.append("asilbike")
# siniftaki_elemanlar.append("burak")
# siniftaki_elemanlar.append("kerem")
# siniftaki_elemanlar.append("yavuz")
# print(siniftaki_elemanlar)

# siniftaki_elemanlar.insert(3,"halit")
# print(siniftaki_elemanlar)
# siniftaki_elemanlar.remove("kerem")
# print(siniftaki_elemanlar)

# siniftaki_elemanlar.pop(2)
# print(siniftaki_elemanlar)

# sayilar = []

# for sayi in range(1,11,1):
#     sayilar.append(sayi)
#     print(sayilar)

# print(sayilar)


# def selamlama(isim):
#     print("merhaba", isim)

# selamlama("Burak")

# def on_ile_topla(sayi):
#     sayi += 10
#     print(sayi)

# on_ile_topla(30)

# def on_ile_topla(sayi):
#     sayi += 10
    
#     return sayi

# deger = on_ile_topla(10)
# print(deger)


def adSoyad(ad,soyad):
    return ad+soyad

deger = adSoyad("Burak","Berber")

print(deger)


