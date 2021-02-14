#Find numbers which are divisible by 7 and multiple of 5 between a range
#@author : Shreekrishna

divisible_numbers=[]
for x in range(1500, 2701):
    if (x%7==0) and (x%5==0):
        divisible_numbers.append(str(x))
print (','.join(divisible_numbers))