#problem vize ve final notunu alıp geçip geçmeyeceğini 
#hesapla ve text dosyasına kaydet.
ogrenci = input("Ogrenci adi ve soyadi: ")

vize = float(input("Vize notunuzu girin: "))
final = float(input("Final notunuzu girin: "))

durum = (vize*0.4) + (final*0.6)
harf_notu = ""

if(85<=durum<=100):
    harf_notu = "AA"
elif (70<=durum):
    harf_notu = "BA"
elif (60<=durum):
    harf_notu = "BB"
elif (50<=durum):
    harf_notu = "CB"
elif (40<=durum):
    harf_notu = "CC"
else:
    harf_notu = "FF"

print("Basari Notu: ", durum)
print("{} isimli ograncinin harf notu {}"
        .format(ogrenci,harf_notu))
# w yazarsan text dosyasını siler a yazarsan üzerine yazars
with open("notlar.txt","a") as dosya:
    dosya.writelines("{} isimli ograncinin basari notu {}, harf notu {} \n"
                    .format(ogrenci,durum,harf_notu))

