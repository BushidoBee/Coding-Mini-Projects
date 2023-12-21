#!/usr/bin/env python3

import os
#from Cryptography.fernet import Fernet #symmetric encryption method, cannot use w/o encryptopn key; 128-bit AES

#encrypt_key = Fernet.generate.key()
all_files = []

for select_file in os.listdir():
    if select_file == "Virus.py":
        continue
    if os.path.isfile(select_file):
        all_files.append(select_file)
    
print(all_files)
#print(encrypt_key)