#guessing.py
import random 
n = random.randin(1, 50)
while True: 
    ans = int(input('Enter your guess: '))
    if ans == n:
        print('Success! You win!;)
        break 
    elif ans > n:
        print('Too high.')
    else: 
        print('Too low.')
