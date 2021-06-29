# STEP 2 #
food = {"chicken":1.59, "beef":1.99, "cheese":1.00, "milk":2.50}

# STEP 3 #
Colors = {"green":1, "blue":2, "red":3, "pink":4}
Cheapest_food = food["cheese"]
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

# STEP 9 #

del shoe_counts["Jordan_11"]
del shoe_counts["Jordan_4"]

print(shoe_counts)

# LAB 4 Part 2 #

def total_price(food1, food2):
    total = food[food1] + food[food2]
    return total


goodToGo = True 
while (goodToGo):
    input1 = input("pls give us a food")
    if (input1 in food):
        print("ok")
        input2 = input("give us a 2nd food")
    if (input2 in food):
            print ("the total price is", total_price("beef","cheese"))
            break
else:
    goodToGo = False

# LAB 4 Part 3 #

def clearanceSale(d,updater):
  d1 = {"Jordan_13":shoe_counts["Jordan_13"]/updater}
  d.update(d1)
  d2 = {"Yeezy":shoe_counts["Yeezy"]/updater}
  d.update(d2)
  d3 = {"Foamposite":d["Foamposite"]/updater}
  d.update(d3)
  d4 = {"Air_Max":d["Air_Max"]/updater}
  d.update(d4)
  d5 = {"SB_Dunk":d["SB_Dunk"]/updater}
  d.update(d5)
  return (shoe_counts)
    

print(clearanceSale(shoe_counts,5))

# STEP 6 #
nba_player = {1:{"name":"Bazemore",  "jerseyNum" :26},
              2:{"name":"Bell",      "jerseyNum":7},
              3:{"name":"Curry",     "jerseyNum":30},
              4:{"name":"Green",     "jerseyNum":23},
              5:{"name":"Lee",       "jerseyNum":1},
              6:{"name":"Looney",   "jerseyNum":5}}

def largestJerseyNumber (nba_player):
    largestJerseyNumber =0

    for x in range(1,6):
         print(nba_player[x]['jerseyNum'])
         if (nba_player[x]['jerseyNum'] > largestJerseyNumber):
             largestJerseyNumber = nba_player[x]['jerseyNum']
             print(nba_player[x]['jerseyNum'])

    print(largestJerseyNumber)

largestJerseyNumber(nba_player)
