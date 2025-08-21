def tam_sayiya_cevir():
    girdi = input("Bir ondalık sayı giriniz")
    

    try:
        girdi = float(girdi)
        print("Yuvarlama işleminin sonucu{}".format(round(girdi)))
    except:
        print(girdi, "değeri ondalık değere çevrilemiyor.")

tam_sayiya_cevir()