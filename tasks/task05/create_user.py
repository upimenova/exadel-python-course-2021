def create_user(name, surname, age=42, **kwargs):
    user = {}
    extra = {}
    user['name'] = name
    user['surname'] = surname
    user['age'] = age
    user['extra'] = kwargs
    return user


assert create_user('John', 'Doe') == {'name': 'John', 'surname': 'Doe', 'age': 42, 'extra': {}}
assert create_user('Bill', 'Gates', age=65) == {'name': 'Bill', 'surname': 'Gates', 'age': 65, 'extra': {}}
assert create_user('Marie', 'Curie', age=66, occupation='physicist', won_nobel=True) ==\
       {'name': 'Marie', 'surname': 'Curie', 'age': 66, 'extra': {'occupation': 'physicist', 'won_nobel': True}}
