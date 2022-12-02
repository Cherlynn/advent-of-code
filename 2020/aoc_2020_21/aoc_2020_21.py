
import re

inputfile_name = "aoc_2020_21_input"
inputfile = open(inputfile_name, "r")
lines = inputfile.readlines()
inputfile.close()

allergens = {} #dictionary where key = allergen, and value = list of sets of ingredient lines where the line contains the particular allergen
cannot_contain_allergens = {} #dictionary where key = allergens, and value = set of ingredients that cannot contain the respective allergen
can_contain_allergens = {}
allergen_mapping = {}
all_ingredients = set()

for line in lines:
    allergen_line = re.search("\(contains (.+)\)", line).group(1)
    allergen_list = [allergen.strip() for allergen in allergen_line.split(',')]
    ingredients_line = line.split('(')[0]
    ingredients_set = {ingredient for ingredient in ingredients_line.split()}
    all_ingredients = all_ingredients.union(ingredients_set)
    for allergen in allergen_list:
        if allergen in allergens:
            allergens[allergen].append(ingredients_set)
        else:
            allergens[allergen] = []
            allergens[allergen].append(ingredients_set)
    #print(allergen_list)
    #print(ingredients_set)

#print(allergens)

for allergen in allergens:
    ingredients_that_can_contain_allergen = allergens[allergen][0].intersection(*allergens[allergen])
    ingredients_that_cannot_contain_allergen = all_ingredients.difference(ingredients_that_can_contain_allergen)
    cannot_contain_allergens[allergen] = ingredients_that_cannot_contain_allergen
    can_contain_allergens[allergen] = ingredients_that_can_contain_allergen
    print(ingredients_that_can_contain_allergen, allergen)
    #print(cannot_contain_allergens[allergen])
    #print(ingredients_that_cannot_contain_allergen)

ingredients_that_cannot_contain_any_allergen = next(iter(cannot_contain_allergens.values())).intersection(*cannot_contain_allergens.values())
#print(ingredients_that_cannot_contain_any_allergen)
#print(len(ingredients_that_cannot_contain_any_allergen))

count = 0
for line in lines:
    ingredients_line = line.split('(')[0]
    ingredients_set = {ingredient for ingredient in ingredients_line.split()}
    #print(ingredients_that_cannot_contain_any_allergen.intersection(ingredients_set))
    num_ingredients_that_cannot_contain_any_allergen = len(ingredients_that_cannot_contain_any_allergen.intersection(ingredients_set))
    count += num_ingredients_that_cannot_contain_any_allergen

# Map allergens to ingredients
while len(allergen_mapping) < len(can_contain_allergens):
    for allergen in can_contain_allergens:
        if len(can_contain_allergens[allergen]) == 1:
            ingredient = can_contain_allergens[allergen].pop()
            allergen_mapping[allergen] = ingredient
            # print(allergen, ingredient)
            # remove ingredient from all other allergens
            for other_allergen in can_contain_allergens:
                can_contain_allergens[other_allergen].discard(ingredient)

print("Part 1:",count)
print("Part 2")

sorted_allergen_ingredients = ""
for allergen in sorted(allergen_mapping.keys()):
    sorted_allergen_ingredients += allergen_mapping[allergen] + ","
print(sorted_allergen_ingredients)

