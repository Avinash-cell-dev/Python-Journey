p=float(input("Enter principal amount: "))
r=float(input("Enter annual interest rate: "))
t=float(input("Enter duration in years: "))
si=(p*r*t)/100
a=p+si
print("simple interest:",si)
print("Final amount:",a)