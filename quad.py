'''3. Coordinate Geometry: Given x and y coordinates, find the quadrant. Handle cases where
the point lies on the X-axis, Y-axis, or Origin.'''


a, b = map(int, input().split())
if a > 0 and b > 0:
    print("1st Quadrent")
elif a < 0 and b > 0:
    print("2nd Quadrent")
elif a < 0 and b < 0:
    print("3rd Quadrent")
elif a > 0 and b < 0:
    print("4th Quadrent")
elif a == 0 and b == 0:
    print("orign")
else:
    print("on an axis")