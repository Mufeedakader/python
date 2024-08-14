def digit_to_text(num):
    if num<0 or num>99:
        return "number out of range"
    else:
        numbers={0:'zero',1:'one',70:'seventy'}
    if num in numbers:
        return numbers[num]
    else:
        return f"{numbers[num-num%10]} -{numbers[num%10]}"
number=int(input('enter a number:'))
print(digit_to_text(number))
    # numbers[70-70%10]-numbers[70%10]  
      