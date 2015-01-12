#Variables

# cars
cars = 100

#Car capacity
space_in_a_car = 4

#drivers
drivers = 30

# passengers 
passengers = 90

# How many cars are parked
cars_not_driven = cars - drivers

#Cars in use
cars_driven = drivers

# Num of ppl that can be driven at a time
carpool_capacity = cars_driven * space_in_a_car

# Avg number of ppl needed per car
average_passengers_per_car = passengers/cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
