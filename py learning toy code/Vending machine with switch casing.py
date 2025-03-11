Items_in_machine = [(1, 'monster', 3.50), (2, 'celsius', 4.00), (3, 'coke', 2.50), (4, 'pepsi', 2.00), (5, 'fourloko', 5.00)]
money_inserted = 0

def check_price():
    selection = int(input('Which number item would you like to see the price for?: '))
    if 1 <= selection <= len(Items_in_machine):  
        print('The value of', Items_in_machine[selection - 1][1], 'item number', Items_in_machine[selection - 1][0], 'is $', Items_in_machine[selection - 1][2])
    else:
        print("Invalid item number.")

def insert_money():
    global money_inserted
    money_inserted += float(input('How many dolla blls are you putting in?: '))

def buy_soda():
    global money_inserted
    while True:
        sodie_selection = int(input('Which number sodie is u poppin\' today king: '))
        if 1 <= sodie_selection <= len(Items_in_machine): 
            if money_inserted < Items_in_machine[sodie_selection - 1][2]:
                print('You broke, add more money')
                break
            elif money_inserted >= Items_in_machine[sodie_selection - 1][2]:
                money_inserted = round(money_inserted - Items_in_machine[sodie_selection - 1][2], 2)
                print('You have', money_inserted, 'dollars leftover')
                print('You received a', Items_in_machine[sodie_selection - 1][1], '!!!')
                break
        else:
            print("Invalid soda selection.")

def user_selection(user_input):
    if user_input.lower() not in ["price", "add", "buy", "esc"]:
        print("Invalid input, please enter a valid option (price, add, buy, esc).")
        return
    match user_input.lower():
        case "price":
            check_price()
        case "add":
            insert_money()
        case "buy":
            buy_soda()

def soda_loop():
    print('Welcome to Noah\'s soda machine here are our options for sodas:')
    for itemnumber, itemname, price in Items_in_machine:
        print(f'Item# {itemnumber} - {itemname} for ${price}')

    print("\nEnter 'price' to check the price of an item number")
    print("Enter 'add' to add money")
    print("Enter 'buy' to purchase a soda")
    print("Enter 'esc' to exit\n")

    while True:
        user_input = input('Enter the option you want from the list above: ').lower()
        user_selection(user_input)
        if user_input == 'esc':
            print('Thanks for using Noah\'s vending machine!')
            break

soda_loop()