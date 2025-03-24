import bcrypt

def hash_password(password: str):
    salt = bcrypt.gensalt()
    print("salt", salt)
    hashed = bcrypt.hashpw(password.encode(), salt)
    print("hashed", hashed)
    return hashed

def check_password(password:str, hashed_password):
    return bcrypt.checkpw(password.encode(), hashed_password)
hashed_password = hash_password("Genius87")
print(check_password("Genius87", hashed_password))

#$2b$12$KApn8FNG0LMDNAjFWXnTseTkVgfCkWvFuTvdz/e2DzbwYWkvNmrfu
#$2b$12$4uCZCVhPjcrQn.9ekhs.9eJV1d.YCpxW6/6iwYRKXLg/veZz2wb16