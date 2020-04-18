time = int(input('the time in second is '))

day = time//86400
hour = time%86400 //3600
minute = time%86400%3600//60
second = time%86400%3600%60
print(f'{day}:{"%02d" % hour}:{"%02d" % minute}:{"%02d" % second}')
