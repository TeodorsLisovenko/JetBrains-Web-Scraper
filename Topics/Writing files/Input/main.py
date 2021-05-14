# write the code here

user_input = input()

file = open('input.txt', 'w', encoding='utf-8')
file.write(user_input)
file.close()
