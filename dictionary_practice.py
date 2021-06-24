# STEP 2 #
dict_food = {"chicken":1.59, "beef":1.99, "cheese":1.00, "milk":2.50}

# STEP 3 #
Colors = {"green":1, "blue":2, "red":3, "pink":4}
Cheapest_food = dict_food["cheese"]
Favorite_colors = Colors["green"]

# STEP 4 - 5 #
print(Cheapest_food)
print(Favorite_colors)

# STEP 6 #
shoe_counts = {"Jordan_13":1, "Yeezy":8, "Foamposite":10, "Air_Max":5, "SB_Dunk":20}

# STEP 7 #
shoe_counts["Jordan_13"] = 5
shoe_counts["Yeezy"] = 13
shoe_counts["Foamposite"] =14
shoe_counts["Air_Max"] = 9
shoe_counts["SB_Dunk"] =24

print(shoe_counts)

#STEP 8 # 
shoe_counts["Jordan_1"] = 7
shoe_counts["Jordan_4"] = 8
shoe_counts["Jordan_11"] = 9

print(shoe_counts)

#STEP 9 #

del shoe_counts["Jordan_11"]
del shoe_counts["Jordan_4"]

print(shoe_counts)