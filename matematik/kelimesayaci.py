def kelime_sayaci(metin):
    kelimeler = metin.split()
    return len(kelimeler)

def main():
    with open("metin_dosyasi.txt", "r", encoding="utf-8") as dosya:
        icerik = dosya.read()
        kelime_sayisi = kelime_sayaci(icerik)
        print(f"Metindeki Kelime Sayısı: {kelime_sayisi}")

if __name__ == "__main__":
    main()
