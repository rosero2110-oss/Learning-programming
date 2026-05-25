

n1 = int(input("Ingrese un numero:"))

cua = n1 * n1
div = str(cua)
mitad = len(div) // 2
mitad_1 = div[:mitad]
mitad_2 = div[mitad:]
n_1 = int(mitad_1)
n_2 = int(mitad_2)
nk = n_1 + n_2

if nk == n1:    
    print(f"Si, {n_1} + {n_2} = {nk}")
else:
    print("No, no es un número de Kaprekar ")

