# len(): Determine the length of a list
# .append(): Add an item to a list
# .pop(): Remove the last item in a list
# .index(): This method searches for the value and returns the index of that item in the list
# max(): Return the largest number in the list
# min(): Return the smallest number in the list
# .sort(): Sort a list of strings in alphabetical order and a list of numbers in numeric order
# .sort(reverse=True): Sort a list in reverse order

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
# print(planets)
# print("There are", len(planets), "planets")

# planets.append("Pluto")
# print("Actually, there are", len(planets), "planets")
# print(planets[-1], "is the last planet")

user_planet = input("Please enter the name of the planet (with a capital letter to start): ")
planet_index = planets.index(user_planet)
print("Here are the planets closer than " + user_planet)
print(planets[0:planet_index])
print("Here are the planets futher than " + user_planet)
print(planets[planet_index + 1:])