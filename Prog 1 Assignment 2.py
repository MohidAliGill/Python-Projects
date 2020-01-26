##Name: Mohid Ali Gill
##Roll No: 21-10842

##Question P3.12

grade=input("Enter a letter grade:")
if grade=="A+":
    print("The numeric value is 4.0.")
elif grade=="A":
    print("The numeric value is 3.7.")
elif grade=="A-":
    print("The numeric value is 3.4.")
elif grade=="B+":
    print("The numeric value is 3.3.")
elif grade=="B":
    print("The numeric value is 3.0.")
elif grade=="B-":
    print("The numeric value is 2.7.")
elif grade=="C+":
    print("The numeric value is 2.3.")
elif grade=="C":
    print("The numeric value is 2.0.")
elif grade=="C-":
    print("The numeric value is 1.7.")
elif grade=="D+":
    print("The numeric value is 1.3.")
elif grade=="D":
    print("The numeric value is 1.0.")
elif grade=="D-":
    print("The numeric value is 0.7.")
elif grade=="F":
    print("The numeric value is 0.0.")
else:
    print("Wrong grade entered")

##Question P3.16

str1=input("Enter string 1:")
str2=input("Enter string 2:")
str3=input("Enter string 3:")
if str1[0]<str2[0] and str1[0]<str3[0]:
    a=str1
    if str2[0]<str3[0]:
        b=str2
        c=str3
    else:
        b=str3
        c=str2
elif str2[0]<str1[0] and str2[0]<str3[0]:
    a=str2
    if str1[0]<str3[0]:
        b=str1
        c=str3
    else:
        b=str3
        c=str1
else:
    a=str3
    if str1[0]<str2[0]:
        b=str1
        c=str2
    else:
        b=str2
        c=str1
print(a)
print(b)
print(c)

##Question P3.27

year=int(input("Enter year:"))
if (year%4==0 or year%400==0) and (year%100!=0):
    print ("Leap Year")
else:
    print ("Not a leap year")

##Question P3.33

savedpin="1234"
pin=input("enter pin")
if pin==savedpin:
    print("Your PIN is correct")
elif pin!=savedpin:
        print("Your pin is incorrect")
        pin=input("Enter pin again")
        if pin==savedpin:
            print("pin correct")
        else:
            print("Your pin is incorrect")
            pin=input("Enter pin again")
            if pin==savedpin:
                print("Pin correct")
            else:
                print("Card blocked")

##Question P4.12

word=input("Enter a word:")
wordlen=len(word)
sublen=1
start=0
for i in range(wordlen):
    start=0
    while start + sublen <= wordlen:
        print (word[start:start+sublen])
        start+=1
    sublen +=1
           
##Question P4.13

number=int(input("Enter number"))
while number!=0:
    print(number%2)
    number=number//2

##Question P4.14

from sys import exit
from math import sqrt
count = 0
sum1 = 0
sumsquares = 0
stop = False
while not stop:
    try:
        inputN=float(input("Value:"))
    except ValueError:
        stop = True
        break
    count+=1
    sum1 +=inputN*inputN
if count<=2:
    exit()
avg=sum1/count
stdDevAvg=(sum1*sum1)/count
standDev=sqrt((sumsquares-stdDevAvg)/(count-1)
print ("There are",count,"value.")
print("The average is",avg, "and the standard deviation is",standDev)



print("There are", count," values")

print("The average is", average," and the standard deviation is", Dev)

##Question P4.17

num=int(input("Enter number:"))
for i in range(3,num + 1):
       for j in range(2,i):
           if (i % j) == 0:
               break
       else:
           print(i)
