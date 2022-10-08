import numpy as np

pt = input("Enter the plain text ")
key = input("Enter the key ")
pt = pt.lower()
key = key.lower()
key = np.array([(ord(b) - 97) for b in key])  # converting alphabets to ascii values

if len(key) == 4:
    size = 2
    keym = key.reshape(2, 2)
if len(key) == 9:
    size = 3
    keym = key.reshape(3, 3)

# loop to append extra characters
pt = list(pt)
while len(pt) % size != 0:
    pt.append("x")

pt = np.array([(ord(a) - 97) for a in pt])

# splits the array into equal parts
ptm = np.array_split(pt, len(pt) / size)
print("Encrypted text is")  # Encryption
enc = []
for a in ptm:
    a = a.reshape(size, 1)
    encr = np.dot(keym, a) % 26
    for a in np.nditer(encr):
        enc.append(a)
        print(chr(a + 97), end=" ")
print()
print("decrypted text is")  # Decryption
adj = np.linalg.inv(keym)
det = round(np.linalg.det(keym))
adj = adj * det  # inverse*det = adjacent matrix

# np.where() to add all the negative numbers
np.where(adj < 0, adj + 26, adj)

# loop to find the inverse which is used to multiply with matrix
x = 1
while (det * x) % 26 != 1:
    x += 1


final = (x * adj) % 26  # final is the inverse matrix of the key
enc = np.array(enc)  # enc is the ciphertext
encm = np.array_split(enc, len(enc) / size)  # spliting it into equal sizes
for a in encm:
    a = a.reshape(size, 1)
    decr = np.round_(np.dot(final, a))
    decr = decr.astype(int)
    decr = decr % 26
    for a in np.nditer(decr):
        print(chr(a + 97), end=" ")
