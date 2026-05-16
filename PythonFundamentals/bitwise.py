''' 2. Binary Power Check: Use Bitwise Operators to determine if an integer is a power of 2. 
You are restricted from using any loops or external libraries. '''

val = int(input())

if val & (val - 1) == 0 and val !=0:
    print("True")
else:
    print("False")