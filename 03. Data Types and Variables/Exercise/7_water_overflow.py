number_of_inputs = int(input())

water_tank_max_capacity = 255
water_tank_current_capacity = 0

for i in range(number_of_inputs):
    current_amount_of_water = int(input())
    water_tank_current_capacity += current_amount_of_water
    if water_tank_current_capacity > water_tank_max_capacity:
        print("Insufficient capacity!")
        water_tank_current_capacity -= current_amount_of_water
print(water_tank_current_capacity)