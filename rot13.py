
# Mērķis: 
# šifrēt tekstu ROT13 kodējumā


def rot13(texts):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    result = ""

    for char in text:
        if char.isalpha(): #если в тексте чар это буква
            is_upper = char.isupper()
            char_index = alphabet.index(char)
            if is_upper:
                new_index = (char_index + 13) % 26 
            else:
                new_index = (char_index + 13) % 26 + 26
            result += alphabet[new_index] if char.isalpha() else char
        else:
            result += char

    return result

print("Enter a text to ROT13 encode")
text = input()
encrypted_text = rot13(text)
print("ROT13 Encoded Text:", encrypted_text)

# Kādas kļūdas izdevies atrast?
# 
