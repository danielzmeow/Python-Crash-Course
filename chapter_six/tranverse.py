usr_0 = {
    'username': 'user_0',
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}


for key, value in usr_0.items():
    print(f"Key: {key}")
    print(f"Value: {value}\n")

# Use .items() for key-value pairs, .keys() for keys, .values() for values

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
}

# set() is for removing duplicates

for language in set(favorite_languages.values()):
    print(language)