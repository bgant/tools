def multiply_setup(amount: float):  # 1) function setup is used
    def multiply(number: float):
        return amount * number  # 3) function we curried is called
    return multiply  # 2) function we acually want to use is returned

double = multiply_setup(2)  # double is multiply func with amount set to 2
triple = multiply_setup(3)  # triple is multiply func with amount set to 3

print(f'double 4 is {double(4)}')
print(f'triple 10 is {triple(10)}')

