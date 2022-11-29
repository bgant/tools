import time
from functools import lru_cache

# Number of steps to divide any number down to 1
@lru_cache(maxsize=100)
def collatz(n):
    count = 0
    while n != 1:
        count += 1
        if n % 2 == 0: # Even Number
            n = int(n/2)
        else: # Odd Number
            n = 3*n + 1
        #print(n)
    return count

# Which numbers in a range have the most steps
def max_collatz_steps(i):
    max = 1
    for n in range(1,i+1):
        if collatz(n) > max:
            max = collatz(n)
            print(f"{n} takes {max} steps")

if __name__ == '__main__':
    start = time.perf_counter()
    n = 0
    while n <= 0:
        n = int(input("Enter a positive integer: "))
    else:
        max_collatz_steps(n)
    end = time.perf_counter()
    print(f"{end - start} seconds")

