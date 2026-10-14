age = input("How old are you? ")

next_year = age + 1

print(f"Next year you will be {next_year}.")

# ERROR MESSAGE:
# TypeError: can only concatenate str (not "int") to str

# CAUSE:
# input() returns a string, and I tried to add an integer to it.

# Fix:
# I converted the input to an integer using int().