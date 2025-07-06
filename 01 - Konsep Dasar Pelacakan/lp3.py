from kanren import Relation, facts, run, conde, var, eq

def get_parent(x, child, father, mother):
    return conde(
        (father(x, child),),
        (mother(x, child),)
    )

if __name__=='__main__':
    father = Relation()
    mother = Relation()

    facts(father, ('Vito', 'Michael'),
                ('Vito', 'Sonny'),
                ('Vito', 'Fredo'),
                ('Michael', 'Anthony'),
                ('Michael', 'Mary'),
                ('Sonny', 'Vicent'),
                ('Sonny', 'Francesca'),
                ('Sonny', 'Kathryn'),
                ('Sonny', 'Frank'),
                ('Sonny', 'Santino'))

    facts(mother, ('Carmela', 'Michael'),
                ('Carmela', 'Sonny'),
                ('Carmela', 'Fredo'),
                ('Kay', 'Mary'),
                ('Kay', 'Anthony'),
                ('Sandra', 'Francesca'),
                ('Sandra', 'Kathryn'),
                ('Sandra', 'Frank'),
                ('Sandra', 'Santino'))

    x = var()
    parents = run(0, x, get_parent(x, 'Michael', father, mother))

    print('\nNama orang tua Michael:')
    for item in parents:
        print(item)