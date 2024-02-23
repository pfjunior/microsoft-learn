# planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

# while loop
new_planet = ""
planets = []

while new_planet.lower() != "done":
    if new_planet:
        planets.append(new_planet)
    
    new_planet = input("Enter a new planet, or done when done: ")
# print(planets)

# for loop
for planet in planets:
    print(planet)