#1. Leap Year Algorithm: Write a script to check if a year provided by the user is a leap year.
#Ensure century years are only leap years if divisible by 400.

year = int(input())

if(year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")