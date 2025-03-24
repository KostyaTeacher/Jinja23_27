import bcrypt

def hash_password(password: str):
    sssaaaallttt = bcrypt.gensalt()
    print("salt", sssaaaallttt)
    hashed = bcrypt.hashpw(password.encode(), sssaaaallttt)
    print("hashed", hashed)
    print("Hello everyone!!!!!")
    print("Hello everyodfne!!!!!")
    print("Hello everyone!fdf!!!!")



    return hashed

def check_password(password:str, hashed_password):
    return bcrypt.checkpw(password.encode(), hashed_password)
hashed_password = hash_password("Genius87")
print(check_password("Genius87", hashed_password))
