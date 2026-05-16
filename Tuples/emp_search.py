'''
2. Employee Records Search
An HR database stores employee data as (ID, Name, Dept). Given a tuple of these records, find the index
of the employee with ID 105. If not found, return -1.
'''
#emp = ((101, 'Ram', 'IT'), (105, 'Neha', 'HR'))
emp = ((101, 'Ram', 'IT'),) 


index = -1

for i in range (len(emp)):
    if emp[i][0] == 105:
        index = i
        break
print(index)