### Example 1
primary = 'Alice'
backup = ''

if user := (primary or backup):
    print(f'{user} authenticated')
else:
    print('No users found')

### Example 2
# without walrus
n = 30
if n > 10:
    print(f"{n} is greater than 10")

# with walrus
if (n := 30) > 10:
    print(f"{n} is greater than 10")

