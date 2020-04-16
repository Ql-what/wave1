money = int(input('the amount of money in cents is :'))

toonies = money//200
loonies = money%200//100
quarters = money%100//25
dimes = money%100%25//10
nickels = money%100%25%10//5
pennies = money%100%25%10%5//1

print(toonies,'toonies', loonies,'loonies', quarters,'quarters', dimes,'dimes', nickels,'nickels', pennies,'pennies')