# {note: none}
# McBurger1.py
# JadenJSJ

def debug(text):
    print('\33[90m' + "[debug] " + str(text) + '\33[0m')

burger = [["McChicken",1.20,0],["McBeef",1.40,0],["McCheese",1.00,0],["McFish",1.60,0]]

def FunBurger():
    print("===================\n█ ▀█▀ █▀▀ █▀▄▀█ █▀\n█ ░█░ ██▄ █░▀░█ ▄█\n===================")
    for i in range(len(burger)):
        print(str(i+1) + ". " + burger[i][0] + "\t$" + f'{burger[i][1]:.2f}')
    itemChoise = int(input("Choise: "))
    itemQuantity = int(input("Quantity: "))

    for i in range(len(burger)):
        if itemChoise == i+1:
            burger[i][2] = burger[i][2] + itemQuantity
            break

    main()

def FunCheckout():
    print("---------------------------------------------------")
    print(f'{"Item":12}{"Price":12}{"Quantity":16}{"Total":18}')
    print("---------------------------------------------------")

    for i in range(len(burger)):
        if not burger[i][2] == 0:
            print(f'{burger[i][0]:12}{burger[i][1]:.2f}{burger[i][2]:16}{burger[i][1]*burger[i][2]:18.2f}')

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