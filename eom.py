# print("Welcome! This is the official software for the End of the Month fanatic.")
# print('You will be walked through completing the EoM through a series of questions to get your databases up-to-date.')
# print('Enjoy the simplicity and power!')


def cash():
    num_accounts = int(input("How many bank accounts/cash equivalents do you have? "))
    if num_accounts == 0:
        return 0
    type_account = ['checking', 'savings', 'cash']
    accounts = {}

    for acc in range(num_accounts):
        print(f"What type of account is account #{acc + 1}? ")
        type = int(input("1 for checking, 2 for savings, and 3 for cash: "))
        if type == 1:
            type = 'checking'
        elif type == 2:
            type = 'savings'
        elif type == 3:
            type = 'cash'
        else:
            print("Sorry please enter a number 1-3. Try again. ")
        nickname = input("Please give this account a nickname: ")
        accounts[type] = [nickname, float(input("How much money is in this account? "))]
        total_cash = total(accounts)

    #  gives user an easy to read view of their cash equivalents
    print("To summarize, you have: ")
    for i, j in enumerate(accounts):
        # print(accounts)
        # print(j)
        # print(str(accounts.get(j)[0]))
        # print(j.get('checking'))
        print('\x1b[6;30;42m' + '$' + '{:,}'.format(accounts.get(j)[1]) + ' in ' + str(accounts.get(j)[0]) + " (" + str(j) + ")" + '\x1b[0m') # + ' called ' + str(accounts.get(j)[0])
    return total_cash

def investments():
    num_accounts = int(input("How many investment accounts do you have? "))
    if num_accounts == 0:
        return 0
    type_account = ['401k', 'IRA', 'cryptocurrency', 'taxable brokerage']
    accounts = {}

    for acc in range(num_accounts):
        print(f"What type of account is account #{acc + 1}? ")
        type = int(input("1 for 401k, 2 for IRA, 3 for taxable brokerage, and 4 for cryptocurrency: "))
        if type == 1:
            type = '401k'
        elif type == 2:
            type = 'IRA'
        elif type == 3:
            type = 'taxable brokerage'
        elif type == 4:
            type = 'cryptocurrency'
        else:
            print("Sorry please enter a number 1-4. Try again. ")
        nickname = input("Please give this account a nickname: ")
        accounts[type] = [nickname, float(input("How much money is in this account? "))]
        total_investments = total(accounts)

    #  gives user a summary of their total investments in an easy to read format
    print("To summarize, you have: ")
    for i, j in enumerate(accounts):
        print('\x1b[1;30;42m' + '$' + '{:,}'.format(accounts.get(j)[1]) + ' in ' + str(j) + '\x1b[0m')
        # '{:,}'.format tells python to add commas to large numbers
    return total_investments

def liabilities():
    num_accounts = int(input("How many debt accounts do you have? "))
    if num_accounts == 0:
        return 0
    type_account = ['mortgage', 'credit card', 'personal loan', 'business loan']
    accounts = {}

    for acc in range(num_accounts):
        print(f"What type of account is account #{acc + 1}? ")
        type = int(input("1 for mortgage, 2 for credit card, 3 for personal loan, and 4 for business loan: "))
        if type == 1:
            type = 'mortgage'
        elif type == 2:
            type = 'credit card'
        elif type == 3:
            type = 'personal loan'
        elif type == 4:
            type = 'business loan'
        else:
            print("Sorry please enter a number 1-4. Try again. ")
        nickname = input("Please give this account a nickname: ")
        accounts[type] = [nickname, float(input("How much money do you owe on this account? "))]
        total_debts = total(accounts)

    #  gives user a summary of their total investments in an easy to read format
    print("To summarize, you owe: ")
    for i, j in enumerate(accounts):
        print('\x1b[1;31;40m' + '$' + '{:,}'.format(accounts.get(j)[1]) + ' in ' + str(j) + '\x1b[0m')
        # '{:,}'.format tells python to add commas to large numbers
    return total_debts

def total(accounts):
    total_cash = 0
    for i in accounts:
        total_cash += accounts[i][1]
    return total_cash

def net_worth(cash = 0, investments = 0, liabilities = 0):
    net_worth = cash + investments - liabilities
    return net_worth

def advices():
    print("Increasing your net worth is simple, but not easy.")
    print("It boils down to one rule: ")
    print("SAVE MORE THAN YOU SPEND.")
    print("Like we said - simple, but not easy.")
    print("The first, best way, to save more than you spend is to increase your earning power. This can be done by increasing your value in the market place through education and skills.")
    print("The second way to cut spending. It's not as fun as the previous bit of advice but sometimes necessaary when our spending gets too carried away.")
    print("Repeat steps one and two until satisfied.")
    print("Thanks for using this tool! \U0001F917")

# Class Assets, Class Liabilities?
# cash()
# stocks()
# realestate()
# retirement_accounts()
# debts
# investments()
# liabilities()
net_worth = net_worth(cash(), investments(), liabilities())
if net_worth > 0:
    print(f"\n\n\x1b[1;32;47mYour total net worth is: ${net_worth}\x1b[0m\n\n")
    print("Great job! You have a positive net worth. Keep saving more than you earn! \U0001F911")
else:
    print(f"\n\n\x1b[1;31;47mYour total net worth is: ${net_worth}\x1b[0m\n\n")
    # \U0001F914 is the code to input emojis using unicode
    print("You have a negative net worth. It is recommended that you start saving more than you spend. \U0001F914")
    advice = input("Would you like advice on how to do that? ")
    if advice == 'yes':
        advices()
    else:
        print("Okay, thanks for running the net worth calculator! See you.")