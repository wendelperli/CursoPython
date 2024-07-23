s = 0
q = 0
for c in range(1, 501):
    if c % 2 != 0 and c % 3 == 0:
        q = q + 1
        s = s + c
        print(q, c, s)
print('A soma de todos os {} valores solicitados é de {}'.format(q, s))
