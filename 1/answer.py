def print_dictionary(inventory):
	"""Function to print out inventory"""
	for i in inventory.items():
		print('{} : {}'.format(i[0], i[1]))

inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

print('Old Dictionary: \n{')
print_dictionary(inventory)
print('}')

"""
Adding a key to inventory called "pocket"
Set the value of 'pocket' to be a list consisting of the strings 'seashell', 'strange berry', and 'lint'.
"""
inventory['pocket'] = ['seashells', 'strange berry', 'lint']

""".sort()the items in the list stored under the 'backpack' key."""
inventory['backpack'] = sorted(inventory['backpack'])

"""Then .remove('dagger') from the list of items stored under the 'backpack' key."""
inventory['backpack'].remove('dagger')

"""Add 50 to the number stored under the 'gold' key."""
inventory['gold'] += 50

print('\nNew Dictionary: \n{')
print_dictionary(inventory)
print('}')
