depositedmoney = int(input())
firstyearamount = depositedmoney*1.04
secondyearamount = depositedmoney*1.04**2
thirdyearamount = depositedmoney*1.04**3
print('the amount after 1 year in the account is', round(firstyearamount, 2))
print('the amount after 2 year in the account is', round(secondyearamount, 2))
print('the amount after 3 year in the account is', round(thirdyearamount, 2))
