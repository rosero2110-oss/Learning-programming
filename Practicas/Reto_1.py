c = 2
n2 = 1

n1 = int(input("Ingrese el numero: "))

status = True
while status:
        
    if n1 != 1:
        n2 = n2 + c
        n3 = n2
        c +=1
        
        if n1 < c:
            print(n2)
            status = False
            break
    else:
        print("1")
        status = False
        break