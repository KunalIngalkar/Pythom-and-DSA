a,b,c = map(int,input().split())

if a == b == c:
    print("Equilateral Triangle")
elif a == b or b == c or c == a:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")