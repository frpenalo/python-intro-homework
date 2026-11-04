names = ["Ana", "Luis", "Maria", "Marcus", "Carlos"]

search_name = input("Enter a name to search for: ")

found = False

for index in range(len(names)):
    if names[index] == search_name:
        print(f'Found "{search_name}" at index {index}.')
        found = True
        break

if found == False:
    print(f'"{search_name}" was not found in the list.')