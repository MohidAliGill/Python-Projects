##Comp 102: Assignment 1
##You are suppose to type in your code where is says:
##    'your code here'


##Question 1: Operator Precedence and Associativity
##Given the question:
##    p) 5 * 6 + 9
##your answer is going to be of the form:
##    p = '(5*6) + 9'
##Note that the answer is in the form of a string

a = '(((5 * 6) / 7) * 8) / 9'
b = '(((5 * 6) / (7 ** (8 / 2))) * 7) + 4'
c = '((True or (False and True)) or (True == False)) or False'
d = '((456 % 10) + ((456 // 10) % 10)) + ((456 // 100) % 10)'

##Question 3:
print ("   ///// ")
print ('  +"""""+')
print (" (| o o |)")
print ("  |  ^  |")
print ("  | --- |")
print ("  +-----+")
##Question 4:
"""
When we assign the value 6 to x an object is created in the global frame
named x and containing value 6
Then we assign the value 9 to y another object is created named y and
containing the value 9
Now another object is created named z and calls the other two objects x and y,
adds thier values i.e: 15,  together and stores the result
Then the value of x is replaced by value of z, the old value of x is deleted
In the last step the value of y is replaced with value of z and old value of y
is deleted
"""
##Question 5:
##Part a:

chic = 20
lettuce = 30
tomato = 50

##Write your formula in terms of the above varialbes.
##Note the answers are not in string form,see the formula
##for volume of a cylinder in the assignment.

max_burgers = 'your code goes here'


##Part b:

r = 3.7
h = 8.9

cone_area = math.pi * r * (r + math.sqrt((h*h) + (r*r)))
##Question 6:

num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))
print("Sum:",(num1 + num2))
print("Difference:",(num1 - num2))
print("Product:",(num1 * num2))
print("Average:",((num1+num2)/2))
print("Distance:",abs(num1-num2))
print("Maximum:",max(num1,num2))
print("Minimum:",min(num1,num2))


##Question 7:
time1 = int(input("Please enter the first time:"))
time2 = int(input("Please enter the second time:"))
hr = (time2 - time1)//100
minutes=((time2-time1)-(hr*100))
print(hr,"hours",minutes,"minutes")

##Question 8:
import math
RH=float(input("Enter Relative Humidity"))
T=float(input("Enter Temperature"))
a,b = 17.27,237.7
f=((a*T)/(b+T))+(math.log(RH))
dewPointTemp=(b*f)/(a-f)
print(dewPointTemp)


##Question 9:
##example format for answere:
##
##     x = 8*9/6 + 10

a = (3*5)/(2+3)
b = ((7 + 9)**0.5)/2
c = (4-7)**3
d = (-19+100)**(1/4)
e = 6%4    
