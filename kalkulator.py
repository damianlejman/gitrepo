suma = 0
kontrolna = -1
peselchk = [1,3,7,9,1,3,7,9,1,3]
try:
    pesel = input()
    kontrolna = int(pesel[10])
    for i in range(10):
        suma += peselchk[i] * int(pesel[i])
    reszta = 10 - (suma % 10)
    if reszta != 10:
        if kontrolna == reszta:
            print("1")
        else:
            print("0")
    else:
        if kontrolna == 0:
            print("1")
        else:
            print("0")
except ValueError:
    print("0")
#
#
#tutaj jakies inne zmiany
#
#
