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