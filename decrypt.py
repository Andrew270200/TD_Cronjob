from cryptography.fernet import Fernet


file = open('key.key','rb')
key = file.read()
file.close	

with open('text.txt.encrypted','rb') as f:
	data = f.read()

fernet = Fernet(key)
decrypted = fernet.decrypt(data)

#write encypted file

with open('text.txt.decrypted','wb') as f:
	f.write(decrypted)


