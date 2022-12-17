from email_validator import validate_email, EmailNotValidError, caching_resolver


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


def check_email(user_email):
    while True:
        # resolver = caching_resolver(timeout=10)
        if user_email.strip() == '':
            print("email cannot be empty")
            user_email = input(user_email)
        else:
            try:
                user_email = validate_email(user_email).email
            except EmailNotValidError as e:
                print(str(e))
                user_email = input(user_email)
                continue
            else:
                return user_email
                break


email = input("Enter email")
email = input(email)
email = check_email(email)
print(f"Your email is {email}")

last_name = input("Enter last name")
last_name = str(input(last_name))
last_name = validate_name(last_name)
print(f"First name is {last_name}")

first_name = input("enter first name")
first_name = str(input(first_name))
first_name = validate_name(first_name)
print(f"First name is {first_name}")
