def create_user(name, surname, age = 42, **extra):
    user = {}
    extra = {}
    user['name'] = name
    user['surname'] = surname
    user['age'] = age
    if extra is True:
        for key, value in extra.items():
            extra[key] = value
    user['extra'] = extra
    print(user)


create_user('Marie', 'Curie', age=66, occupation='physicist', won_nobel=True)
