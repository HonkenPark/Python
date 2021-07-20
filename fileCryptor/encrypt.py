import os
from cryptography.fernet import Fernet

class SimpleEnDecrypt:
    def __init__(self, key=os.path.isfile('./key')):
        if key is False:
            print("No key.. Generate !!")
            key = Fernet.generate_key()
            with open('./key', mode='wb') as keyValue:
                keyValue.write(key)
                keyValue.seek(0)
                keyValue.close()
        else:
            print("Key Exist.. Using !!")
            with open('./key', mode='rb') as keyValue:
                key = keyValue.read()
                keyValue.close()

        self.key = key
        self.f = Fernet(self.key)
        
    def encrypt(self, data, is_out_string=True):
        if isinstance(data, bytes):
            ou = self.f.encrypt(data) # Byte
        else:
            ou = self.f.encrypt(data.encode('utf-8')) # Encoding First
        if is_out_string is True:
            return ou.decode('utf-8') # In case of string, return after decodning
        else:
            return ou        

simpleEnDecrypt = SimpleEnDecrypt()
path_dir = os.getcwd() + '/test_folder'
file_list = os.listdir(path_dir)

for i in file_list:
    encrypt_text = simpleEnDecrypt.encrypt(i)
    os.rename(path_dir + '/' + i, path_dir + '/' + encrypt_text)


