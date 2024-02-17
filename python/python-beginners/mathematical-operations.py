first_planet_input = input("Enter the distance from the sun for the first planet in km: ")
second_planet_input = input("Enter the distance from the sun for the second planet in km: ")

first_planet = int(first_planet_input)
second_planet = int(second_planet_input)

distance_km = abs(first_planet - second_planet)
print(distance_km)

distance_mi = abs(distance_km / 1.609344)
print(distance_mi)



