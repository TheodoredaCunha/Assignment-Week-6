#Creating the dictionary
prices = {
	"banana": 4,
	"apple": 2,
	"orange": 1.5,
	"pear": 3
}

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

#Printig all fruit names, prices, and stocks
for i in prices.items():
	print("\n {} \n price: {} \n stock: {} ".format(i[0], prices[i[0]], stock[i[0]]))

print("\n")

#Calculating the total price to pay
total = 0
for i in prices.items():
	#total_fruit_price is the total price for each fruit
	total_fruit_price = prices[i[0]] * stock[i[0]]
	print("All {} costs {}".format(i[0], total_fruit_price))
	total += total_fruit_price

print("Total Price to pay is {}".format(total))
	