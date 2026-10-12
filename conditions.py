p = True
q = False

#r = p + q
#print(r)
if p:
    print('p')
if q:
    print('q')

a = 4
b = 4
#
# if a <= b and (a < 5 or b > 7):
#     print('a < b')
#     print('2nd line here')
# else:
#     print('a > b')


def check_a_b(a, b):
    if a <= b and (a < 5 or b > 7):
        print('a < b')
        print('2nd line here')
    else:
        print('a > b')


check_a_b(4, 5)
check_a_b(7, 8)