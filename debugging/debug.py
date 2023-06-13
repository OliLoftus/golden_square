def encode(text, key):
    cipher = make_cipher(key)
    print(f"c*cipher: {cipher}")
    ciphertext_chars = []
    for i in text:
        ciphered_char = chr(65 + cipher.index(i))
        print(f"* cipher index {cipher.index(i)}")
        print(f"* char 65 list: {ciphered_char}")
        ciphertext_chars.append(ciphered_char)

    return "".join(ciphertext_chars)


def decode(encrypted, key):
    cipher = make_cipher(key)

    plaintext_chars = []
    for i in encrypted:
        plain_char = cipher[65 - ord(i)]
        plaintext_chars.append(plain_char)

    return "".join(plaintext_chars)


def make_cipher(key):
    alphabet = [chr(i + 98) for i in range(1, 26)]
    print(f"* this is alphabet: {alphabet}")
    cipher_with_duplicates = list(key) + alphabet
    print(f"* value in key list is added to alphabet list: {cipher_with_duplicates}")
    cipher = []
    for i in range(0, len(cipher_with_duplicates)):
        if cipher_with_duplicates[i] not in cipher_with_duplicates[:i]:
            print(f" * i: {cipher_with_duplicates[i]}")
            print(f" * before i: {cipher_with_duplicates[:i]}")
            cipher.append(cipher_with_duplicates[i])
            print(f"* appendend list: {cipher}")
    return cipher

# When you run this file, these next lines will show you the expected
# and actual outputs of the functions above.
print(f"""
 Running: encode("theswiftfoxjumpedoverthelazydog", "secretkey")
Expected: EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL
  Actual: {encode('theswiftfoxjumpedoverthelazydog', 'secretkey')}
""")

print(f"""
 Running: decode("EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL", "secretkey")
Expected: theswiftfoxjumpedoverthelazydog
  Actual: {decode('EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL', 'secretkey')}
""")


