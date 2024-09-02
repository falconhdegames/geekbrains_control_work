from Counter import Counter
from JsonFile import JsonFile
from NotNullInput import *

def add_animal():
    name = NotNullInput('Enter name: ').capitalize()
    birth_date = DateInput('Enter birth date: ')
    commands = NotNullInput('Enter commands that the animal can do: ')
    animal_type = NotNullInput('Enter animal\'s type (example: cat): ')
    animal_kind = 'uknown'

    if animal_type.upper() in ('CAT', 'DOG', 'HAMSTER'): animal_kind = 'Home animal'
    elif animal_type.upper() in ('HORSE', 'CAMEL', 'DONKEY'): animal_kind = 'Pack animal'

    id = open('id', 'r', encoding='utf-8').read()
    JsonFile('animals.json').writeValue(id, {'name': name, 'birth_date': birth_date, 'commands': commands, 'animal_kind': animal_kind, 'animal_type': animal_type})
    open('id', 'w', encoding='utf-8').write(str(int(id)+1))

    Counter().add()
    print(f'Animal\'s ID is {id}')

def new_command():
    try:
        id = NotNullInput('Enter ID: ')
        command = NotNullInput('Enter command')
        file = JsonFile('animals.json')
        file.writeValueInDict(id, 'commands', f'{file.readValue("commands")}, {command}')
    except:
        print('Animal with this ID doesn\'t exists')

def view_commands():
    try:
        id = NotNullInput('Enter ID: ')
        print(JsonFile('animals.json').readValue(id)['commands'])
    except:
        print('Animal with this ID doesn\'t exists')

def view_animal(id = None):
    try:
        if not id: id = NotNullInput('Enter ID: ')
        animal = JsonFile('animals.json').readValue(id)
        print(F'ID: {id}; name: {animal["name"]}; birth date: {animal["birth_date"]}; commands: {animal["commands"]}; animal_kind: {animal["animal_kind"]}, animal type: {animal["animal_type"]}')
    except:
        print('Animal with this ID doesn\'t exists')

def remove_animal():
    try:
        id = NotNullInput('Enter ID: ')
        JsonFile('animals.json').removeValue(id)
        Counter().remove()
    except:
        print('Animal with this ID doesn\'t exists')

def view_all():
    try:
        for id in JsonFile('animals.json').readAll():
            view_animal(id)
    except:
        print('There aren\'t any animals.')