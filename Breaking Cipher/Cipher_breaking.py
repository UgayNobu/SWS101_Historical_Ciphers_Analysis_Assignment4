def break_cipher(cipher, known):
    cipher = cipher.upper()
    known = known.upper()
    key = ""

    for i in range(len(known)):
        c = ord(cipher[i]) - 65
        p = ord(known[i]) - 65
        k = (c - p + 26) % 26
        key += chr(k + 65)

    return key

# Trial
cipher = "MXXTOO"
known = "ATTACK"
key_found = break_cipher(cipher, known)
print("Key Guess:", key_found)