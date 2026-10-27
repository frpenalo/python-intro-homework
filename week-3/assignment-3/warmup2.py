# Here I ask for user age using input.
# Converts the age to an integer.
# Checks the age range and prints the correct category.

age = int(input("Enter your age: "))

if age >= 0 and age <= 12:
    category = "Child"
elif age >= 13 and age <= 17:
    category = "Teen"
elif age >= 18 and age <= 64:
    category = "Adult"
else:
    category = "Senior"

print(f"You are a {category}.")