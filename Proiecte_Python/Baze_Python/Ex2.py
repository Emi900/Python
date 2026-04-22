#Exercise 2 Shopping Cart Program 

item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many woul you like?: "))
total = price * quantity

print(f"The toatal price for {item} is ${total}!")