from kanren.facts import Relation, facts, fact
from kanren.core import var, run

jenis = Relation()
rasa = Relation()
original = Relation()
facts(jenis, ("makaroni balado", "makanan"),
            ("es boba", "minuman"),
            ("cimol pedas", "makanan"),
            ("es jeruk", "minuman"),
            ("es teh", "minuman"),
            ("makaroni barbeque", "makanan"))

facts(rasa, ("makaroni balado", "balado"),
            ("cimol pedes", "pedas"),
            ("es boba", "manis"),
            ("es jeruk", "asam"),
            ("es teh", "tawar"),
            ("makaroni barbeque", "barbeque"))
fact(original, "balado")
fact(original, "asin")

x = var()
y = var()

minuman = run(0, x, jenis(x, "minuman"))
makanan = run(0, y, jenis(y, "makanan"))

minumanmanis = run(0, x, jenis(x, "minuman"), rasa(x, "manis"))
rasaori = run(0, x, original(y), rasa(x,y))

print("Menu berjenin makanan : ", makanan)
print("Menu berjenis minuman : ", minuman)
print("Minuman yang memiliki rasa manis : ", minumanmanis)
print("Makanan yang memiliki rasa original : ", rasaori)