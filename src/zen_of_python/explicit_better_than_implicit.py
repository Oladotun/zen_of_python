"""
Explicit is better than implicit suggests that, the function inputs and output should be explicit.
Take the below example
"""


# bad code
def add(a, b):
    return a + b


print(add(1, 2))
print(add("orange", "banana"))
print(
    "The above code will take any function \n"
    "since it has not been explicitly defined ad return an input from it"
)

"""
The above code will take any function,
since it has not been explicitly defined ad return an input from it
"""


def add_explicit(a: int, b: int) -> int:
    return a + b


print(
    "The above is better for typehinting to ensure developer\n"
    "know what inputs are expected"
)
print(add_explicit(1, 2))
print(
    "we can try to add a string below and it would"
    " work due to the fact that strings can be added"
)
print(add_explicit("orange", "banana"))
