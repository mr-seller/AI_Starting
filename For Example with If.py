moderator = "Ayşe Demir"

kullanici_sayisi = 0
moderator_sayisi = 0

yorum_birakanlar = ["Ali Yıldırım", "Ayşe Demir", "Mehmet Can", "Zeynep Yılmaz", "Seda Kaya", "Emre Çelik"]
for kullanici in yorum_birakanlar:
    kullanici_adi = kullanici.split()[0]
    kullanici_soyadi = kullanici.split()[1]

    if kullanici == moderator:
        moderator_sayisi += 1
        print("{}. Moderatörün Adı: {}, Soyadı: {}".format(kullanici_sayisi, kullanici_adi, kullanici_soyadi))
    else:
        kullanici_sayisi += 1
        print("{}. Kullanıcının Adı: {}, Soyadı: {}".format(kullanici_sayisi, kullanici_adi, kullanici_soyadi))
