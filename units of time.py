daysnumber = int(input('the number of days is:'))
hoursnumber = int(input('the number of hours is'))
minutesnumber = int(input('the number of minutes is'))
secondsnumber = int(input('the number of seconds is'))

totalseconds = daysnumber*86400 + hoursnumber*3600 + minutesnumber*60 + secondsnumber
print('the total number of time in seconds is:', totalseconds)