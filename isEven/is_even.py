# As an alias to remain backward compatible
def isEven(number):
    return is_even(number)

def is_even(number: int) -> bool:
    return number & 1 ^ 1
