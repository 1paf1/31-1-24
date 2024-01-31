# import re
#
# def validate_home_phone(phone_number):
#     pattern = r'^\d{7,10}$'
#     return (re.match(pattern, phone_number))
#
# home_phone_number = input("Enter your home phone number: ")
#
# if not validate_home_phone(home_phone_number):
#     print("Invalid home phone number")
# else:
#     print("Valid home phone number")

####################


#
# import re
#
# def validate_phone_number(personal_phone_number):
#     pattern = r'^\+?\d{7,15}$'
#     return re.match(pattern, personal_phone_number) is not None
#
# phone_number = input("Enter your phone number: ")
#
# if not validate_phone_number(phone_number):
#     print("Invalid phone number")
# else:
#     print("Valid phone number")


# email (наявність @, домену: gmail.com наприклад, мінімальна довжина та максимальна на ваш вибір)
# import re
#
# def validate_email(email_address):
#     pattern = r'^[a-z0-9]{3,60}@gmail\.com$'
#
#     return re.match(pattern, email_address) is not None
#
# email = input("Enter your email: ")
# if not validate_email(email):
#     print("Invalid email")
# else:
#     print("Valid email")


#- ПІБ клієнта (3 слова, мінімальна довжина 2 символи, максимальна довжина 20)

# import re
#
# def validate_full_name(full_name):
#     pattern = r'^[a-zA-ZА-Яа-яёЁЇїІіЄєҐґ]{2,20}(?: [a-zA-ZА-Яа-яёЁЇїІіЄєҐґ]{2,20}){2}$'
#     return re.match(pattern, full_name) is not None
#
# fullname = input('Enter your full name: ')
# if validate_full_name(fullname):
#     print("Full name is valid")
# else:
#     print("Full name is not valid")


 ######3