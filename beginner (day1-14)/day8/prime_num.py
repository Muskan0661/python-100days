def prime_check(num):
    is_prime = True

    if num < 2:
        is_prime = False
    else:
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

    if is_prime:
        print("It is a prime number.")
    else:
        print("Not a prime number.")

n = int(input("Enter number to check: "))
prime_check(n)