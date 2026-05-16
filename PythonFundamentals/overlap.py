'''
4. Logical Overlap: Given two intervals [a, b] and [c, d], write a single logical expression
using comparison operators to detect if they overlap.
'''

a,b = map(int,input().split())
c,d = map(int,input().split())

if (a <= d) & (c <= b):
    print("Overlap")
else:
    print("Not Overlap")

