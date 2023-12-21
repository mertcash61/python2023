import requests
from bs4 import BeautifulSoup

def web_verisi_cek(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as err:
        print(f"Hata: {err}")
        return None

def basliklari_getir(web_verisi):
    soup = BeautifulSoup(web_verisi, 'html.parser')
    basliklar = soup.find_all('h2')
    return [baslik.text.strip() for baslik in basliklar]

def main():
    url = "https://www.example.com"
    web_verisi = web_verisi_cek(url)

    if web_verisi:
        basliklar = basliklari_getir(web_verisi)
        for i, baslik in enumerate(basliklar, start=1):
            print(f"{i}. Başlık: {baslik}")

if __name__ == "__main__":
    main()