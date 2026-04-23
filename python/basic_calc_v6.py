'''
this is a calculator where you have the possibility of selec between differents operations
'''

# ask the user to enter two numbers

num1 = float(input("Please, enter first number: "))
num2 = float(input("Please, enter second number: "))

# menu of options

def main_menu ():

    while True:
        operations = print( """
    Selecciona la operación que quieres realizar
    (1) Suma
    (2) Resta
    (3) Multiplicación
    (4) División
    (5) Promedio
    (6) Todas las operaciones
    """)
    operations = int(input ("Elige una opción: "))

main_menu()

match operations:
    case 1:
        add = num1 + num2
        print (f"la suma es: {add}")
    case 2:
        subs = num1 - num2
        print (f"la resta es; {subs}")
    case 3: 
        mult = num1 * num2
        print (f"la multiplicación es: {mult}")
    case 4:
        div = num1 / num2
        print(f"La división es: {div}")
    case 5:
        prom = (num1 + num2) / 2
        print(f"El promedio es: {prom}")
    case 6:
        add = num1 + num2
        subs = num1 - num2
        mult = num1 * num2
        prom = (num1 + num2) / 2
        print (f"la suma es: {add}")
        print (f"la resta es; {subs}")
        print (f"la multiplicación es: {mult}")
        print(f"La división es: {div}")
        print(f"El promedio es: {prom}")
    case _:
        print("opcion invalda, intenta de nuevo")