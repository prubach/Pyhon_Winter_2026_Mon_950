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


