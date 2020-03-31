#integer
cars = 100
#float
space_in_a_car = 4.0
#number of people driving
drivers = 30
#number of people needing to be driven that are not drivers
passengers = 90
# results = 100 - 90
cars_not_driven = cars - drivers
#a car must be driven by one person
cars_driven = drivers
#number of seats available = 30 * 4
carpool_capacity = cars_driven * space_in_a_car
#90 passengers divided by 30 = 3
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
