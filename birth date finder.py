name = input("what is your name?  ")
print("hello " + name + " This is a trial program to output your your birthday")
import calendar
dy = int(input("Please type in the day: "))
mth = int(input("Please type in the month: "))
Age = int(input("Please type in your age: "))
ext = ['1st month of','2nd month of','3rd month of', '4th month of', '5th month of', '6th month of', '7th month of', '8th month of', '9th month of', '10th month of', '11th month of', '12th month of']

ordinal = ext[mth - 1]
from _datetime import datetime
currentYear = datetime.now() .year
yr = currentYear - Age
exact_date = calendar.weekday(yr, mth, dy)

if(exact_date == 0):
         print("you were born on a Monday in the ", ordinal, yr)


if(exact_date == 1):
         print("you were born on a Tuesday in the", ordinal, yr)



if(exact_date == 2):
         print("you were born on a Wednesday in the" , ordinal, yr)




if(exact_date == 3):
         print("you were born on a Thursday in the", ordinal, yr)



if(exact_date == 4):
         print("you were born on a Friday in the", ordinal, yr)



if(exact_date == 5):
         print("you were born on a Saturday in the", ordinal, yr)




if(exact_date == 6):
         print("you were born on a Sunday in the", ordinal, yr)
again =input('Do you want to find another birth date? (y/n):')
if again =="n":
    quit
if again =="y":
 print('here we go again')
import calendar
dy = int(input("Please type in the day: "))
mth = int(input("Please type in the month: "))
Age = int(input("Please type in your age: "))
ext = ['1st month of','2nd month of','3rd month of', '4th month of', '5th month of', '6th month of', '7th month of', '8th month of', '9th month of', '10th month of', '11th month of', '12th month of']

ordinal = ext[mth - 1]
from _datetime import datetime
currentYear = datetime.now() .year
yr = currentYear - Age
exact_date = calendar.weekday(yr, mth, dy)

if(exact_date == 0):
         print("you were born on a Monday in the ", ordinal, yr)


if(exact_date == 1):
         print("you were born on a Tuesday in the", ordinal, yr)



if(exact_date == 2):
         print("you were born on a Wednesday in the" , ordinal, yr)




if(exact_date == 3):
         print("you were born on a Thursday in the", ordinal, yr)



if(exact_date == 4):
         print("you were born on a Friday in the", ordinal, yr)



if(exact_date == 5):
         print("you were born on a Saturday in the", ordinal, yr)




if(exact_date == 6):
         print("you were born on a Sunday in the", ordinal, yr)
again =input('Do you want to find another birth date? (y/n):')
if again =="n":
    quit
if again =="y":
    input("please press <enter> to quit program")



