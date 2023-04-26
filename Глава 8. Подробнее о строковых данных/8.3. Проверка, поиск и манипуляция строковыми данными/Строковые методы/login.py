def get_login_name(first, last, idnum):
    set1 = first[0 : 3]
    set2 = last[0 : 3]
    set3 = idnum[-3 : ]
    return set1 + set2 + set3
def valid_pass(password):
    correct_length = False
    has_upp = False
    has_low = False
    has_dig = False
    if len(password) >= 7:
        correct_length = True
        for ch in password:
            if ch.isupper(): has_upp = True
            if ch.islower(): has_low = True
            if ch.isdigit(): has_dig = True
        if correct_length and has_upp and has_low and has_dig: is_valid = True
        else: is_valid = False
        return is_valid
