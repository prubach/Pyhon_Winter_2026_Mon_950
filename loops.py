for i in range(10):
    print(i, end=' ')

print('\n' + '-'*60)

for i in range(2, 10):
    print(i, end=' ')

print('\n' + '-'*60)


for i in range(2, 10, 3):
    print(i, end=' ')

print('\n' + '-'*60)

for i in reversed(range(2, 10, 3)):
    print(i, end=' ')

print('\n' + '-'*60)

for i in range(10, 2, -1):
    print(i, end=' ')

print('\n' + '-'*60)

i = 0

while i < 10:
    i += 1
    if i == 3:
        continue
    print(i, end=' ')
    if i == 6:
        break
