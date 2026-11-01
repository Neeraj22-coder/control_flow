print("====MENU====")
print("1.veg sandwich - 60")
print("2.Masala dosa - 80")
print("3.chole rice - 90")
print("4.paneer roll - 100")
print("6.tea - 20")
total=0
item=int(input("Enter the item no (1-5):"))
while True:
    if item==1:
        name="veg sandwich"
        price=60
    elif item==2:
        name="Masala Dosa"
        price=80
    elif item==3:
        name="chole rice"
        price=90
    elif item==4:
        name="paneer roll"
        price=100
    elif item==5:
        name="tea"
        price=20
    else:
        print("invalid itenm number")
        continue
    quantity=int(input("Enter the quantity:"))
    if quantity<=0:
        print("Enter the quantity")
    cost=quantity*price
    total=+cost
    print(name,"=",cost)
    again=(input("add more item? (yes=item no, no):"))
    if again == "no":
        break
if total>=500:
    discount=total*10/100
elif total>=250:
    discount=total*5/100
else:
    discount=0
total_amount=total-discount

print("\n=====RECEIPT=====")
print("Subtotal: ",total)
print("discount:",discount)
print("final amount: ",total_amount)
print("\n====THANK YOU====")
print("Visit Again")




