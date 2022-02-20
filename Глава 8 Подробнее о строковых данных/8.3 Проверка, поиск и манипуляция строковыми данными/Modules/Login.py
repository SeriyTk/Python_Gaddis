def valid_password(par):
    correct_length = False
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    if len(par) >= 7:
        correct_length = True
    for ch in par:
        if ch.isupper():
            has_uppercase = True
        if ch.islower():
            has_lowercase = True
        if ch.isdigit():
            has_digit = True
    if correct_length and has_uppercase and has_lowercase and has_digit:
        is_valid = True
    else:
        is_valid = False

    return is_valid
