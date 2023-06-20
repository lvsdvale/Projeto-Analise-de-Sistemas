from passlib.context import CryptContext

CRYPTO = CryptContext(schemes=['bcrypt'], deprecated='auto')

def verify_password(password: str, hash: str) -> bool:
    return CRYPTO.verify(password, hash=hash)

def create_hash(password: str) -> str:
    return CRYPTO.hash(password)