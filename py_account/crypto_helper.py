from cryptography.fernet import Fernet
from cryptography.hazmat import backends
from cryptography.hazmat import primitives
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, kdf
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os

crypto_manager = None

class CryptoHandler:
    def __init__(self, **kwargs):
        self.key = kwargs.get("key")
        self.fernet = None
        # very first object
        if self.key == None and kwargs.get("generate_new"): # generate_new = True
            self.key = Fernet.generate_key() #get new key.
            file_location = kwargs.get("key_location") # default = key.key

            if file_location == None:
                self.save_key() # to default location.

            else:
                self.save_key(file_location)

        # import object
        elif self.key == None and kwargs.get("read_key"):
            file_location = kwargs.get("key_location")

            if file_location == None:
                self.get_key()

            else:
                self.get_key(file_location)
        
        # init fernet obj
        self.fernet = Fernet(self.key)
    
    # for future use
    def save_key(self, filename = "key.key"):
        if self.key == None:
            raise Exception("Key is null")

        file = open(filename, 'wb')
        file.write(self.key)
        file.close()

    def get_key(self, filename = "key.key"):
        file = open(filename, 'rb')
        self.key = file.read()
        file.close()
        return self.key

    def encrypt(self, message):
        if type(message) == type(b'a'): return self.fernet.encrypt(message)
        if type(message) == type(""):return self.fernet.encrypt(message.encode())
        return None

    def decrypt(self, message):
        if message == None:return None
        if type(message) == type(b'a'): return self.fernet.decrypt(message)
        if type(message) == type(""): return self.fernet.decrypt(message.decode())
        return None
        

    def save_data(self, data, file_location):
        operation = ""
        if type(data) == type(b'a'): operation = 'wb'
        elif type(data) == type(""): operation = 'w'
        
        with open(file_location, operation) as file:
            file.write(data)

    # just reads from file. Does not encrypt or decrypt.
    # Get the data with this and do the operation with other functions.
    def read_data(self, file_location):
        file = open(file_location, 'rb')
        data = file.read()
        file.close()
        return data


def first(MAIN_KEY):
    global crypto_manager
    crypto_manager = CryptoHandler(generate_new = True, file_location = MAIN_KEY)

def load(MAIN_KEY):
    global crypto_manager
    if not os.path.exists(MAIN_KEY):
        print("Couldn't find the main file: " + MAIN_KEY )
        print("Saving new one.")
        first(MAIN_KEY)
    else:
        crypto_manager = CryptoHandler(generate_new = False, read_key = True, key_location = MAIN_KEY)





