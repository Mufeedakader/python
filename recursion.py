def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
n=int (input('enter a number:'))
print(fact(n))
"""
n=3
fact(3)
3*fact(2)
2*fact(1)
if n=1 fact(1)=1
fact(3)=6
"""