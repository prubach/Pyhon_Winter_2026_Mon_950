s1 = 'abcdef'
print(f's1={s1}')
#geheh
'''
This is a multiline comment

'''
# s1_sub = s1[0:4]
s1_sub = s1[:4]
print(f's1_sub={s1_sub}')
s2_sub = s1[4:]
print(f's2_sub={s2_sub}')

s3_sub = s1[4]
print(f's3_sub={s3_sub}')

a = 9
b = '9'
print(f'type a={type(a)}, type b={type(b)}')
print(f'a={a}, b={b}')

s_a = str(a)
s_a = '22525'
i_a = int(s_a)
print(f' type s_a={type(s_a)}, type i_a={type(i_a)}')
print(f'i_a={i_a}')

s_a = '22.53636525e34'
f_a = float(s_a)
print(f' type s_a={type(s_a)}, type f_a={type(f_a)}')
print(f'f_a={f_a}')

s1 = 'abcdef'
s2 = 'ghijkl'
print(f's1={s1}, s2={s2}')
s3 = s1 + s2
print(f's3={s3}')
len_s3 = len(s3)
print(f'len_s3={len_s3}')

s3 = 'abcdef efg'
sub_ind = s3.find('ef')
print(f'sub_ind={sub_ind}')


