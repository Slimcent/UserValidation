
# while first_name == '':
#     print("first number cannot be empty")
#     first_name = input(first_name)


def validate_name(name):
    while True:
        if name.strip() == '':
            print("first name cannot be empty")
            name = input(name)
        elif any(not c.isalpha() for c in name):
            print("first name cannot contain a number")
            name = input(name)
        else:
            name = name.capitalize()
            break
    return name


first_name = input("Enter first name")
first_name = str(input(first_name))
first_name = validate_name(first_name)


print(f"First name is {first_name}")
