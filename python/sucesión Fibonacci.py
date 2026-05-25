i = 0
n1 = 0
n2 = 1
print(n1)
while i < 20:
    secuencia = n1 + n2
    n1 = n2
    n2 = secuencia
    print(secuencia)
    i += 1