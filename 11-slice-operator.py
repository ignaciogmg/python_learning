def caesarCipherEncryptor (string, key):
    new_string = ""
    for letter in string:
        if ord(letter)+key > ord('z'):
            new_string += chr(ord('a') + key - (ord('z')-ord(letter))-1)
        else:
            new_string += chr(ord(letter) + key )
    return print(new_string)


caesarCipherEncryptor('xyz', 2)
