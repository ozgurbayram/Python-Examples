import bcrypt


passwrd = 'hello3Bworld'.encode()

print(bcrypt.hashpw(passwrd, bcrypt.gensalt(12)))