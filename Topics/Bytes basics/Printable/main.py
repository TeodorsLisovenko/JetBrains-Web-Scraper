user_input = int(input())

if 32 <= user_input <= 126:
    print(chr(user_input))
else:
    print(False)
