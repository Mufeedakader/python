# try:
#     num1=int(input('enter the first number'))
#     num2=int(input('enter the second number'))
#     div=num1/num2
#     print(div)
# except ZeroDivisionError:
#     print('cannot divided by zero')
# except ValueError:
#     print('invalid input')
# finally:
#     print('execution completed')
try:
    num1=int(input('enter the first number'))
    num2=int(input('enter the second number'))
    div=num1/num2
    print(div)
except (ZeroDivisionError,ValueError):
    print('cannot divided by zero or invalid error')
finally:
    print('execution completed')
