#sort.py 
a_list = [] 
while True:
    str1 = input('Enter a name: ')
    if str1 == '': # If string is empty, 
        break 
    a_list.append(str1) 
a_list.sort()
print('Here is the alpha sorted list...')
for str1 in a_list:
    print(str1)
