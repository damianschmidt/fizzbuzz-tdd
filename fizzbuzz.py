def check(number: int) -> str:
    result = ''

    if is_divisible_by_value(number, 3):
        result += "Fizz"

    if is_divisible_by_value(number, 5):
        result += "Buzz"

    if result:
        return result
    else:
        return str(number)


def is_divisible_by_value(number: int, value: int) -> bool:
    return number % value == 0


# How it works
for num in range(1, 101):
    print(check(num))
