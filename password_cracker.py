import hashlib


def crack_sha1_hash(hash_to_check, use_salts=False):
    with open("top-10000-passwords.txt", "r") as f:
        passwords = [line.strip() for line in f]

    if not use_salts:
        for password in passwords:
            if hashlib.sha1(password.encode()).hexdigest() == hash_to_check:
                return password
        return "PASSWORD NOT IN DATABASE"

    with open("known-salts.txt", "r") as f:
        salts = [line.strip() for line in f]

    for password in passwords:
        for salt in salts:
            if hashlib.sha1((salt + password).encode()).hexdigest() == hash_to_check:
                return password
            if hashlib.sha1((password + salt).encode()).hexdigest() == hash_to_check:
                return password

    return "PASSWORD NOT IN DATABASE"