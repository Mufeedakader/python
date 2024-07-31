# check whether neg or postv or zero 
# num=float(input('enter a number'))
# if num<0:
#     print('it is a negative number')
# elif num>0:
#     print('it is a positive number')
# else:
#     print('it is a zero')
# check whether 3 digit or not
# number=input('enter a three digit number')
# if number.isdigit() and 100 <= int(number) <= 999:
#     print(f"The number {number} is a 3-digit number.")
# else:
#     print(f"The number {number} is not a 3-digit number.")
# coverting digits to text
# def number_to_text(n):
#     if n < 0 or n > 99:
#         return "Number out of range. Please enter a number between 0 and 99."

#     ones = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
#     teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
#     tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

#     if 0 <= n < 10:
#         return ones[n]
#     elif 10 <= n < 20:
#         return teens[n - 10]
#     else:
#         return tens[n // 10] + ('' if n % 10 == 0 else ' ' + ones[n % 10])
# number = int(input("Enter a number between 0 and 99: "))
# print(number_to_text(number))
# check whether divisble by 7 or not
num=int(input('enter a number'))
if num%7==0:
    print(f'{num}is divisble by 7')
else:
    print(f'{num}is not divible  by 7')  
