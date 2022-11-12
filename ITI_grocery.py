import os
import time

stock = {
    'items': ['Apple', 'Banana', 'Orange'],
    'qty': [10, 40, 35],
    'price': [10, 5, 3]
}
print('Wellcome to ITI shop')
time.sleep(1)
cart = []
password = '123'
pass_trials = 3
sys_on = True


while sys_on:
    os.system('cls')
    mode = input('''Select mode:
1   Owner
2   Customer
e   to exit\n''').strip().lower()

    if mode == 'e':
        sys_on = False
        os.system('cls')
        print('.......Thank you.......')
        time.sleep(2)

    elif mode == '1':
        buff = input('Enter password:\n').strip()
        go_in = True
        while pass_trials > 0 and go_in:
            if buff != password:
                print('Wrong password !\nTry again.')
                pass_trials -= 1
                time.sleep(1)
                os.system('cls')

            else:
                os.system('cls')
                while True:

                    print('Hello..')
                    buff = input('''1   List items
2   Add item
3   Edit item
4   Change password\n
e   Exit\n''').strip().lower()

                    if buff == '1':
                        os.system('cls')
                        print('Item\t\t\t\tPrice\t\tQty')
                        for n in range(0, len(stock['items'])):
                            print('{}\t\t\t\t{}\t\t{}'.format(
                                stock['items'][n], stock['price'][n], stock['qty'][n]))
                        print('-'*50)

                    elif buff == '2':
                        os.system('cls')
                        name = input('Enter item\'s name : ').strip()
                        price = float(
                            input('Enter price of 1 item : ').strip())
                        qty = int(input('Enter quantity : ').strip())
                        stock['items'].append(name)
                        stock['price'].append(price)
                        stock['qty'].append(qty)
                        print('item was added')
                        time.sleep(2)
                        os.system('cls')

                    elif buff == '3':
                        os.system('cls')
                        for item in stock['items']:
                            n = stock['items'].index(item)
                            print('{}\t{}'.format(n+1, item))
                        index = int(input('Choose item to edit\n').strip())-1
                        all_item = False
                        edit = input('''would you like to edit:
1   item\'s name
2   item\'s price
3   item\'s qty
4   whole item\n''').strip()
                        if edit == '4':
                            all_item = True
                        if edit == '1' or all_item:
                            stock['items'][index] = input(
                                'Enter new name : ').strip()
                        elif edit == '2' or all_item:
                            stock['price'][index] = float(
                                input('Enter new price : ').strip())
                        elif edit == '3' or all_item:
                            stock['qty'][index] = int(
                                input('Enter new quantity : ').strip())

                    elif buff == '4':
                        os.system('cls')
                        password = input('Enter new passward : ').strip()
                    elif buff == 'e':
                        go_in = False
                        break

    elif mode == '2':
        os.system('cls')
        while True:
            buff = input('''\nHello.. :)
Welcome to ITI shop\n
please choose from the following options:
1   view available items
2   add item to cart
3   remove item from cart
4   view items in cart
5   purcase
e   exit\n''').strip().lower()
            if buff == '1':
                os.system('cls')
                print('Item\t\t\t\tPrice')
                for n in range(0, len(stock['items'])):
                    print('{}\t\t\t\t{}'.format(
                        stock['items'][n], stock['price'][n]))
                print('-'*50)
            elif buff == '2':
                os.system('cls')
                print('Item\t\t\t\tPrice')
                i = 1
                for n in range(0, len(stock['items'])):
                    print('{}\t\t\t\t{}'.format(i, stock['items'][n]))
                    i += 1
                print('-'*50)
                item = int(input('Choose item to add to cart : ').strip())-1
                qty = int(input('How many would you like to add : ').strip())
                cart.append([stock['items'][item], qty])
            elif buff == '3':
                os.system('cls')
                c = 1
                for i in cart:
                    print('{}\t{}\t\t{}'.format(c, i[0], i[1]))
                    c += 1
                print('-'*50)
                item_remove = int(
                    input('Choose the item you want to remove : ').strip())-1
                cart.pop(item_remove)
            elif buff == '4':
                os.system('cls')
                print('items\t\tqty')
                for i in cart:
                    print('{}\t\t{}'.format(i[0], i[1]))
                print('-'*50)
            elif buff == '5':
                os.system('cls')
                print('item\t\tqty\tprice')
                total_price = 0
                for i in cart:
                    item_price = i[1] * \
                        stock['price'][stock['items'].index(i[0])]
                    total_price += item_price
                    print('{}\t\t{}\t{}'.format(i[0], i[1], item_price))
                print('-'*50)
                print('Total price :\t{}'.format(total_price))
                cart = []
            elif buff == 'e':
                break
    else:
        print('Invalid mode !!')
        time.sleep(2)
