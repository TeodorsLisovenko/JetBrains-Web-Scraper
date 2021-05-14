key_to_delete = int(input())

get_deleted_key = squares.pop(key_to_delete, 'There is no such key')

print(get_deleted_key)

print(squares)
