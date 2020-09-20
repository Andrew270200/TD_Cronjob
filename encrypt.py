from cryptography.fernet import Fernet


file = open('key.key','rb')
key = file.read()
file.close	

with open('text.txt','rb') as f:
	data = f.read()

fernet = Fernet(key)
encrypted = fernet.encrypt(data)

#write encypted file

with open('text.txt.encrypted','wb') as f:
	f.write(encrypted)


