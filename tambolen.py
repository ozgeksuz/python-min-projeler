def tamSayiBolenleriAl(sayi):
    bos =[]
    for i in range (1,sayi):
        if sayi % i == 0:
            bos.append(i)
    return bos

sayi1=int(input("Bir sayi giriniz: "))
print("Tam bölenler: ",tamSayiBolenleriAl(sayi1))