a,b = map(int,input().split())
c,d = map(int,input().split())

if (a <= d) & (c <= b):
    print("Overlap")
else:
    print("Not Overlap")

