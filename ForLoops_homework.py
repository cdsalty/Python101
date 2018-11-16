# Using a for loop and the range function, print out the numbers between 1 and 10 inclusive, one on a line.
for i in range(1,11):
    print i

# n to m
# Same as the previous problem, except you will prompt the user for the number to start on and the number to end on

beginning = raw_input("What is your starting number? ")
end = raw_input("What is your ending number? ")
for i in range(int(beginning), int(end)):
    print i

#Print each odd number between 1 and 10 inclusive
for i in range(1,10): #determines the number of rows we will have
    if i % 2 == 1: #if the number divided by 2 leaves you a remainder, then print it.
        print i


# Print a 5x5 square of * characters. 

for i in range(1, 6):
    print "*****"

#Print a NxN square of * characters. Prompt the user for N.
squareSize = int(raw_input("How large do you want your square? "))
for i in range(1, squareSize + 1):
    print "*" * squareSize

#Given a height and width, input by the user(**CREATE VARIABLES**), print a box consisting of * characters as its border.
height = int(raw_input("What would you like to select as your height? "))
width = int(raw_input("What would you like to select as your width?"))
for i in range(0, height):
    if i == 0: #on row zero, what are you doing?
        print width * "*" #printing width times the stars
    elif i == (height -1):
        print width * "*"
    else:
        print "*" + ((width -2) * "$") + "*"


#Khanh, Brandon, Bryan
p = int(raw_input("How big is your triangle?")); #make sure it's an integer
for i in range(1,p+1,2):
    print "-" * p + i * "*"
    # print i to see iterations per loop
    p -= 1