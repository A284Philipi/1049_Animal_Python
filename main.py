coluna = str(input())
familia = str(input())
alimentacao = str(input())
animal = str()

if (coluna == 'vertebrado'):
    if (familia == 'ave'):
        if (alimentacao == 'carnivoro'):
            animal = 'aguia'
        else:
            animal = 'pomba'
    else:
        if (alimentacao == 'onivoro'):
            animal = 'homem'
        else:
            animal = 'vaca'
else:
    if (familia == 'inseto'):
        if (alimentacao == 'hematofago'):
            animal = 'pulga'
        else:
            animal = 'lagarta'
    else:
        if (alimentacao == 'hematofago'):
            animal = 'sanguessuga'
        else:
            animal = 'minhoca'

print(animal)