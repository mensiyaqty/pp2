def is_prime(n: int):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers: list[int]):
    return [num for num in numbers if is_prime(num)]

nums = [3, 4, 7, 8, 11, 15, 17, 20]
print(filter_prime(nums))
