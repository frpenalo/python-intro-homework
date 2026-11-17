def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32


def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9


fahrenheit1 = celsius_to_fahrenheit(0)
fahrenheit2 = celsius_to_fahrenheit(100)
celsius1 = fahrenheit_to_celsius(72)

print(f"0°C = {round(fahrenheit1, 1)}°F")
print(f"100°C = {round(fahrenheit2, 1)}°F")
print(f"72°F = {round(celsius1, 1)}°C")