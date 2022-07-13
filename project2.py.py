import rsa
(publickey, privkey)= rsa.newkeys(512) #generated key pair
#RSA module only handles bits so using strings would become difficult?


with open ("publickey.pem","wb") as publickey_file:
    publickey_file.write(publickey.save_pkcs1())
print("public key is ", publickey)

with open ("privkey.pem","wb") as privkey_file:
    privkey_file.write(privkey.save_pkcs1())
print(" ")
print("private key is ", privkey)


print(" ")

print("The copy of your key from part 1 is saved and ready to encrypt")
print(" ")


print(" ")
with open('rsa_sym_key_plain.txt', 'rb') as original:
    original= original.read() 
print("here is the the key that needs encrypted", original)

print("")
print("we will now encrypt the  key with the public key using RSA")

encrypted= rsa.encrypt(original,publickey)

print("")
print("here is the encrypted key which used the public key", encrypted)
print("")
print("saving encrypted key to the folder")

with open('rsa_sym_key_cipher.txt ', 'wb') as encrypted_file: 
    encrypted_file.write(encrypted)





#decrypt
with open('rsa_sym_key_cipher.txt', 'rb') as enc:
    enc= enc.read() 
print("here is the the encrypted key that needs decrypted", enc)

decrypt= rsa.decrypt(enc,privkey)

print("Done! here is the decrypted key using the private key", decrypt)


