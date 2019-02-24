import random
n = int(input("Maksimal təxmin etmə şansını daxil edin:->"))
number = random.randint(1, 99)
s = n

while n >= s > 0:
    texmin = int(input("Eded daxil edin"))
    s = s - 1
    if texmin == number:
        print("Tebrikler dogru texmin elediniz")
        break

    elif texmin < number and s > 0 :
        print("Daha boyuk daxil edin")

    elif texmin > number and s > 0:
        print("Daha kicik eded daxil edin")

    else:
        print("****************************\nSansiniz bitdi....\nTeessufki uduzdunuz:")
