number = int(input("Enter a number: "))

# Check the sign
if number > 0:
    sign = "positive"
elif number < 0:
    sign = "negative"
else:
    sign = "zero"

# Check if it is even or odd
if number % 2 == 0:
    parity = "even"
else:
    parity = "odd"

print(f"{number} is {sign}.")
print(f"{number} is {parity}.")