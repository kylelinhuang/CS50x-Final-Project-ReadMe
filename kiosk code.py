import os, time
from decimal import Decimal
print('Welcome to In-N-Out. What will it be to start off today?')
x = True
no_tax = Decimal('0.00')
display = []
while x == True:
  print('Please type a number 1-16')
  print('')
  print('1 - Double-Double Combo: $7.89')
  print('2 - Cheeseburger Combo: $6.65')
  print('3 - Cheeseburger: $2.95')
  print('4 - Hamburger Combo: $6.35')
  print('5 - Hamburger: $2.65')
  print('6 - French Fries: $2.95')
  print('7 - Chocolate Shake: $2.50')
  print('8 - Vanilla Shake: $2.50')
  print('9 - Strawberry Shake: $2.50')
  print('10 - Small Soda: $1.65')
  print('11 - Medium Soda: $1.75')
  print('12 - Large Soda: $1.95')
  print('13 - Extra Large Soda: $2.15')
  print('14 - Milk: $0.99')
  print('15 - Hot Cocoa: $1.75')
  print('16 - Coffee: $1.25')
  print('')
  My_library = {'1':Decimal('7.89'), '2':Decimal('6.65'), '3':Decimal('2.95'), '4':Decimal('6.35'), '5':Decimal('2.65'), '6':Decimal('2.65'), '7':Decimal('2.50'), '8':Decimal('2.50'), '9':Decimal('2.50'), '10':Decimal('1.65'), '11':Decimal('1.75'), '12':Decimal('1.95'), '13':Decimal('2.15'), '14':Decimal('0.99'), '15':Decimal('1.75'), '16':Decimal('1.25')}
  My_display = {'1':'Double-Double Combo', '2':'Cheeseburger Combo', '3':'Cheeseburger', '4':'Hamburger Combo', '5': 'Hamburger', '6':'French Fries', '7':'Chocolate Shake', '8':'Vanilla Shake', '9':'Strawberry Shake', '10':'Small Soda', '11':'Medium Soda', '12':'Large Soda', '13':'Extra Large Soda', '14':'Milk', '15':'Hot Cocoa', '16':'Coffee'}
  order = input('')
  no_tax += My_library[order]
  os.system('clear')
  display.append(My_display[order])
  print('Your Total: $' + str(no_tax))
  print('Your Order: ' + str(display))
  print('')
  print('Would you like to add something else? (y/n)')
  print('')
  repeat = input('')
  time.sleep(1)
  os.system('clear')
  if repeat == 'Yes' or repeat == 'Y' or repeat == 'yes' or repeat =='y':
    x == True
  else:
    break
taxed = no_tax*Decimal('1.08')
taxed = round(taxed, 2)
print('With tax, your total will be $' + str(taxed) + '. Please pay at the next window and wait for your number to be called. Thank you for your purchase and have a good day!')
time.sleep(10)
os.system('clear')
