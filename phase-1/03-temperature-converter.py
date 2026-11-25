temp=float(input("Enter temperature: "))
type=input("Enter Type (C/F/K): ")
if type=='C' or type=='c':
    print("Temperature in Kelvin: ", temp+273.15)
    print("Temperature in Fahrenheit: ", (temp*(9/5))+32)
elif type=='F' or type=='f':
    print("Temperature in Kelvin: ", ((temp-32)*(5/9))+273.15)
    print("Temperature in Celsius: ", (temp-32)*(5/9))
elif type=='K' or type=='k':
    print("Temperature in Fahrenheit: ", ((temp-273.15)*(9/5))+32)
    print("Temperature in Celsius: ", temp-273.15)
else:
    print("invalid type!")