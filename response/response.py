from validator_collection import validators, checkers, errors

try:
    user_email =  input("email: ")
    email_address = validators.email(user_email)
    print("valid")
except errors.EmptyValueError:
    print("invalid")
except errors.InvalidEmailError:
    print("invalid")