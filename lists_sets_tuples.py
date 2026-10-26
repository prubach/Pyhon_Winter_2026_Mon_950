list_a = [1, 3, 5, 7, 8, 9]
list_b = [10, 12.3, 25.3]
print(f'list_a={list_a}')
print(f'list_b={list_b}')
list_c = list_a + list_b
print(f'list_c={list_c}')
print(f'list_a_2_5={list_a[2:5]}')

list_c.append(5)
print(f'list_c={list_c}')
list_c.extend([6, 7])
print(f'list_c={list_c}')
list_c.insert(2, 8)
print(f'list_c={list_c}')
print('-' * 60)
# remove by value - removes only first occurence
#list_c.remove(8)
print(f'list_c={list_c}')
if 8 in list_c:
    print(f' 8 is in list_c={list_c}')
while 8 in list_c:
    list_c.remove(8)
print(f'list_c={list_c}')

print('-' * 60)
list_c.pop(1)
print(f'list_c={list_c}')
#list_c.sort()
list_c.sort(reverse=True)
print(f'list_c={list_c}')

# Tuples - are immutable - we can't change them after they are created
tuple_a = (1, 3, 5, 7, 8, 9)
print(f'tuple_a={tuple_a}')
print(f'tuple_a[2]={tuple_a[2]}')
print(f'tuple_a[2:5]={tuple_a[2:5]}')
# tuple_a.append(3)  -
# tuple_a.remove(3)
# tuple_a[1] = 543
print(f'tuple_a={tuple_a}')


