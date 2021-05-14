user_input = input()

encrypted_string = ""
for word in user_input:
    for char in word:
        encrypted_string += chr(ord(char) + 1)

print(encrypted_string)
