def prime_check(number):
    is_prime = True
    for i in range(2, number):
        # print(i)
        result = number % i
        if result == 0:
            is_prime = False
            # print(f"The number is divided by {i}")
            break
    return is_prime


num = int(input("Check prime: "))
prime = prime_check(num)
if prime:
    print("It's a prime number.")
else:
    print("It's not a prime number.")
