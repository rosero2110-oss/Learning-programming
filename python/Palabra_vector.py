palabra = []
def menu(): 
    print("""
    :::Menu principal:::
    [1]. Ingrese palabra
    [2]. Mostrar palabra
    [3]. Mostrar palabra(invertida)
    [4]. Salir""")
    opt = int(input("Seleccione una opcion: "))
    return opt

menu_status = True
while menu_status:
    opt = menu()
    match opt:
        case 1:
            n = int(input("Ingrese el nuemro de letras que contiene la palabra: "))
            palabra = [] * n
            for i in range(n):
                letra = input(f"ingrse la letra {i +1}: ")
                palabra.append(letra)
                key = input("Presione Enter para continuar")
                menu_status = False
                break
