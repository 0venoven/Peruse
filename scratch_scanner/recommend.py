import re

def recommend(password):
    weakness_list = []
    weakness_list.append('Common Password: Your password is very commonly used, try creating a passphrase from a memory unique to you.')
    if len(password) < 12:
        weakness_list.append('Too short: Your password is too short, try making it longer.')
    if password.islower():
        weakness_list.append('All lower: Try a mix of uppercase and lowercase letters, numbers or symbols to make your password more random and difficult to guess.')
    elif password.isupper():
        weakness_list.append('All upper: Try a mix of uppercase and lowercase letters, numbers or symbols to make your password more random and difficult to guess.')
    if password.isalpha():
        weakness_list.append('Just letters: Your password only contains letters. Adding numbers or symbols will make your password more secure.')
    elif password.isnumeric():
        weakness_list.append('Just numbers: Your password only contains numbers. Adding letters or symbols will make your password more secure.')
    elif re.search(r'^[!@#$%^&*()_+\-=\[\]{};\'":\\|,.<>\/?]+$', password):
        weakness_list.append('Just symbols: Your password only contains symbols. Adding letters or numbers will make your password more secure.')
    if re.search(r'(.+?)\1+$', password):
        weakness_list.append('Repeated pattern: Repeated characters or patterns can make your password more predictable, try creating a passphrase from a memory unique to you.')
    return weakness_list

print(recommend('password'))
print(recommend('password123'))
print(recommend('password123!'))
print(recommend('password123!password123!'))
print(recommend('!@#$%^&*()_+'))
# maybe can direct them to CSA's password checker & how to create a secure password