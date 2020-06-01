# this sets the variable cars to the integer of 100
cars = 100

# this sets space_in_a_car to the float of 4.0
space_in_a_car = 4.0

# this sets drivers to the integer of 30
drivers = 30

# this sets passengers to the integer of 90
passengers = 90

# this takes 100-30=70 cars not driven
cars_not_driven = cars - drivers

# this defines cars_driven as 30
cars_driven = drivers

# this tells you that 30 cars driven * 4.0 = 120.0
carpool_capacity = cars_driven * space_in_a_car

# this takes 90 passengers and divides it by how many cars are driven to get how many people per car
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
