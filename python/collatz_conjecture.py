n = int(input("Enter a number: "))

def collatz(n):
    count = 0
    while n != 1:
        count += 1
        if n % 2 == 0: # Even Number
            n = int(n/2)
        else: # Odd Number
            n = 3*n + 1
        print(n)
    return count

print("With", n, "we reached 1 in", collatz(n), "steps.")
