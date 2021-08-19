import time
import random

def sayı_al():
    sayı_tahmin = int(input("Bir sayı giriniz? "))
    return sayı_tahmin
def oyun_baslat():

    print("""
        *** SAYI TAHMİN OYUNUNA HOŞ GELDİNİZ ***

    """)

dogru_sayı = random.randint(1,100)
while True:
        sayı_tahmin = sayı_al()

        print("Kontrol ediliyor...")
        time.sleep(1)
        if dogru_sayı < sayı_tahmin:
            print("Biraz aşağı gelin")

        elif dogru_sayı > sayı_tahmin:
            print("Biraz yukarı gelin")
        
        else:
            print("\n *** SAYI DOĞRU! ***")
            break