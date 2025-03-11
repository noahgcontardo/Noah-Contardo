#
Items_in_machine = [(1, 'monster', 3.50), (2, 'celsius', 4.00), (3, 'coke', 2.50), (4, 'pepsi', 2.00), (5, 'fourloko', 5.00)]
money_inserted = 0
#
def check_price():
    selection = int(input('Which number item would you like to see the price for?: '))    
    print('The value of',Items_in_machine[selection][1], 'item number',Items_in_machine[selection][0], 'is $',Items_in_machine[selection][2])
#
def insert_money():
    global money_inserted
    money_inserted += float(input('how many dolla blls are you putting in?: '))
#
def buy_soda():
    global money_inserted
    while True:
        sodie_selection = int(input('Which number sodie is u poppin\' today king: '))
        if money_inserted < Items_in_machine[sodie_selection - 1][2]:
            print('you broke add more money')
            break
        elif money_inserted >= Items_in_machine[sodie_selection - 1][2]:
            money_inserted = round(money_inserted - Items_in_machine[sodie_selection - 1][2], 2)
            print('you have', money_inserted, 'dollars leftover')
            print('you received a ', Items_in_machine[sodie_selection - 1][1],'!!!')
            break

def soda_loop():
    print('welcome to noah\'s soda machine here are our options for sodas:')
    for itemnumber, itemname, price in Items_in_machine:
        print('here are the items we have in the vending machine','item# ',itemnumber,'item name', itemname)

    while True:
        print('enter 1 to see item price')
        print('enter 2 to insert money')
        print('enter 3 to purchase an item')
        user_input = int(input('press 4 to quit: '))
        if user_input == 1:
            check_price()
        elif user_input == 2:
            insert_money()
        elif user_input == 3:
            buy_soda()
        elif user_input == 4:
            print("Enjoy ur soda")
            break
        else:
            print("------Something went wrong try again------")
            continue
soda_loop()