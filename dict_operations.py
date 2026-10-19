my_currencies = { 'USD': 1, 'EUR': 1.1}

print(my_currencies)

my_currencies['USD'] = 1.5
my_currencies['PLN'] = 4
print(my_currencies)
#for key, value in my_currencies.items():
#    print(key, value)

#print(my_currencies['PLN'])
#print(my_currencies.get('PLN'))
print(my_currencies.get('PLN', 3))


print('-------------------')
for key in my_currencies.keys():
    print(key, my_currencies.get(key))
    print(key, my_currencies[key])

print('-------------------')
print(list(my_currencies.values()))