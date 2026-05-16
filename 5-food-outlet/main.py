# food outlet program 

print("Pruducts available list:")
print("pizza - $3.99")
print("cola - $1.99")
print("burger - $4.48")
print("chips - $1.00")
print("roll - $4.98")

foods = []
prices = []
quantitys = []
total = 0

rack = {
    "pizza": 3.99,
    "cola": 1.99,
    "burger": 4.48,
    "chips": 1.00,
    "roll": 4.98,
    "hotdog": 1.75,
    "golden burger": 10
}

print("\n")
print("-------------------------------------------")
while True:
    item = input("what item would you like to eat?: ")
    if item.lower() == "q":
        break
    else:
        quantity = int(input("How many would you like?: "))
        quantitys.append(quantity)
        foods.append(item)
        price = rack[item]
        prices.append(price * quantity)

tip = float(input("Tip for our Service: "))
for price in prices:
    total += price

subtotal = total + tip

print("\n\n")
print("-------------------------------")
print("            BILL")
print("-------------------------------")
for i in range(len(foods)):
    print(quantitys[i],foods[i],": "," $", rack[foods[i]])
print(f"TIP: ${tip}")
print("-------------------------------")
print(f"Subtotal: ${subtotal}")