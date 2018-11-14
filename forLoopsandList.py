# # for loops expect a starting and ending point.
# # The ending point does not get counted, it will stop when/BEFORE it gets there.
# i = the thing that will change each time through.
for i in range(1, 10): #stop when it sees 10, not on the number 10. if you want ten, then you need to put 11.
    print i

 #A 3rd argument you can  hand, is called "step"

for i in range(1, 10, 2):
    print i


#=====LISTS========
#IN PYTHON, a list is just a list of variables; any other language, it would be an array.

student1 = "Brian"
student2 = "Brandon"
student3 = "Zac"
student4 = "J.R."

print student2

# A list groups "stuff" variables together and indexes them by number.
# A list INDEX ALWAYS starts at 0
# a list is made with []
# when making a list, separate each with an ","
students = ["Brian", "Brandon", "Zach", "J.R."]
print students[0]
print students[-1]
print students[-4] #negitave numbers start with 1, not zero so in this case, it would list "Brian"

teams = [
    ["Falcons",
    "Panthers",
    "Bucs",
    "Saints"
    ],
    ["Patiots",
    "Eagles",
    "Bills",
    "49ers"]
]
print teams[0][0]

#All list, have a length you can find with LEN()
numOfStudents = len(students)
for i in range(0, numOfStudents):
    print students[i]

# A TUPLE is a list who;s elements CANNOT be changed.
# A tuple is made with () instead of []
students = ("Michael", "Matt", "Cody", "ConnEr")
    # if you try to reassign Matt with Christopher, like students[1] = "Christopher"   --> this will not work on TUPLES
    # create a Tuple and it will work like a const; you can't change.

#Create an empty list and to add to it, you use "APPEND"; in javascript this would be a "push"
atlanta_teams= []
atlanta_teams.append("Falcons")
atlanta_teams.append("Braves")
atlanta_teams.append("Hawks")
atlanta_teams.append("Thrashers")

#HEY! Wait a minute, the Thrashers left years ago
atlanta_teams.pop() #this will remove the last of the list.
print atlanta_teams
    #if you did, .pop(3), it would remove the 3rd element in  a list.
atlanta_teams.append("United") #ADDS TO THE LAST PLACE
print atlanta_teams

#A sort method for list! (used for NATURAL order; the order it would normally be in)
atlanta_teams.sort()
print atlanta_teams #THIS WILL CHANGE UP OR MESS UP YOUR ORIGINAL ORDER IT WAS ORIGINALLY EXPECTED.

sortedAtlantaTeams = sorted(atlanta_teams) #this keeps the list sorted specifically vs. when .sort() and creating a new list.
print sortedAtlantaTeams

# reverseSort is the .reverse()
sortedAtlantaTeams.reverse()
print sortedAtlantaTeams


#If you have a string and want to turn it into a list, use SPLIT
#split!! Requires a delimiter is what you want the split to look and each time it finds it, it will create a new element.
reindeer = "Dasher, Dancer, Prancer, Vixon"
reindeerAsAList= reindeer.split(', ') # (',') this is a delimiter, I had to input the extra space so it looks for a comma and then a space.
print reindeerAsAList

#if you want part of a list, you use [x:y]
#  this will create a COPY of thge array, It will not change the original. It will start copying the 1st number and will stop before the last number.
dancerPrance = reindeerAsAList[1:3] #start at 1 and copy the first position and second position and end there. Start at one and end before 3
print dancerPrance