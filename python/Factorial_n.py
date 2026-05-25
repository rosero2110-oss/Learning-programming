
n = int(input("Ingrese un numero para calcular su factorial: "))
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1) 
print(f"El factorial de {n} es: {factorial(n)}")
print(factorial(n-1))
