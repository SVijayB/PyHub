#Caesar cipher: Encryption and Decryption
def encrypt(text,s):
    result = ""
    
    for i in range(len(text)):
        char = text[i]
 
        if char.isupper():
            result += chr((ord(char) + s-65) % 26 + 65)
 
        elif char.islower():
            result += chr((ord(char) + s - 97) % 26 + 97)
        
        else:
            result += char
    return result

def decrypt(text,s):
    result = ""
    
    for i in range(len(text)):
        char = text[i]
 
        if char.isupper():
            result += chr((ord(char) - s-65 + 26) % 26 + 65)
 
        elif char.islower():
            result += chr((ord(char) - s - 97 + 26) % 26 + 97)
        
        else:
            result += char
    return result
 
if __name__ == "__main__":

    text = input("\nEnter the plaintext: ")
    key = int(input("\nEnter the key: "))
    ciphertest = encrypt(text,key)
    print ("\nCipher: " + ciphertest)
    print ("\nDecrypted: " + decrypt(ciphertest,key))