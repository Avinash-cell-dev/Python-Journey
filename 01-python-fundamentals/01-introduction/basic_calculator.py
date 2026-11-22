number1=float(input("Enter number 1: "))
number2=float(input("Enter number 2: "))
print("===Menu===")
print("1. Add")
print("2. Sub")
print("3. Divide")
print("4. Multiply")
print("5. Get Reminder")
choice=int(input("Enter your choice: "))
if choice==1:
    print(number1+number2)
elif choice==2:
    print(number1-number2)
elif choice==3:
    print(number1/number2)
elif choice==4:
    print(number1*number2)
elif choice==5:
    print(number1%number2)
else:
    print("invalid choice")