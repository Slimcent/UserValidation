from email_validator import validate_email, EmailNotValidError, caching_resolver
import phonenumbers


def check_empty_input(user_input):
    while user_input.strip() == '':
        print(f"field {user_input} cannot be empty")
        user_input = input(user_input)


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


def phone_number_validation(user_phone_number):
    while True:
        if user_phone_number == '':
            print("Phone number cannot be empty")
            user_phone_number = input(user_phone_number)
        else:
            try:
                user_phone_number = phonenumbers.parse(user_phone_number, None)
                phonenumbers.is_valid_number(user_phone_number)
            except phonenumbers.NumberParseException as e:
                print(str(e))
                user_phone_number = input(user_phone_number)
                continue
            else:
                return user_phone_number
                break


def validate_address(user_address):
    while True:
        if user_address == '':
            print("Address cannot be empty")
            user_address = input(user_address)
        elif len(user_address) <= 4:
            print("Address length cannot be lower than 5 characters")
            user_address = input(user_address)
        elif len(user_address) >= 51:
            print("Address length cannot be more than 50 characters")
            user_address = input(user_address)
        else:
            return user_address
            break


def validate_age(user_age):
    while True:
        try:
            user_age = int(input(user_age))
        except ValueError:
            print("Age is invalid")
            continue
        else:
            if user_age <= 17:
                print("Age not eligible for registration")
                user_age = user_age
            else:
                return user_age
                break


age = validate_age("Enter age")
print(f"Your age is {age}")


address = input("Enter address")
address = validate_address(address)
print(f"Your address is {address}")

phone_number = input("Enter phone number")
phone_number = phone_number_validation(phone_number)
print(f"Your phone number is {phone_number.national_number}")

email = input("Enter email")
email = check_email(email)
print(f"Your email is {email}")

last_name = input("Enter last name")
last_name = validate_name(last_name)
print(f"First name is {last_name}")

first_name = input("enter first name")
first_name = validate_name(first_name)
print(f"First name is {first_name}")

print(f"Congrats {first_name}, your registration was successful\n "
      f"Full name : {last_name} {first_name}\n Email : {email}\n"
      f"Phone number : {phone_number.national_number}\n"
      f"Address is {address} and\n Age is : {age}")
