from kanren import Relation, facts, var, run

father = Relation()
facts(father, ('Slamet', 'Amin'),
                ('Slamet', 'Anang'),
                ('Amin', 'Badu'),
                ('Amin', 'Budi'),
                ('Anang', 'Didi'),
                ('Anang', 'Dadi'))

x = var()
child = 'Amin'
output = run(0, x, father(x, child))
print('\nNama ayah ', child, ': ')
for item in output:
    print(item)