import os

my_file = os.path.join('data', 'rates.csv')
rates = {}
# Contributed by Dariusz Jadowski
with open(my_file, 'r') as f:
    lines = f.readlines()
    for line in lines[1:]:  # pomija header
        line = line.strip()
        if not line:
            continue
        currency, value = line.split(',')
        value = float(value)
        rates[currency] = float(value)

print(rates)

amount = 100
result = amount / rates['PLN'] * rates['USD']
print(f"{amount} PLN = {result:.2f} USD")
