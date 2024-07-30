def sum_of_nnum(n):
    i=1
    sum=0
    while i<=n:
        print(i)
        sum+=i
        i+=1
    return sum
num=int(input('enter a limit'))
print(f"sum of {num} number is{sum_of_nnum(num)} ")
"""
num=3
sum of n num(3)
i=1
sum=0
while 1<=3:
print(1)
sum=0+1
i=2
while 2<=3:
print(2)
sum=1+2
i=3
while 3<=3:
print(3)
sum=3+3
i=4(loop breaks)
sum=6
"""
