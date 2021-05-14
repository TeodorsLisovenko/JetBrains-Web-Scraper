# read animals.txt
animals = open('animals.txt', 'r')
x = animals.read()
animals.close()

# mock_animals = 'rabbit\ncat\nturtle'
# and write animals_new.txt

animals_modified = str(x).replace("\n", " ")

file = open('animals_new.txt', 'w',  encoding='utf-8')
file.write(animals_modified)
file.close()
