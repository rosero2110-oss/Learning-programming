#Impot libraries

import os

# Initialize the variables or constants

client_id = []
client_name = []
client_address = []
client_phone = []
client_email = []
client_gender = []
client_age = []

product_code = []
product_name = []
product_quantity = []
unit_value_product = []

option = 0

# Main menu

os.system("clear")
def main_menu():
    option = print("""
    Select the option:
    [1] Register client
    [2] Register product
    [3] list clients 
    [4] list products
    [5] Search client by ident
    [6] Search product by code
    [7] Update client
    [8] Update product
    [9] Delete client
    [10] Delete product
    [11] Exit """)
    option = int(input("Select any option: "))
    return option

# Main
menu_status = True
while menu_status:
    option = main_menu()

    match option:
        case 1:
            os.system("clear")
            print("### New Client ###")
            ident = input("Client identification: ")
            client_id.append(ident)
            full_name = input("Client full name: ")
            client_name.append(full_name)
            address = input("Client address: ")
            client_address.append(address)
            phone = input("Client phone number: ")
            client_phone.append(phone)
            email = input("Client email: ")
            client_email.append(email)
            gender = input("Client gender: ")
            client_gender.append(gender)
            age = input("Client age: ")
            client_age.append(age)
            print("Client has been registered successfully !")
            key = input("Press Enter to continue...")
        case 2:
            os.system("clear")
            print("### New Product ###")
            code = input("Product code: ")
            product_code.append(code)
            name = input("Name of the product: ")
            product_name.append(name)
            quantity = input("Quantity of the product: ")
            product_quantity.append(quantity)
            value = input("Unit value of the product: ")
            unit_value_product.append(value)
            print("The product has been registered succesfully !")
            key = input("Press Enter for continue...")
        case 3:
            os.system("clear")
            print("### List of clients ###")
            i = 0
            while i < len(client_name):
                print(" IDENTIFICATION | FULL NAME | ADDRESS | PHONE NUMBER | EMAIL | GENDER | AGE ")
                print(f"{client_id[i]}  | {client_name[i]} | {client_address[i]} | {client_phone[i]} | {client_email[i]} | {client_gender[i]} | {client_age[i]}")
                i +=1
            key = input("Press Enter for continue...")
        case 4:
            os.system("clear")
            print("### List of products ###")
            i = 0
            while i < len(product_name):
                print(" CODE | NAME | QUANTITY | UNIT VALUE ")
                print(f"{product_code[i]}  | {product_name[i]} | {product_quantity[i]} | {unit_value_product[i]}")
                i +=1
            key = input("Press Enter for continue...")

        case 11:
            print("Exiting the program...\n Bye, bye!")
            menu_status = False
            break
        case _:
            print("Invalid option, try again")
            os.system("pause")
