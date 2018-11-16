#Uppercase a String
aString = "connor";
print aString.upper()
print aString

#Capitalize a String
print aString.capitalize()

#Reverse a String
#Given a string, print the string reversed
print aString[::-1]

aStringAsList = list(aString)
print aStringAsList

#Now, since you made it a list, you can reverse it...
aStringAsList.reverse()
print "".join(aStringAsList)

#Print the first charactaer of "connor" which is listed as "aString"
print aString[0]

#Printing a Strings list (len is the key to length)
lengthOfString = len(aString)
for i in range(0, lengthOfString):    ## don't forget your "   :   "
    print aString[i]

reverserdString = "";
for i in range(0, lengthOfString):
        reverserdString += aString[lengthOfString - (i + 1)] 
        print reverserdString

leetString = "Sean McQuaid"
newString = leetString.upper() #convert it to uppercase so you don't have to compare upper case and lower case. so all cases are the same.
leetA = newString.replace("A", "4")
leetE = leetA.replace("E", "3")
leetG = leetE.replace("G", "6").replace("I", "1")


#append is push in python.

# MAKING A TRIANGLE
p = int(raw_input("How big is your triangle?")); #make sure it's an integer
for i in range(1,p+1,2):
    print "-" * p + i * "*"
    # print i to see iterations per loop
    p -= 1



