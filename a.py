def factorial (number):
    factorial=1
    for i in range(1, number + 1):
        factorial *= i
    return("{}! eşittir {}".format(number, factorial))

number = int(input("Bir numara giriniz"))



a = factorial(number)
print (a)