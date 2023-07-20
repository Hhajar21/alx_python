def validate_password(password):
    if len(password) < 8:
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    if ' ' in password:
        return False
    return True 

validate_password = __import__('validate_password').validate_password

print(validate_password("Hello123"))  # True
print(validate_password("password"))  # False
print(validate_password("StrongPwd"))  # False
print(validate_password("AbCdEfG123"))  # True
print(validate_password(" Passw0rd "))  # False