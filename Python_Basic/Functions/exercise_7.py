def find_prime(number):
    if number < 2:
        return False
    for divisor in range(2, number):
        if number % divisor == 0:
            return False
    return True

def get_prime_numbers(numbers):
    prime_numbers = []
    for number in numbers:
        if find_prime(number):
            prime_numbers.append(number)
    return prime_numbers

numbers_to_find = [1,4,6,7,13,9,67]
result = get_prime_numbers(numbers_to_find)
print()
print(f"The Original list number is: {numbers_to_find}")
print(f"There's only the prime numbers in the list: {result}")
print()
    
