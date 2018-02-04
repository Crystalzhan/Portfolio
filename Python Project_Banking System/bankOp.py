import accountInfo

class ATM:
    savingsAccounts = {}

    def makeDeposit(self, pin, depositAmount):
        ATM.savingsAccounts[pin].acctBal += depositAmount
        return ATM.savingsAccounts[pin].acctBal

    def makeWithdraw(self, pin, withdrawAmount):
        ATM.savingsAccounts[pin].acctBal -= withdrawAmount
        return ATM.savingsAccounts[pin].acctBal

    def viewAccountBalance(self, pin):
        acctBalance = ATM.savingsAccounts[pin].acctBal
        return acctBalance

    def viewAccountInf(self, pin):
        acctInf = ATM.savingsAccounts[pin]
        return acctInf

    def loadAccounts(self, fileName):
        accountsFH = open(fileName)
        accountsDict = ATM()
    
        for line in accountsFH:
            aInfo = line.split(',')
            pin = aInfo[0]
            acctNum = aInfo[1]
            firstName = aInfo[2]
            lastName = aInfo[3]
            acctBal = aInfo[4]
            acctType = aInfo[5]
            anAccount = accountInfo.Account(pin, acctNum, firstName, lastName, acctBal, acctType)
            accountsDict.savingsAccounts[pin] = anAccount
        

    def login(self, pin):
        if pin in ATM.savingsAccounts:
            return True
        else:
            return False
            
            
        
        

    

    

    
    
