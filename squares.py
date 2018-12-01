#squares.py 
sqr_list = [i * i for i in range(1, 7)]
format_str = '{:>3}  {:>3}  {:>3}' 
old_val = 0 
for i, item in enumerate(sqr_list, 1):
    print(format_str.format(i, item, item - old_val))
    old_val = item 
fib_list = [1, 2, 4, 5, 8, 13, 21, 34, 55, 89, 144]
