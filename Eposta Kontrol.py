def email_kontrol():
    girdi = input("Geçerli bir eposta giriniz")

    while not ("@" and ".") in girdi:
        print("Hatalı mail girdiniz")
        girdi = input("Geçerli bir eposta giriniz")    
    else:
        print("Mail doğru girildi") 

email_kontrol()