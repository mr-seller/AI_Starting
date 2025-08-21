def karesini_al(x):
    return x**2

sayilar = list(range(1, 6))
for index in len(range(sayilar)):
   sayilar[index] = karesini_al(sayilar[index])
print(sayilar)