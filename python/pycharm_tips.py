### Use function return types / PyCharm can now give "context options"
def func(numbers: list[int]) -> list[int]:
    numbers.reverse()  # Ctrl+Space to see context options based on type
    return numbers


print(func([1,2,3,4,5]))

### Hover over anything for a bit and documenation about it will pop-up

