import math
import sys
import os
import random
num=64
square_root=math.sqrt(num)
print(square_root)
print(math.factorial(5))
random_int=random.randint(1,100)
print(random_int)
list1=[4,1,6,89,42,68]
random.shuffle(list1)
print(list1)
def odd_even(n):
    if n%2==0:
        return "even"
    else:
        return "odd"
print(os.getcwd())
print(sys.version)
