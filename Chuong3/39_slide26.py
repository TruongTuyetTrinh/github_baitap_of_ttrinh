yrsofsevice=int(input('So nam lm viec:'))
salary=int(input('Muc luong hien tai:'))
if yrsofsevice<5:
    if salary<500:
        bonus=100
    else:
        bonus=200
else:
    bonus=700
print('Bonus amount',bonus)
    
    