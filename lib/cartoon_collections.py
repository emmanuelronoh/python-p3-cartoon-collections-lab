# cartoon_collections.py

def roll_call_dwarves(dwarves):
    '''Prints out the 7 dwarfs in a numbered list.'''
    for index, dwarf in enumerate(dwarves, start=1):
        print(f"{index}. {dwarf}")

def summon_captain_planet(elements):
    '''Capitalizes each element and adds an exclamation mark.'''
    return [f"{element.capitalize()}!" for element in elements]

def long_planeteer_calls(calls):
    '''Returns true if any calls are longer than 4 characters.'''
    return any(len(call) > 4 for call in calls)

def find_the_cheese(snacks):
    '''Returns the first element of the array that is cheese.'''
    cheeses = ["cheddar", "gouda", "camembert"]
    for snack in snacks:
        if snack in cheeses:
            return snack
    return None
