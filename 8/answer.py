def get_next(pokemon, dictionary):
	try:
		next_letter = pokemon[len(pokemon) - 1]
		return dictionary[next_letter]
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

		
record = 0
chain = []	
current_length = 0
current_chain = []

def play_game(name, dictionary):
	global current_chain
	global current_length
	global record 
	global chain
	current_chain.append(name)
	current_length += 1
	next_list = get_next(name, dictionary)
	try:
		dictionary[name[0]].remove(name)
	except:
		pass
	if len(next_list) == 0:
		if current_length >= record:
			record = current_length
			chain = current_chain
		print("{}: {}".format(current_length, current_chain))
		current_chain = []
		current_length = 0
	else:
		for i in next_list:
			play_game(i, pokemons_dictionary)

for i in list_of_pokemons:
	print(i)
	play_game(i, pokemons_dictionary)
