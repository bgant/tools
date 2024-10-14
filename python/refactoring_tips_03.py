### Use zip
# instead of
a = [1, 2, 3]
b = ["a","b","c"]
for idx in range(len(a)):
    print(a[idx], b[idx])

# do this
a = [1, 2, 3]
b = ["a", "b", "c"]
for val1, val2 in zip(a, b, strict=True):
    print(val1, val2)

### Think lazy, use a generator
# instead of
events = [("learn", 5), ("learn", 10), ("relaxed", 20)]
minutes_studied = 0
for event in events:
    if event[0] == "learn":
        minutes_studied += event[1]

# do this
study_times = (event[1] for event in events if event[0] == "learn")
  # () creates generator / [] creates comprehension
minutes_studied = sum(studytimes)
  # generator empties out values as they are used / comprehension is list

### Use itertools: https://docs.python.org/3.12/library/itertools.html
from itertools import islice
first_five_lines = islice(lines, 5)
for line in first_five_lines:
    print(line)

### Use any() and all()
any_true = any([False, False, True])
all_true = all([True, True, True])

### Avoid long if/elif statements 
def do_one(x):
    print("one: x*1 = ", x*1)
def do_two(x):
    print("two: x*2 = ", x*2)
def do_three(x):
    print("three: x*3 = ", x*3)
def do_default(x):
    print("default: x = ", x)
x = 2

# instead of
if x == 1:
    do_one(x)
elif x == 2:
    do_two(x)
elif x == 3:
    do_three(x)
else:
    do_default(x)

# do this
actions = {1: do_one, 2: do_two, 3: do_three}  # Dictionary of functions
actions = actions.get(x, do_default(x))        # pick function 1,2,3 or default
action(x)

### Count with Counter()
from collections import Counter
my_list = [10, 10, 5, 2, 9, 9, 9]
counter = Counter(my_list)
print(counter)
print(counter[10])  # 2
print(counter.most_common(1))  # number of most_common items

### Execute command and capture output
import subprocess
result = subprocess.run(['ls','-al'], capture_output=True, text=True)
print(result)
print(result.stdout)
print(result.stderr)

### Python 3.10 introduced Pattern Matching (case statements)
def http_error(status):
    match status:
        case 400:
            print("Bad Request")
        case 401 | 403 | 405:
            print("Not Allowed")
        case 418:
            print("I'm a teapot")
        case _:
            print("Something's wrong with the internet")

### Check if file exists
import os
if os.path.exists('filename.txt'):  # os.path.isfile, os.path.isdir
    f = open('filename.txt')

### Save RAM with generators
import sys

my_list = [i for i in range(10000)]
print(sys.getsizeof(my_list), "bytes")

my_gen  = (i for i in range(10000)]
print(sys.getsizeof(my_gen), "bytes")

### Get dictionary values without errors
my_dict = {"item": "Football", "price": 10.00}
count = mydict["count"]  <-- Generates error for missing key

count = mydict.get("count", 0)  <-- if count is missing, return 0

### Open file for reading
# instead of
f = open('test.txt', 'r')
file_contents = f.read()
f.close()

# do this
with open('test.txt', 'r') as f:
    file_contents = f.read()

