'''

5. Database Row Unpacking
A database query returns a row as (User_ID, Username, Email, City). Unpack this tuple into variables and
return a formatted string: 'User [Username] lives in [City]'.

'''


row = (1, 'prof_ram', 'ram@logic.com', 'Pune') 

print("User" , row[1], "lives in", row[3])