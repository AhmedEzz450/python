import os
import time

calc_on = True
normal_operation = ('+', '-', '/', '*')
normal_history = []

prog_operation = ('and', 'or', 'not', 'xor', '<<', '>>')

result = int()

#print("Hello, AEMA :)")

message = ''

while calc_on:
    os.system('cls')
    print(message)
    message = ''
    mode = input('''Select mode
N  for normal mode
P  for programmer mode
E  to exit\n''').upper().strip()

    if mode == 'E':
        calc_on = False

    elif mode == 'N':
        while mode == 'N':
            os.system('cls')
            for h in normal_history:
                print(h)

            buff = input("Enter your operation \
            EX: 1 + 1\nEnter E to exit Normal mode\n").strip().upper()

            if buff == 'E':
                break

            else:
                a = ''
                operator = ''
                b = ''
                index = None

                for digit in buff:
                    if digit in normal_operation:
                        operator += digit
                        index = buff.index(digit) + 1
                        break
                    else:
                        a += digit.strip()

                b = buff[index:].strip()
                print(a)
                print(operator)
                print(b)

                if a.replace('.', '', 1).isdigit() == False:
                    print('1st operand is not numeric !!')
                    time.sleep(2)
                    continue
                elif operator not in normal_operation:
                    print('Wrong operator !!')
                    time.sleep(2)
                    continue
                elif b.replace('.', '', 1).isdigit() == False:
                    print('2nd operand is not numeric')
                    time.sleep(2)
                    continue

                if operator == '+':
                    result = float(a) + float(b)
                    print('{} {} {} = {}'.format(a, operator, b, str(result)))
                elif operator == '-':
                    result = float(a) - float(b)
                    print('{} {} {} = {}'.format(a, operator, b, str(result)))
                elif operator == '*':
                    result = float(a) * float(b)
                    print('{} {} {} = {}'.format(a, operator, b, str(result)))
                elif operator == '/':
                    if float(b) != 0:
                        result = float(a) / float(b)
                        print('{} {} {} = {}'.format(
                            a, operator, b, str(result)))
                    else:
                        print('Can\'t divide by 0 !!!')
                time.sleep(2)

    elif mode == 'P':
        while mode == 'P':
            os.system('cls')
            buff = input("Enter your operation\
            EX: 1 and 1 \nEnter E to exit Programmer mode\n").strip().lower()

            if buff == 'e':
                break
            else:
                a = ''
                operator = ''
                b = ''

                for digit in buff:
                    if digit.isnumeric():
                        if operator in prog_operation:
                            b += digit
                        else:
                            a += digit
                    else:
                        operator += digit.strip()

                if operator not in prog_operation:
                    print("Invalid operator !!!")
                    time.sleep(2)
                    continue
                elif a.isnumeric() == False:
                    if (operator != 'not') or (not b.isnumeric()):
                        print('Invalid operand !!!')
                        time.sleep(2)
                        continue

                if operator == 'and':
                    result = int(a) & int(b)
                    print('{} {} {} = {}'.format(a, operator, b, str(result)))
                elif operator == 'or':
                    result = int(a) | int(b)
                    print('{} {} {} = {}'.format(a, operator, b, str(result)))
                elif operator == 'xor':
                    result = int(a) ^ int(b)
                    print('{} {} {} = {}'.format(a, operator, b, str(result)))
                elif operator == 'not':
                    result = ~int(b)
                    print('{} {} {} = {}'.format(a, operator, b, str(result)))
                elif operator == '<<':
                    result = int(a) << int(b)
                    print('{} {} {} = {}'.format(a, operator, b, str(result)))
                elif operator == '>>':
                    result = int(a) >> int(b)
                    print('{} {} {} = {}'.format(a, operator, b, str(result)))
                time.sleep(2)
    else:
        message = 'Invalid selection !!'
