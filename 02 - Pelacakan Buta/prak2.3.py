from kanren.facts import Relation, facts, fact
from kanren.core import var, run

ukuran = Relation()
warna = Relation()
gelap = Relation()

facts(ukuran, ("beruang", "besar"),
                ("gajah", "besar"),
                ("kucing", "kecil"))

facts(warna, ("beruang", "cokelat"),
                ("kucing", "hitam"),
                ("gajah", "kelabu"))

fact(gelap, "hitam")
fact(gelap, "cokelat")

z = var()
kecil = run(0, z, ukuran(z, "kecil"))
print("hewan berukuran kecil: ", kecil)

x_hewan = var()
y_warna = var()

result = run(0, x_hewan, warna(x_hewan, y_warna), gelap(y_warna))
print('Hewan gelap', result)