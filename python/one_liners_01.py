### 1 swap variables
a = 5
b = 10
a, b = b, a

### 2 list comprehension
# instead of 
squares = []
for i in range(10):
    if i % 2 == 0:
       squares.append(i*i)

# do this
squares = [i*i for i in range(10) if i % 2 == 0]

### 3 if else (ternary operator)
# instead of
if 3 > 2:
    var = 42
else:
    var = 99

# do this
var = 42 if 3 > 2 else 99

### 4 print without new lines
# instead of 
data = [0, 1, 2, 3, 4, 5]
for i in data:
    print(i, end=" ")

# do this
data = [0, 1, 2, 3 ,4, 5]
print(*data)

### 5 command-line one-liner
python -c import datetime;print(date)

### 6 reversing a list
a = [1, 2, 3, 4, 5, 6]
a = a[::-1]

### 7 multiple variable assignments
name, age, language = "Patrick", 31, "Python"

### 8 space separated numbers to integer list
user_input = "1 2 3 4 5 6"
my_list = list(map(int, user_input.split()))

### 9 Reading file into list
names = [line.strip() for line in open("names.txt", "r")]

### 10 http server
python -m http.server  <-- Creates web server for current directory

### 11 How to print emojis
print("🦕")
print("\U0001f995")
print("\N{SAUROPOD}")

### 12 print functions
s = "python"
print(s.startswith("py"))
print(s.endswith("on"))

### 13 find longest
my_list = ["I", "love", "Python"]
longest = max(my_list, key=len)  <-- This is the len() function without the ()

numbers = [-3, 4, 2]
sort(numbers)   <-- [-3, 2, 4]
sort(numbers, key=abs)   <-- [2, -3, 4]  <-- doesn't change the values


