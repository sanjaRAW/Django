import random
import math

customers = ['brad', 'jolie', 'johny', 'sooronbai', 'sooronbai', 'sadyr', 'sadyr', 'emma', 'sooronbai',
             'brad', 'almazbek', 'roza', 'roza', 'kurmanbek', 'toby', 'tony', 'robert', 'askar', 'robert', 'chris',
             'chris']

custdist = set(customers)

custdistnum = len(custdist)

print(custdist, custdistnum)


list1 = random.sample(range(1,1000000), 600000)


listmax = list1.index(max(list1))

listmin = list1.index(min(list1))

if listmin > listmax:
    listfrst = listmin
    listscnd = listmax
else:
    listfrst = listmax
    listscnd = listmin

print(listmax, listmin, listfrst - listscnd, list1[listmax], list1[listmin])

fact = math.factorial(400000)
result = fact/ (fact * math.factorial(10))

print(result)