'''
4. Config Integrity Check
System configurations are stored in a tuple to prevent accidental changes. Write a script to count how
many times the value 'Enabled' appears in the config tuple.
'''


#sc = ('Enabled', 'Disabled', 'Enabled')
sc = ('Disabled', 'Pending')

count = 0

for value in sc:
    if value == "Enabled":
        count = count + 1

print(count)
