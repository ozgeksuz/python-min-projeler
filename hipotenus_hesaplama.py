#üçgenin hipotenüsünü hesapla   
def hipotenusHesapla(karsi,komsu):
    hipotenus = ((karsi**2) + (komsu**2)) ** 0.5
    print("Hipotenus degeri: ",hipotenus)
    return hipotenus

karsi = float(input("Karsi degeri giriniz: "))
komsu = float(input("Komsu degeri giriniz: "))
hipotenusHesapla(karsi,komsu)