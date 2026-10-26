'''
   * * * * *
    * * * *
     * * *
      * *
       *
n = 5
'''

#def count_bowls(n):
#    count = 0
#    n # - number of rows

from time import time

def count_bowls_loop(n):
    count = 0
    for row in range(n, 0, -1):
        count += row
    return count


def count_bowls_recursive(n):
    if n == 1:
        return 1
    else:
        prev_sum = count_bowls_recursive(n - 1)
        cur_sum = prev_sum + n
        return cur_sum

def count_bowls_sequence(n):
    return int((n * (n + 1)) / 2)


def time_func(func, n):
    t0 = time()
    print(f'Running {func.__name__} with n = {n}')
    res = func(n)
    t1 = time()
    elapsed_time = round(t1 - t0, 8)
    print(f'Result: {res}')
    print(f'Elapsed time: {elapsed_time}')


#n = 998
n = 250000000
#print(f'Count bowls loop for n={n}: {count_bowls_loop(n)}')
#print(f'Count bowls recursive for n={n}: {count_bowls_recursive(n)}')

time_func(count_bowls_loop, n)
# Computational complexity O(1)
#time_func(count_bowls_recursive, n)
time_func(count_bowls_sequence, n)
# Computational complexity O(n)
