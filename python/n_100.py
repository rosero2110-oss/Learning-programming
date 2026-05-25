suma = 0
n3 = 0
n2 = 0
equal_n = 0
anterior_n = None
while suma <= 100:
    n = int(input("Ingrese un numero: "))
    suma += n
    if n == 3:
        n3 += 1
        if n3 > 3:
            print("Has ingresado el numero 3 mas de tres veces, el programa se cerrara")
            break
    if n == 2:
        n2 +=1
        if n2 > 2:
            print("Has ingresado el numero 2 mas de dos veces, el programa se cerrara")
            break
    if n != 2 and n != 3:
        if n == anterior_n:
            equal_n +=1
        else:
            equal_n = 1

        if equal_n > 8:
            print("Has ingresado el mismo numero mas de ocho veces, el programa se cerrara")
            break
    anterior_n = n

