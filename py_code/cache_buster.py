import hashlib
import os
import random

# Translated via ChatGPT from  
# https://distresssignal.org/busting-css-cache-with-jekyll-md5-hash

class CacheDigester:
    def __init__(self, file_name, directory=None):
        self.file_name = file_name
        self.directory = directory

    def digest(self):
        #return f"{self.file_name}?{self._calculate_md5_hash()}"
        random_int = random.randint(0, 10)
        return f"{self.file_name}?{random_int}"

    def _directory_files_content(self):
        files_content = []
        for root, _, files in os.walk(self.directory):
            for file in files:
                file_path = os.path.join(root, file)
                if not os.path.isdir(file_path):
                    with open(file_path, 'r') as f:
                        files_content.append(f.read())

        print(''.join(files_content))
        return ''.join(files_content)

    def _file_content(self):
        with open(self.file_name, 'r') as f:
            return f.read()

    def _calculate_md5_hash(self):
        if self._is_directory():
            return hashlib.md5(self._directory_files_content().encode()).hexdigest()
        return hashlib.md5(self._file_content().encode()).hexdigest()

    def _is_directory(self):
        return self.directory is None

def bust_file_cache(file_name):
    digester = CacheDigester(file_name)
    return digester.digest()

def bust_css_cache(file_name):
    digester = CacheDigester(file_name, directory='assets/_sass')
    return digester.digest()
