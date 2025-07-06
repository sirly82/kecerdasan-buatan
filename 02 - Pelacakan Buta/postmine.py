from kanren.facts import facts, fact, Relation
from kanren.core import var, run

cuaca = Relation()
suhu = Relation()
feel_bad = Relation()

facts(cuaca,    ('jambi', 'hujan'),
                ('yogyakarta', 'panas'),
                ("bandung", "berawan"),
                ("surabaya", "berawan"),
                ("bogor", "hujan"))

facts(suhu, ('jambi', 'rendah'),
            ('yogyakarta', 'tinggi'),
            ("bandung", "rendah"),
            ("surabaya", "tinggi"),
            ("bogor", "rendah"))

fact(feel_bad, 'hujan')
fact(feel_bad, 'panas')

kota_x = var()
cuaca_y = var()

hujan = run(0, kota_x,cuaca(kota_x, 'hujan'))
print('Kota yang sedang hujan: \n', hujan)

# Kota yang cuaca tidak menyenangkan
feel_bad_r = run(0, kota_x, cuaca(kota_x, cuaca_y), feel_bad(cuaca_y))
print('Kota dengan cuaca tidak menyenangkan: \n', feel_bad_r)

# Kota tidak menyenangkan dan suhu tinggi
result = run(0, kota_x, cuaca(kota_x, cuaca_y), feel_bad(cuaca_y), suhu(kota_x, 'tinggi'))
print('Kota dengan cuaca tidak menyenangkan dan suhu tinggi: \n', result)