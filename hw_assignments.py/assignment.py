item = input("Item Name: ")
unit_price = float(input("Unit Price: $"))
quantity = int(input("Quantity: "))
member = input("Member(Y or N): ")
subtotal = float(unit_price * quantity)
print("Subtotal: $", format(subtotal, ".2f"))
if member =="Y":
    discount_rate = 10 #in terms of percentage
else:
    discount_rate = 0 #in terms of percentage
print("Discount Rate: ", discount_rate, "%")
discount = float(subtotal * (discount_rate / 100))
print("Discount: -$", format(discount, ".2f"))
total = float(subtotal - discount)
print("Total: $", format(total, ".2f"))


#1)Item Name is a string; Unit Price is a float; Quantity is an integer; and Member is a string
#2)To compute these values, I used the equations that were given in the assignment documents. 
#Specifically for the discount rate, I add the divide by 100 to ensure the percentage was 
#Formatted as a decimal in the discount calculation. 
#3)For my if/else statement I have if member == “Y” then the discount rate is 10 (in terms of a percent)
#and the else statement says the discount rate is 0. 
