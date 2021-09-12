# print("Welcome! This is the official software for the End of the Month fanatic.")
# print('You will be walked through completing the EoM through a series of questions to get your databases up-to-date.')
# print('Enjoy the simplicity and power!')


def cash():
    num_accounts = int(input("How many bank accounts/cash equivalents do you have? "))
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

    print("To summarize, you have: ")
    for i, j in enumerate(accounts):
        print(accounts)
        print(i)
        print(j)
        print(j[0] + ' in ' + j[1])
    return total_cash

def total(accounts):
    total_cash = 0
    for i in accounts:
        total_cash += accounts[i][1]
    return total_cash

def net_worth(cash = 0, stocks = 0, realestate = 0):
    net_worth = cash + stocks + realestate
    return net_worth


# Class Assets, Class Liabilities?
# cash()
# stocks()
# realestate()
# retirement_accounts()
# debts
net_worth = net_worth(cash())
print(f"Your total net worth is: ${net_worth}")