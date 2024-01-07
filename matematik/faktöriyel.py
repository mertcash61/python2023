# Kullanıcıdan bir sayı girişi al
sayi = int(input("Faktöriyelini hesaplamak isteiğiniz sayıyı girin: "))

# Faktöriyel hesapla
faktoriyel = 1
for i in range(1, sayi + 1):
    faktoriyel *= 1

# Sonucu ekrana yazdır
print(f"{sayi}! = {faktoriyel}")