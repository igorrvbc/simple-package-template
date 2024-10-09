import random
import string

def generate_password(length=12):
    if length < 4:
        raise ValueError("A senha deve ter pelo menos 4 caracteres.")

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))

    return password
