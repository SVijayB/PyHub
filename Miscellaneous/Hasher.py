from passlib.hash import pbkdf2_sha256

hash = pbkdf2_sha256.hash("Secret!")
print(hash)
hash2 = pbkdf2_sha256.hash("Secret!")
print(hash2)

x = pbkdf2_sha256.verify("password", hash)
print(x)
y = pbkdf2_sha256.verify("Secret!", hash)
print(y)