def is_prime():
    user_input = input("Enter a number: ")
    num = int(user_input)

    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(f"{num} is NOT a prime number.")
                break
        else:
            print(f"{num} is a prime number!")
    else:
            print(f"{num} is NOT prime number!")
is_prime()

