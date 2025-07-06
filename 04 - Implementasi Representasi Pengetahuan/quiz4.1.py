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
    A, B = map(Expr, 'AB')
    model = {A: False, B: True}

    # Query dasar
    query = (A & B)
    print(query, ' : ', is_true(query, model))

    # Query 1: not (A and B)
    query1 = ~(A & B)
    print("Query 1: not (A and B) : ", is_true(query1, model))

    # Query 2: not (A and B) or not (A or B)
    query2 = ~(A & B) | ~(A | B)
    print("Query 2: not (A and B) or not (A or B) : ", is_true(query2, model))

    # Query 3: not (A or B) and not (A and B)
    query3 = ~(A | B) & ~(A & B)
    print("Query 3: not (A or B) and not (A and B) : ", is_true(query3, model))

    # Query 4: not (A or B) and not (B)
    query4 = ~(A | B) & ~B
    print("Query 4: not (A or B) and not (B) : ", is_true(query4, model))