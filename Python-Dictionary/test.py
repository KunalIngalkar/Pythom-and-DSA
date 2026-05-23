nums =[2,7,11,15]
target = 18
'''for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == target:
            values = [i, j]   
            print(values)
  '''

for i in range(len(nums)-1 ):
    if nums[i] + nums[i+1] == target:
        val = [i, i+1]  
        print(val)