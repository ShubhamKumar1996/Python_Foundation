# Total number of cars we have 100
cars = 100

# Number of person that can sit in car is 4
space_in_a_car = 4.0

# Total number of drivers available is 30.
drivers = 30

# Total number of passengers is 90.
passengers = 90

# Number of cars for which we don't have any driver.
cars_not_driven = cars - drivers

# Number of cars for which we have drivers.
cars_driven = drivers

# Total number of person who can sit in all the cars which have driver.
carpool_capacity = cars_driven * space_in_a_car

# Average number of person that should sit in a car.
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
