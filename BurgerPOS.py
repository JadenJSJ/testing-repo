# {note: none}
# McBurger1.py
# JadenJSJ

def debug(text):
	print('\33[90m' + "[debug] " + str(text) + '\33[0m')

burger = [["McChicken",1.20,0],["McBeef",1.40,0],["McCheese",1.00,0]]

def FunBurger():
    print("===================\n█ ▀█▀ █▀▀ █▀▄▀█ █▀\n█ ░█░ ██▄ █░▀░█ ▄█\n===================\n1. McChicken\t$1.20\n2. McBeef\t$1.40\n3. McCheese\t$1.00\n")
    itemChoise = int(input("Choise: "))
    itemQuantity = int(input("Quantity: "))

    if itemChoise == 1:
        burger[0][2] = burger[0][2] + itemQuantity
    
    elif itemChoise == 2:
        burger[1][2] = burger[1][2] + itemQuantity

    elif itemChoise == 3:
        burger[2][2] = burger[2][2] + itemQuantity

    main()

def FunCheckout():
    print("---------------------------------------------------")
    print(f'{"Item":12}{"Price":12}{"Quantity":16}{"Total":18}')
    print("---------------------------------------------------")
    if not burger[0][2] == 0:
        print(f'{burger[0][0]:12}{burger[0][1]:.2f}{burger[0][2]:16}{burger[0][1]*burger[0][2]:18.2f}')

    if not burger[1][2] == 0:
        print(f'{burger[1][0]:12}{burger[1][1]:.2f}{burger[1][2]:16}{burger[1][1]*burger[1][2]:18.2f}')

    if not burger[2][2] == 0:
        print(f'{burger[2][0]:12}{burger[2][1]:.2f}{burger[2][2]:16}{burger[2][1]*burger[2][2]:18.2f}')

    print("---------------------------------------------------")
    print("Total Purchase: " + f'{burger[0][1]*burger[0][2] + burger[1][1]*burger[1][2] + burger[2][1]*burger[2][2]:.2f}')

def main():
    print()
    print("Welcome to")
    print("█▀▄▀█ █▀▀   █▄▄ █░█ █▀█ █▀▀ █▀▀ █▀█")
    print("█░▀░█ █▄▄   █▄█ █▄█ █▀▄ █▄█ ██▄ █▀▄")
    print("===================================")
    print("1. Items")
    print("2. Checkout")

    choise = int(input("Choise: "))
    print()

    if choise == 1:
        FunBurger()


    if choise == 2:
        FunCheckout()

main()