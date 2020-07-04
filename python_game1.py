import time
print(
    """
    +================================+
    | Welcome to my game, muggle!    |
    | Enter an integer number        |
    | and guess what number I've     |
    | picked for you.                |
    | So, what is the secret number? |
    +================================+
    """)

secret_no = 777
number = int(input("enter number : "))
while number != 777:
    if number == secret_no:

        pass

    else:
        print("Ha ha! You're stuck in my loop!")
        time.sleep(0)

    number = int(input("enter number : "))

print("Well done, muggle! You are free now.")
