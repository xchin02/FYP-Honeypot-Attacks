import os
from cryptography.fernet import Fernet

main_dir = "/home/pi"

with open(".encrypt.key", "rb") as key:
    decrypt_key = key.read()

for subdir, dirs, files in os.walk(main_dir):
    for file in files:
        if file == "ransomware.py" or file == "decrypt.py" or file == ".encrypt.key":
            continue
        else:
            try:
                with open(file, "rb") as usrFile:
                    contents = usrFile.read()
                encrypted_content = Fernet(decrypt_key).decrypt(contents)
                with open(file, "wb") as usrFile:
                    usrFile.write(encrypted_content) #Decrypts files except for root files
            except:
                pass
