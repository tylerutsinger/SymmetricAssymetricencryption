from cryptography.fernet import Fernet
import shutil, os #used to copy file for part 2 of project


key = Fernet.generate_key() 

with open('thekey.txt','wb') as thekey:
    thekey.write(key)


print("this is the generated key",key)


t = Fernet(key)

with open ('message.txt', 'rb') as original:
    original = original.read() 

encrypted = t.encrypt(original)


with open('encryptedmessage.txt', 'wb') as encrypted_file: 
    encrypted_file.write(encrypted)




print("the unencrypted file in folder is",original)
print("the encrypted message is now", encrypted)
print("Encrypted file and key have been saved to folder") 
print("")
print("")

# provide copy to part 2 of the project
shutil.copy("C:\\Users\\tyler\\Desktop\\project\\project part 1\\thekey.txt","C:\\Users\\tyler\\Desktop\\project\\projectparttwo\\rsa_sym_key_plain.txt")
response = input("do you want to decrypt the file? yes/no")
if response == "yes": 
    print('okay we will decrypt the file')

    t= Fernet(key)
    with open('encryptedmessage.txt','rb') as encrypted_file:
        encrypted = encrypted_file.read()

    decrypted=t.decrypt(encrypted)

    with open ('decrypted.txt', 'wb') as decrypted_file:
        decrypted_file.write(decrypted)

    print("file has been decrypted and saved to folder")
    print("The decrypted string in the txt file was, ", decrypted)



