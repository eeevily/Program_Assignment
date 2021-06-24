
# STEP 2 #

cities = ["Oakland","Atlanta","New_York_City","Seattle","Memphis","Miami","Boston","Los_Angeles","Denver","New_Orleans"]
print(cities)

# STEP 3 #
foods = ["chip","cake","noodle","rice","taco","pizza","burger","milk","candy","fries"]
print(foods)

favorite_cities = cities[2:5]
print(favorite_cities)

# STEP 4 #
last_four_cities = cities[0:4]
last_four_foods = foods[0:4]
print(last_four_cities)
print(last_four_foods)

# STEP 5 #
cities[0] = "San_Francisco"
cities[2] = "Brooklyn"
cities[7] = "Hollywood"
cities[5] = "Tampa"
print(cities)

# STEP 6 #
cities.append("Oakland")
cities.extend(["New_York_City","Los_Angeles"])
cities.insert(0,"Miami")
print(cities)

# STEP 7 #
del cities[2]
del cities[3]
del cities[4]
print(cities)

