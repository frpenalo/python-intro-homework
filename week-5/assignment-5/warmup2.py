while True:
    number = input("Enter a positive integer: ")

    if number.isdigit() and int(number) > 0:
        print(f"Got it: {number}")
        break
    else:
        print("That's not a positive integer. Try again.")