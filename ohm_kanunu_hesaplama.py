#elektrik akıma göre direnç bulma
# V=I*R

secenek = input("Ohm Kanunu V=I*R (Gerilim = Akim * Direnc) \n Bulmak istediginiz degeri giriniz: 1)V gerilim 2)I akim 3)R direnc")

if (secenek == "1"):
    akim = float(input("akim degerini giriniz: "))
    direnc = float(input("direnc degerini giriniz: "))
    gerilim = akim * direnc
    print(gerilim)
elif (secenek == "2"):
    gerilim = float(input("gerilim degerini giriniz: "))
    direnc = float(input("direnc degerini giriniz: "))
    akim = gerilim/direnc
    print(akim)
elif(secenek  ==  "3"):
    gerilim = float(input("gerilim degerini giriniz: "))
    akim = float(input("akim degerini giriniz: "))
    direnc= gerilim/akim
    print(direnc)

