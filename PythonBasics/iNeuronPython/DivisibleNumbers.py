#Find numbers which are divisible by 7 and multiple of 5 between a range 2000 & 3200
#@author : Shreekrishna

divisible_numbers=[]
for x in range(2000, 3200):
    if (x%7==0) and (x%5==0):
        divisible_numbers.append(str(x))
print (','.join(divisible_numbers))