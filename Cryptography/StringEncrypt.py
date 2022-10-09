from cryptography.fernet import Fernet
import rsa

message = "Hello world!"
key = Fernet.generate_key()
fernet = Fernet(key)
encMessage = fernet.encrypt(message.encode())
 
print("Original string: ", message)
print("Encrypted string: ", encMessage)

decMessage = fernet.decrypt(encMessage).decode()
 
print("Decrypted string: ", decMessage)

# --- RSA MODULE ---

publicKey, privateKey = rsa.newkeys(512)

encMessage = rsa.encrypt(message.encode(), publicKey)
 
print("Original string: ", message)
print("Encrypted string: ", encMessage)
decMessage = rsa.decrypt(encMessage, privateKey).decode()
print("Decrypted string: ", decMessage)
