#fact2.py 
n = int(input('Calculate factorial for which n? ')) 
prod = 1 
for i in range(1, n + 1): # For 1 to n, inclusive
    prod = prod * i 
print('The result is: ', prod)
