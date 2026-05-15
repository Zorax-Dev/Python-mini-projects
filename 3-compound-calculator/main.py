# python compound interest calculator 

principal = 0
rate = 0 
time = 0

while True:
    principal = float(input("Enter teh principal amount: "))
    if principal <=0:
        print("principal cant be less than zero")
    else:
        break

while True:
    rate = float(input("Enter teh rate amount: "))
    if rate <=0:
        print("rate cant be less than zero")
    else:
        break

while True:
    time = float(input("Enter teh time amount: "))
    if time <=0:
        print("time cant be less than zero")
    else:
        break

total = principal * pow((1 + rate/100),time) 

print("\n------------------------------------------------------")
print(f"your money in {time} years will be: ${round(total, 2)}")
