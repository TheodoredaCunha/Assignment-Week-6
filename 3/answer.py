#groceries list 
groceries = ["banana","orange", "apple"]

#stocks and prices dictionaries
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

def compute_bill(food):
	total = 0
	for item in food:
		if stock[item] > 0:
			total += prices[item]
			stock[item] -= 1
		
	return total
print("Groceries list: {}".format(groceries))
print("The total price to pay for the grocery list is {}".format(compute_bill(groceries)))