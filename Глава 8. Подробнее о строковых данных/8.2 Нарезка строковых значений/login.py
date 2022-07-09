def get_login_name(first, last, id):
    login_name = first[0:3] + last[0:3] + id[-3:]
    return login_name
