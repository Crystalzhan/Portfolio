import bankOp
import accountInfo


def accountSPrompt(pinNum):
    accountInfo = accountsDb.viewAccountInf(pinNum)
    print('First Name:     {}\nLast Name:      {}\nAccount Number: {}\nAccountType:    {}'.format(accountInfo.firstName, accountInfo.lastName, accountInfo.acctNum, accountInfo.acctType))
    while True:
        accountBalance = accountsDb.viewAccountBalance(pinNum)
        option = input('Please enter the Option number you want select (Option1: view Balance; Option2: make Deposit; Option 3: withdraw funds; Option 4: return to main menu）: ')
        if option == '1':
            print ('Your current Account Balance is : ', accountBalance)

        elif option == '2':
            depositAmt = eval(input('Please enter the deposit amount: '))
            
            preDBal = accountBalance
            curDBal = accountsDb.makeDeposit(pinNum, depositAmt)
            print('Your previous Account Balance is: {}\nYour deposit amount is:            {}\nYour current Account Balance is:  {}'.format(preDBal, depositAmt, curDBal))

        elif option == '3':
            withdrawAmt = eval(input('Please enter the withdraw amount: '))
            while accountBalance < withdrawAmt:
                print('The amount you entered is greater than your Account Balance, please enter a new amount: ')
                withdrawAmt = eval(input('Please enter the withdraw amount: '))
                    
            preWBal = accountBalance
            curWBal = accountsDb.makeWithdraw(pinNum, withdrawAmt)
            print('Your previous Account Balance is: {}\nYour withdraw amount is:            {}\nYour current Account Balance is:  {}'.format(preWBal, withdrawAmt, curWBal))

        elif option == '4':
            break


accountsDb = bankOp.ATM()
accountsDb.loadAccounts('accountsinfo.txt')
count = 0

while True:
    pinEnt = input('Please enter the 4-digit PIN that corresponds to your account: ')
    pinMatch = accountsDb.login(pinEnt)

    if count > 2:
        print('Sorry, you have input invalid PIN 3 times, please contact Bank to change your PIN')
        exit()
    elif pinMatch == False:
        count += 1
        print('The PIN you entered is invalid! Please enter again!')
    else:
        count = 0
        accountSPrompt(pinEnt)

    
