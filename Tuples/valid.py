'''
7. Product Dimension Validator
A shipping company accepts packages if the sum of dimensions (Length, Width, Height) is less than 100.
Given a tuple of 3 integers, return 'Accept' or 'Reject'.

'''

dim  = tuple(map(int, input("Enter lenght, width, height: ").split()))

flag = True
for value in dim:
    if value > 100:
        flag = False
        break
if flag:
    print("Accept")
else:
    print("Reject")

'''

if all(value < 100 for value in dim):
    print("Accept")
else:
    print("Reject")

'''