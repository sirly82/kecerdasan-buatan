from kanren import var, eq, run, conde

x = var()
result = run(2, x, eq(x, 100))
print(result)

y = var()
result = run(1, x, eq((x, y), (y, 3)))
print(result)

result = run(0, x, conde([eq(x, 1), eq(x,10)], [eq(x, 2)]))
print(result)