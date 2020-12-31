"""
You need to write a function that checks 
whether if the number passed into it is a prime number or not.
"""
def prime_checker(number):
    
    is_prime = True
    for nb in range(2, number):
        if number % nb == 0:
            is_prime = False

    if is_prime:
        print(f"{number} is a prime number.")

    else:
        print(f"{number} is Not a prime number") 


n = int(input("Check this number: "))
prime_checker(number=n)


"""
Prime numbers: 2 3 5 7 11 13 17 19 23 29
"""