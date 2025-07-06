from kanren.facts import Relation, facts
from kanren.core import var, run, conde

if __name__=='__main__':
    parent = Relation()
    facts(parent, ("Slamet", "Amin"),
                  ("Slamet", "Anang"),
                  ("Amin", "Badu"),
                  ("Amin", "Budi"),
                  ("Anang", "Didi"),
                  ("Anang", "Dadi"))


    #=====================================
    # Versi Membuat Relasi Baru
    #=====================================

    grandfather = Relation()
    children = Relation()
    uncle = Relation()

    facts(grandfather, ("Slamet", "Badu"),
                       ("Slamet", "Budi"),
                       ("Slamet", "Didi"),
                       ("Slamet", "Dadi"))

    facts(children, ("Amin", "Slamet"),
                    ("Anang", "Slamet"),
                    ("Badu", "Amin"),
                    ("Budi", "Amin"),
                    ("Didi", "Anang"),
                    ("Dadi", "Anang"))

    facts(uncle, ("Amin", "Didi"),
                 ("Amin", "Dadi"),
                 ("Anang", "Badu"),
                 ("Anang", "Budi"))

    x = var()

    print("\nA. Dengan Membuat Relasi Baru")
    print("=============================")

    output_kakek1 = run(1, x, grandfather(x, "Badu"))
    print("Nama kakek Badu : ", output_kakek1[0])

    output_anak1 = run(0, x, children(x, "Amin"))
    print("\nNama anak Amin :", ', '.join(output_anak1))
    
    output_paman1 = run(0, x, uncle(x, "Didi"))
    print("\nNama paman Didi :", output_paman1[0])
    print("-----------------------------")


    #=======================================
    # Versi Tanpa Membuat Relasi Baru
    #=======================================

    def get_grandfather(grandfather, grandchild):
        father = var()
        return conde((parent(grandfather, father), parent(father, grandchild)))

    def get_children(child, parent_name):
        return parent(parent_name, child)

    def get_uncle(uncle, child_name):
        father = var()
        grandparent = var()
        return conde(
            (parent(father, child_name),
             parent(grandparent, father),
             parent(grandparent, uncle))
        )

    print("\nB. Tanpa Membuat Relasi Baru")
    print("=============================")

    output_kakek = run(1, x, get_grandfather(x, "Badu"))
    print("Nama kakek Badu : ", output_kakek[0])

    output_anak = run(0, x, get_children(x, "Amin"))
    print("\nNama anak Amin : ", ', '.join(output_anak))

    output_paman = run(0, x, get_uncle(x, "Didi"))

    ayah = run(1, x, parent(x, "Didi"))[0]
    paman = [nama for nama in output_paman if nama != ayah]

    print("\nNama paman Didi : ", ', '.join(paman))
    print("-----------------------------")