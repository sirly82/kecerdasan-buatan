from kanren.facts import Relation, facts
from kanren.core import var, run, conde

def get_sibling(x, y):
    temp = var()
    return conde((parent(temp, x), parent(temp, y)))

def get_uncle(x, y):
    father = var()
    grandfather = var()

    return conde((parent(grandfather, father),
                parent(father, y),
                parent(grandfather, x)))

if __name__=='__main__':
    parent = Relation()
    facts(parent, ('Homer', 'Bart'),
                ('Homer', 'Lisa'),
                ('Homer', 'Ana'),
                ('Abe', 'Homer'),
                ('Abe', 'Jude'),
                ('Jude', 'Anna'))

    x = var()
    father = run(1, x, parent(x, 'Bart'))
    print('\nNama ayah Bart: ', father[0])

    # sibling = Relation()
    # facts(sibling, ('Bart', 'Lisa'),
    #                 ('Lisa', 'Bart'))
    # brother = run(0, x, sibling(x, 'Lisa'))
    # print('\nNama saudara laki-laki Lisa: ', brother[0])
    # sister = run(0, x, sibling(x, 'Bart'))
    # print('\nNama saudara perempuan Bart: ', sister[0])

    siblings = run(0, x, get_sibling(x, 'Bart'))
    siblings = [x for x in siblings if x != 'Bart']
    print('\nNama Saudara Bart: ')
    for item in siblings:
        print(item)
    
    uncle = run(0, x, get_uncle(x, 'Bart'))
    uncle = [x for x in uncle if x != father[0]]
    print('\nNama Uncle Bart: ')
    for item in uncle:
        print(item)