class ATM(object):
  

  def __init__(self, cardNumber, pinNumber):
    self.cardNumber = cardNumber
    self.pinNumber = pinNumber
    

  def cashWithdrawel(self):
    print("You have withdrawn some cash from your bank account")

  def balanceEnquiry(self):
    print("Your current balance is...")

  def depositCash(self):
    print("You just deposited some cash into your bank account")

payPal= ATM("123 567 890", "130")
print(payPal.depositCash())
    

  



