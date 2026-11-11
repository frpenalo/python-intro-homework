# Example 1: variable inside a function

def create_message():
    message = "Hello from inside the function"
    print(message)


create_message()

# print(message)
# NameError: name 'message' is not defined


# Example 2: using return

def create_message2():
    message = "Hello from the function"
    return message


result = create_message2()

print(result)