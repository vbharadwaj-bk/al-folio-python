import hashlib
import os
import random

# Translated via ChatGPT from  
# https://distresssignal.org/busting-css-cache-with-jekyll-md5-hash

class CacheDigester:
    def __init__(self, file_name):
        self.file_name = file_name
        self.BUF_SIZE = 65536


    def digest(self):
        md5 = hashlib.md5()
        with open(f'content/{self.file_name}', 'rb') as f:
            while True:
                data = f.read(self.BUF_SIZE)
                if not data:
                    break
                md5.update(data) 
        
        return f"{self.file_name}?{md5.hexdigest()}"

def bust_file_cache(file_name):
    if '://' not in file_name:
        digester = CacheDigester(file_name)
        return digester.digest()
    else:
        return file_name