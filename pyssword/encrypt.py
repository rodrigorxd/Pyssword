import hashlib

#encrypt input password - SHA1
def encrypt_password(pass_check):
    pass_encrypt = hashlib.sha1()
    pass_encrypt.update(pass_check.encode())
    return pass_encrypt.hexdigest()

#store first 5 encrypted digits
def first_five(encrypted):
    five_digits = ""
    for i in range(0, 5):
        five_digits += encrypted[i]
    return five_digits

#store other encrypted digits
def second_part(encrypted):
    other_digits = ""
    for i in range(5, len(encrypted)):
        other_digits += encrypted[i]
    return other_digits
