kullanici1 = {
    'ad': 'Ferhat',
    'soyad': 'Ibrik',
    'uzmanlik': ['Front-End']
}
kullanici2 = {
    'ad': 'Gokce',
    'soyad': 'Gün',
    'uzmanlik': ['Tasarim']
}
kullanici3 = {
    'ad': 'Mesut',
    'soyad': 'Gün',
    'uzmanlik': ['Front-End']
}

kullanici3['uzmanlik'].append('Yazilim')
kullanici_listesi = [kullanici1, kullanici2, kullanici3]
kullanici_yaslari_listesi = [22, 34, 32]

for kullanici, yas in zip(kullanici_listesi, kullanici_yaslari_listesi):
    print("Ad: {}, Soyad: {}, Uzmanlik: {}, Yas: {}".format(
        kullanici['ad'], kullanici['soyad'], kullanici['uzmanlik'], yas))