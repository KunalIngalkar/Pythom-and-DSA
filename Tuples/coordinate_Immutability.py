'''1. Coordinate Immutability

A GPS system stores location as (latitude, longitude). Write a function that takes a list of coordinate tuples
and returns only those that are within the 'Northern Hemisphere' (Latitude > 0).

'''

def nh(coords):
    result = []

    for lat, lon in coords:
        if lat > 0:
            result.append((lat, lon))
    return result

standard = [(18.5, 73.8), (-33.8, 151.2)] 
equator = [(0, 78.9)]
empty_list = []

print(nh(standard))
print(nh(equator))
print(nh(empty_list))