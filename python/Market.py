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
                print(f"{product_code[i]}   | {product_name[i]} | {product_quantity[i]} | {unit_value_product[i]}")
                i +=1
            key = input("Press Enter for continue...")
        case 5:
            os.system("clear")
            print("### Search client by identification ###")
            
            search_id = input("Enter client identification\n")

            if search_id in client_id:
                i = client_id.index(search_id)

                print("\n### Client Found ###")
                print(f"Identification: {client_id[i]}")
                print(f"Full name: {client_name[i]}")
                print(f"Address: {client_address[i]}")
                print(f"Phone number: {client_phone[i]}")
                print(f"Email: {client_email[i]}")
                print(f"Gender: {client_gender[i]}")
                print(f"Age: {client_age[i]}")
            else:
                print("Client not found")

            key = input("\nPress Enter to continue...")
        case 6:
            os.system("clear")
            print("### Search product by code ###")
            
            search_code = input("Enter the code of product\n")

            if search_code in product_code:
                i = product_code.index(search_code)

                print("\n### Product Found ###")
                print(f"Code: {product_code[i]}")
                print(f"Product name: {product_name[i]}")
                print(f"Quantity: {product_quantity[i]}")
                print(f"Unit value of the product: {unit_value_product[i]}")

            else:
                print("Product not found")

            key = input("\nPress Enter to continue...")
        case 7:
            os.system("clear")
            print("### Update Client ###")

            search_id = input("Enter client identification: ")

            if search_id in client_id:
                i = client_id.index(search_id)

                print("\nCurrent data:")
                print(f"Name: {client_name[i]}")
                print(f"Address: {client_address[i]}")
                print(f"Phone: {client_phone[i]}")
                print(f"Email: {client_email[i]}")
                print(f"Gender: {client_gender[i]}")
                print(f"Age: {client_age[i]}")

                print("\nEnter new data")

                client_name[i] = input("New full name: ")
                client_address[i] = input("New address: ")
                client_phone[i] = input("New phone number: ")
                client_email[i] = input("New email: ")
                client_gender[i] = input("New gender: ")
                client_age[i] = input("New age: ")

                print("\nClient updated successfully!")

            else:
                print("Client not found")

            key = input("\nPress Enter to continue...")
        case 8:
            os.system("clear")
            print("### Update Product ###")

            search_code = input("Enter the code of product\n")

            if search_code in product_code:
                i = product_code.index(search_code)

                print("\n### Product Found ###")
                print(f"Code: {product_code[i]}")
                print(f"Product name: {product_name[i]}")
                print(f"Quantity: {product_quantity[i]}")
                print(f"Unit value of the product: {unit_value_product[i]}")


                print("\nEnter new data")

                product_code[i] = input("New code: ")
                product_name[i] = input("New name: ")
                product_quantity[i] = input("New quantity of the product: ")
                unit_value_product[i] = input("Unit value of the product: ")

                print("\nClient updated successfully!")

            else:
                print("Product not found")

            key = input("\nPress Enter to continue...")
        case 9:
            os.system("clear")
            print("### Delete Client ###")

            search_id = input("Enter client identification: ")

            if search_id in client_id:
                i = client_id.index(search_id)

                print("\nClient found:")
                print(f"{client_id[i]} - {client_name[i]}")

                confirm = input("Are you sure you want to delete this client? (yes/no): ")

                if confirm.lower() == "yes":

                    client_id.pop(i)
                    client_name.pop(i)
                    client_address.pop(i)
                    client_phone.pop(i)
                    client_email.pop(i)
                    client_gender.pop(i)
                    client_age.pop(i)

                    print("\nClient deleted successfully!")

                else:
                    print("Operation cancelled")

            else:
                print("Client not found")

            key = input("\nPress Enter to continue...")
        case 10:
            os.system("clear")
            print("### Delete Product ###")

            search_code = input("Enter product code: ")

            if search_code in product_code:
                i = product_code.index(search_code)

                print("\nProduct found:")
                print(f"{product_code[i]} - {product_name[i]}")

                confirm = input("Are you sure you want to delete this product? (yes/no): ")

                if confirm.lower() == "yes":

                    product_code.pop(i)
                    product_name.pop(i)
                    product_quantity.pop(i)
                    unit_value_product.pop(i)

                    print("\nProduct deleted successfully!")

                else:
                    print("Operation cancelled")

            else:
                print("Product not found")

            key = input("\nPress Enter to continue...")
        case 11:
            print("Exiting the program...\n Bye, bye!")
            menu_status = False
            break
        case _:
            print("Invalid option, try again")
            os.system("pause")
