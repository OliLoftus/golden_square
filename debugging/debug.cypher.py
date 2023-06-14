def encode(text, key):
    cipher = make_cipher(key)
    ciphertext_chars = []
    for i in text:
        ciphered_char = chr(65 + cipher.index(i))
        # iterates over text and for the char(i) in text find the index of that in the cipher of the key and
        # adds it to 65(a) then appends to ciphered_chars
        ciphertext_chars.append(ciphered_char)
    print(f"* ciphertext_chars: {ciphertext_chars}")

    return "".join(ciphertext_chars)


def decode(encrypted, key):
    cipher = make_cipher(key)
    print(f"* cipher: {cipher}")
    plaintext_chars = []
    for i in encrypted:
        print(f"* Index: {i}")
        plain_char = cipher[abs(65 - ord(i))]
        # discovered 65 - ord(i) was a negative value where it needed to be a positive so use the abs method to 
        # ensure its the absolute value ignoring the negative sign
        plaintext_chars.append(plain_char)

    return "".join(plaintext_chars)


def make_cipher(key):
    alphabet = [chr(i + 96) for i in range(1, 27)]
    # changed so it includes a(96 instead of 98) and includes z so 27 instead of 26
    cipher_with_duplicates = list(key) + alphabet
    cipher = []
    for i in range(0, len(cipher_with_duplicates)):
        if cipher_with_duplicates[i] not in cipher_with_duplicates[:i]:
            cipher.append(cipher_with_duplicates[i])
    return cipher



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


