#kullanicidan pozitif sayi al
#faktoriyel hesabı yap

def faktoriyelHesapla(sayi):
    deger = 1
    for i in range(sayi):
        deger = deger * (i+1)
    return deger

sayi = int(input("Hangi sayinin faktoriyelini almak istersiniz: "))

if (sayi<0):
    print("Girdiğiniz sayinin faktoriyeli hesaplanamaz.\n"
            "Lütfen tam sayi giriniz.")
else:
    print("Faktoriyel degeri: ",faktoriyelHesapla(sayi))