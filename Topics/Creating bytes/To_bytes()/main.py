user_input = int(input())

int_to_bytes = (user_input).to_bytes(2, 'big')

the_sum = 0

for byte in int_to_bytes:
    the_sum += byte

print(the_sum)
