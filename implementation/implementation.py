def to_num(c):
    return ord(c) - 65  

def to_char(n):
    return chr(n + 65)  

def encrypt(msg, key):
    msg = msg.upper().replace(" ", "")
    key = key.upper().replace(" ", "")
    result = ""

    for i in range(len(msg)):
        m = to_num(msg[i])
        k = to_num(key[i])
        e = (m + k) % 26
        result += to_char(e)

    return result

def decrypt(cipher, key):
    cipher = cipher.upper().replace(" ", "")
    key = key.upper().replace(" ", "")
    result = ""

    for i in range(len(cipher)):
        c = to_num(cipher[i])
        k = to_num(key[i])
        d = (c - k + 26) % 26
        result += to_char(d)

    return result

# Trial
plain = "HELLO"
key = "XMCKL"
cipher = encrypt(plain, key)
print("Encrypted:", cipher)

original = decrypt(cipher, key)
print("Decrypted:", original)