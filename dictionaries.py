#DICTIONARIES
#   - JUST LIKE LIST; 
# EXCEPT... INSTEAD OF NUMBERED INDICIES, THEY HAVE ENGILISH INDICIES;
# a dictionary is similar to a key. in a normal list and you want to know what's greg's job is, no one knows what greg[3] means

# DICTIONAIRES ARE SIMPLY A LIST WITH VALUES, KEY VALUE PAIRS;


# greg = [
#     "Greg",
#     "Male",
#     "Tall",
#     "Developer"
# ]

greg = {
    "name": "Greg",
    "gender": "Male",
    "height": "Tall",
    "job": "Developer"
}
print greg["name"]
print greg["job"]   ##Prints out greg's name and Greg's job.


# MAKING A NEW DICTIONARY (can't use append)
zombie = {} #dictionary
zombies = [] #list
zombie["weapon"] = "fist"
zombie["health"] = 100
zombie["speed"] = 10

print zombie
print zombie["weapon"]

# for key,value in zomnie.items(): 
#     print "Zombie has a key of %s witgh a value of %s" % (key, value)


zombies = []
zombies.append({
    "name": "Hank",
    "weapon": "bat",
    "speed": 10
})

zombies.append({
    "name": "Willie",
    "weapon": "axe",
    "speed": 3,
    "victims": [
        "squirrel",
        "rabbit",
        "racoon"
    ]
})
print zombies[0]["weapon"]
print zombies[1]["victims"][1]
