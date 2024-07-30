# if bill is greater than 2000 then discount =12%
# bill>5000 then 18%
# bill >10000 then 25%
# def calc_discount(total_price):
#     if total_price>10000:
#         return total_price*0.25
#     elif total_price>5000:
#         return total_price*0.18
#     elif total_price>2000:
#         return total_price*0.12
#     else:
#         return 0
# def main():
#     prices=[]
#     num_of_items=int(input("number of items"))
#     for i in range(num_of_items):
#         price=(float (input("enter the price of the item")))
#         prices.append(price)
#     total_price=sum(prices)
#     discount=calc_discount(total_price)
#     final_price=total_price-discount
#     print(f"total price {total_price}")
#     print(f"discount{discount}")
#     print(f"final price{final_price}")
# main()
# leap year
year = int(input("Enter a year: "))
if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")