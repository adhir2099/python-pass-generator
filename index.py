import secrets
import string

def new_pass(randomized):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""
    for _ in range(randomized):
        password += secrets.choice(characters)
    return password

new_generated_password = new_pass(16)
print(new_generated_password)