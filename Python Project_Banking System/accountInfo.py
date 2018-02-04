class Account:
    def __init__(self, aPin, aAcctNum, aFName, aLName, aAcctBal, aAcctType):
        self.pin = aPin
        self.acctNum = aAcctNum
        self.firstName = aFName
        self.lastName = aLName 
        self.acctBal = eval(aAcctBal)
        self.acctType = aAcctType
        
