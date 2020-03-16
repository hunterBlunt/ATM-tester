import sys

#ATM program 

#account balance 
account_balance = float(500.25)



#printbalance function
def printbalance ():
  p = print(account_balance)
  return p

#deposit function
def deposit (dep):
  global account_balance
  d = account_balance + float(dep)
  d = print('Deposit was $' + '%.2f' % float(dep) + ', current balance is $' + str(d))
  return d
  

#withdraw function
def withdraw (wit):
  global account_balance
  w = account_balance - float(wit)
  
  #in case they enter an ammount greater than balance
  
  if w < 0:
    print('$' + '%.2f' % float(wit) + ' is greater than your account balance of $' + str(500.25))
  else:
    print('Withdrawal amount was $' + '%.2f' % float(wit) + ', current balance is $' + str(w))
  return w

#gets the users input and runs fuctions based on their selection

userchoice = input ('What would you like to do?\n (D) Deposit\n (W) Withdrawal\n (B) Print Balance\n (Q) Quit\n')

if (userchoice == 'D'):
  deposit (input('How much would you like to deposit today?\n'))

elif (userchoice == 'W'):
  withdraw (input('How much would you like to withdraw today?\n'))
  
elif (userchoice == 'B'):
  print('Your current balance:')
  printbalance ()

elif (userchoice == 'Q'):
  print('Thank you for banking with us.')

