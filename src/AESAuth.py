from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes

from globals import DEFAULT_KEY_PATH


BYTES = 32


class AESAuth:
    def __init__(self, key):
        self.key = key
        self.nonce= None


    @staticmethod
    def key() -> bytes:
        return get_random_bytes(BYTES)


    def get_key(self) -> list:
        with open(DEFAULT_KEY_PATH, "rb") as file:
            for data in ([BYTES, BYTES, -1]):
                self.nonce, self.tag, self.key = file.read(data)
    

    def dump_key(self) -> None:
        with open(DEFAULT_KEY_PATH, "wb") as file:
            for data in [self.nonce, self.tag, self.key]:
                file.write(data)
        pass
    

    def encrypt(self, data: bytes) -> bytes:
        cipher = AES.new(self.key, AES.MODE_EAX)
        self.nonce = cipher.nonce
        ciphertext, self.tag = cipher.encrypt_and_digest(data)
        return ciphertext

    
    def decrypt(self, data: str) -> bytes:
        cipher = AES.new(self.key, AES.MODE_EAX, nonce=self.nonce)
        try:
            cipher.verify(self.tag)
            
        except ValueError:
            raise Exception("Invalid key.")