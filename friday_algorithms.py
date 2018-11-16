# rand_student_index = random.randint(0,len(variable name here)-1)
# current_student = students[rand_student_index]

# students.remove(current_student)


# function: a piece of code that we intend to use over and over.
#     - functions in python are called definitions
#         def get_student():


# _____________
# Algorigthm 1:
# _____________
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

# total_sum = 0
# for i in range(1000):
#     if (i % 3 == 0 or i % 5 == 0):
#         total_sum = total_sum+i
# print total_sum

#----------------
# Algorithm 2:
#----------------
# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, 
# the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the 
# even-valued terms.
    #a while statement is used when you have no idea how long the code should run. If you have a known/fixed ending point, 
    #then use a for loop.
sum_total = 0
fib1 = 1
fib2 = 2
while(sum_total < 4000000):
    new_fib = fib1 + fib2
    fib1 = fib2
    fib2 = new_fib
    if(fib1 % 2 == 0):  #here, we are determining if our number will divide evenly by 2; a remainder of 0
        sum_total += fib1 # OR sum_total = sum_total + fb1
print sum_total

