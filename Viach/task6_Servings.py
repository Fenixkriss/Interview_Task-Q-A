# Function takes a recipe (dictionary) and available ingredients (dictionary) 
# and returns the number of servings we can cook.
# Example:
# recipe = {"flour": 500, "sugar": 200, "eggs": 1} 
# available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
# count(recipe, available) -> 2


def servings(demand, storage): 
	# calculate demand/storage ratio. resistant for missing ingredient
	c = [] # list of ratios
	for k,v in demand.items():
		try : c.append(storage[k]//v)
		except : c.append(0) #No such ingredient in storage
	return min(c)	
		
# -- main --
recipe = {"flour": 500, "sugar": 200, "eggs": 1} 
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}

servings_count = servings(recipe, available) #function call

print("Recipe:", recipe)
print("Storage:", available)
print("Avialible servings is", servings_count)