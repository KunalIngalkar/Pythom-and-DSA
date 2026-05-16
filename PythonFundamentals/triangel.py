'''
6. Triangle Validity & Classification: Input three sides. Check if the triangle is valid. If valid,
classify it as Equilateral, Isosceles, or Scalene.
'''

a,b,c = map(int,input().split())

if a == b == c:
    print("Equilateral Triangle")
elif a == b or b == c or c == a:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")