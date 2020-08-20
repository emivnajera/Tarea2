import json

with open('alumnos.json') as data:
    info = json.load(data)


def correr():
    for i in info:
        print(i)
        print()


print(correr())
