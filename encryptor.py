import bcrypt

def hash_password(password:str) -> str:
    hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    return hashed.decode("utf-8")

def checked_password(password:str, hashed_password: str) -> str:
    return bcrypt.checkpw(password.encode("utf-8"), hashed_password.encode("utf-8"))