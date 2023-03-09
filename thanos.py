#code

initial_position = 0
distance_to_wakanda = 50
food_supply = 10

distance_to_first_planet = 10
food_on_first_planet = 20

distance_to_second_planet = 30
food_on_second_planet = 40

#calculate the number of planets Thanos needs to stop at

remaining_distance = distance_to_wakanda - initial_position
number_of_planets = 0

if food_supply >= remaining_distance:
    number_of_planets = 0
else:
    food_needed = remaining_distance - food_supply
    if food_on_first_planet >= food_needed:
        number_of_planets = 1
    else:
        number_of_planets = 2

print("Thanos needs to stop at", number_of_planets, "planets.")