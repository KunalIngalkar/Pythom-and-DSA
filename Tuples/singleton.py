'''
9. The 'Singleton' Error
You are given an input. Your task is to ensure it is returned as a tuple. If it's a single integer `n`, return
`(n,)`.

'''

t  = tuple(map(int, input("Enter values ").split()))
print(t)