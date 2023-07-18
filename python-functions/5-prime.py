def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

is_prime = __import__('is_prime').is_prime

print(is_prime(7))
print(is_prime(12))
print(is_prime(29))
print(is_prime(0))
print(is_prime(1))