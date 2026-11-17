numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]


def find_min(numbers):
    smallest = numbers[0]

    for number in numbers:
        if number < smallest:
            smallest = number

    return smallest


def find_max(numbers):
    largest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number

    return largest


def search(numbers, target):
    for index in range(len(numbers)):
        if numbers[index] == target:
            return index

    return -1


def bubble_sort(numbers):
    new_list = numbers.copy()

    swapped = True

    while swapped:
        swapped = False

        for i in range(len(new_list) - 1):
            if new_list[i] > new_list[i + 1]:

                temp = new_list[i]
                new_list[i] = new_list[i + 1]
                new_list[i + 1] = temp

                swapped = True

    return new_list


def show_menu():
    print("\n=== Number Cruncher ===")
    print("1. Find minimum")
    print("2. Find maximum")
    print("3. Search for a number")
    print("4. Sort the list")
    print("5. Quit")

    choice = input("Choose an option (1-5): ")

    return choice


def main():
    while True:

        choice = show_menu()

        if choice == "1":
            result = find_min(numbers)
            print(f"Minimum: {result}")

        elif choice == "2":
            result = find_max(numbers)
            print(f"Maximum: {result}")

        elif choice == "3":
            target = int(input("Enter a number to search for: "))

            index = search(numbers, target)

            if index == -1:
                print("Not found")
            else:
                print(f"Found at index {index}")

        elif choice == "4":
            sorted_numbers = bubble_sort(numbers)
            print("Sorted list:", sorted_numbers)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Please choose a number from 1 to 5.")


main()