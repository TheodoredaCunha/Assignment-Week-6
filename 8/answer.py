def get_next(pokemon):
	try:
		next_letter = pokemon[len(pokemon) - 1]
		return pokemons_dictionary2[next_letter]
	except:
		return []

pokedex = """audino bagon baltoy banette bidoof braviary bronzor carracosta
charmeleon cresselia croagunk darmanitan deino emboar emolga exeggcute
 gabite girafarig gulpin haxorus heatmor heatran ivysaur jellicent jumpluff
 kangaskhan kricketune landorus ledyba loudred lumineon lunatone machamp magnezone mamoswine nosepass
 petilil pidgeotto pikachu pinsir poliwrath poochyena porygon2 porygonz registeel relicanth remoraid rufflet
 sableye scolipede scrafty seaking sealeo silcoon simisear snivy snorlax spoink starly tirtouga trapinch treecko
 tyrogue vigoroth vulpix wailord wartortle whismur wingull yamask
"""

list_of_pokemons = pokedex.split(" ")

for index in range(len(list_of_pokemons)):
	list_of_pokemons[index] = list_of_pokemons[index].replace("\n", "")
	
pokemons_dictionary = {}
for pokemon in list_of_pokemons:
	try:
		pokemons_dictionary[pokemon[0]].append(pokemon)
	except:
		pokemons_dictionary[pokemon[0]] = []
		pokemons_dictionary[pokemon[0]].append(pokemon)

pokemons_dictionary2 = pokemons_dictionary
		
record = 0
chain = []	
current_length = 0
current_chain = []

def play_game(name):
	global current_chain
	global current_length
	global record 
	global chain
	global pokemons_dictionary2
	current_chain.append(name)
	current_length += 1
	next_list = get_next(name)
	pokemons_dictionary2[name[0]].remove(name)
	if len(next_list) == 0:
		if current_length >= record:
			record = current_length
			chain = current_chain
		print("{}: {}".format(record, chain))
		current_chain = []
		current_length = 0
		pokemons_dictionary2 = pokemons_dictionary
	else:
		for i in next_list:
			play_game(i)

"""
for i in list_of_pokemons:
	print(i)
	pokemons_dictionary2 = pokemons_dictionary
	play_game(i)
"""

play_game("machamp")