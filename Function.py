def buyuk_sayi_dondur(a, b):
    if a > b:
        return(a)
    elif b>a:
        return(b)
    else:
        return("Eşit sayı girdiniz.")



def metin_dondur(a, b):
    buyuk_sayi = buyuk_sayi_dondur (a, b)
    sablon_metin = "{} daha büyük sayıdır.".format(buyuk_sayi)
    print(sablon_metin)

metin_dondur(15, 10)