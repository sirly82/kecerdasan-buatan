from ai_pkg.utils import Expr
# import sys
# sys.path.append(r"D:\SIRLY\Downloads\aima-python")
# from utils import Expr

def is_prop_symbol(s):
    """
    Cek apakah s adalah simbol proposisional.
    Simbol proposisional adalah string yang dimulai dengan huruf kapital.
    """
    return isinstance(s, str) and s[:1].isalpha() and s[0].isupper()

def is_true(exp, model={}):
    """
    Evaluasi ekspresi logika proposisional dalam model yang diberikan.
    exp : Expr atau boolean
    model : dictionary yang memetakan simbol proposisional ke nilai True/False
    """
    if exp in (True, False):
        return exp

    op, args = exp.op, exp.args

    if is_prop_symbol(op):
        return model.get(exp)

    elif op == '~':  # Negasi
        p = is_true(args[0], model)
        if p is None:
            return None
        else:
            return not p

    elif op == '|':  # Disjungsi (OR)
        result = False
        for arg in args:
            p = is_true(arg, model)
            if p is True:
                return True
            if p is None:
                result = None
        return result

    elif op == '&':  # Konjungsi (AND)
        result = True
        for arg in args:
            p = is_true(arg, model)
            if p is False:
                return False
            if p is None:
                result = None
        return result

    p, q = args

    if op == '==>':  # Implikasi
        return is_true(~p | q, model)

    elif op == '<==':  # Implikasi terbalik
        return is_true(p | ~q, model)

    pt = is_true(p, model)
    if pt is None:
        return None

    qt = is_true(q, model)
    if qt is None:
        return None

    if op == '<=>':  # Biimplikasi (ekuivalensi)
        return pt == qt

    elif op == '^':  # XOR (eksklusif OR)
        return pt != qt

    else:
        raise ValueError("Illegal operator: " + str(exp))

if __name__ == '__main__':
    # Definisikan Expr A, B, C, D
    A, B, C, D = map(Expr, 'ABCD')

    # Model awal: C = False, D belum ada (tidak didefinisikan)
    model = {A: False, B: True, C: False}

    # Query 1: (A or B) and (C or D)
    # Karena D belum didefinisikan di model, hasilnya bisa None jika D muncul
    query1 = (A | B) & (C | D)
    print("Query 1 dengan C=False dan D tidak didefinisikan:")
    print(query1, " : ", is_true(query1, model))

    # Query 2: (A and B) and (C or D)
    query2 = (A & B) & (C | D)
    print("Query 2 dengan C=False dan D tidak didefinisikan:")
    print(query2, " : ", is_true(query2, model))

    # Sekarang tambahkan D dengan nilai True ke model
    model[D] = True

    print("\nSetelah menambahkan D=True ke model:")

    print("Query 1 dengan C=False dan D=True:")
    print(query1, " : ", is_true(query1, model))

    print("Query 2 dengan C=False dan D=True:")
    print(query2, " : ", is_true(query2, model))