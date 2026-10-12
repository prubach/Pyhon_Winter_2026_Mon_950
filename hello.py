print("hello world")
print('2nd line', end='')
print(' continueing 2nd line')

a = 463.4234
t_a = type(a)
print(f'type of a: {t_a}')
b = 563
c = a + b
t_c = type(c)
print(f'type of c: {t_c}')
print(f'c={c}')
print('c=' + str(c))

i_a = 2535367743568426526354654937676509265017514712526578365872347658726387562385
i_b = 5698672367326739267983769873257360971096729762093769802736097296723906723976
max_int = i_a + i_b
print(f'max_int={max_int}')
s_a = str(i_a)
print(f'type(s_a): {type(s_a)}')
print(f'len o s_a={len(s_a)}')