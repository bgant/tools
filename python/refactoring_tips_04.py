### Avoid if-else hell
def first():
    print('Calling: first')
def second():
    print('Calling: second')
def third():
    print('Calling: third')
def default():
    print('Calling: default')

var: int = 2

# instead of this
if var == 0:
    first()
elif var == 1:
    second()
elif var == 2:
    third()
else:
    default()

# do this
funcs: dict = {0: first,  # dictionary of int and function object
               1: second,
               2: third}
final = funcs.get(var, default)  # final is one of three function objects
final()

