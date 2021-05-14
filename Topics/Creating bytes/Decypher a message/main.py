encoded_message = input()

key = int(input())

key_to_bytes = key.to_bytes(2, byteorder='little')

real_key = 0

for byte in key_to_bytes:
    real_key += byte

decoded_message = ""

for char in encoded_message:
    decoded_message += chr(ord(char) + real_key)

print(decoded_message)
