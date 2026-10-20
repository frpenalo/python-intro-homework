f = float(input("Enter a temperature in Fahrenheit: "))

c = (f - 32) * 5 / 9
c = round(c, 1)

print(f"{f}°F is {c}°C.")