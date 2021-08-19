def ekok(sayi1,sayi2):
    #en büyük ekok değeri ikisinin çarpımıdır.
    ekok = sayi1*sayi2

    for i in range (ekok, max(sayi1,sayi2)-1,-1):
        if i % sayi1 == 0 and i % sayi2 == 0:
            ekok = i
    return ekok

birinciSayi = int(input("Birinci sayiyi giriniz: "))
ikinciSayi = int(input("ikinciSayi sayiyi giriniz: "))

print(ekok(birinciSayi,ikinciSayi))
