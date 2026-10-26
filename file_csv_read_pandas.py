import os

my_file = os.path.join('data', 'rates.csv')
rates = {}

import pandas as pd

df = pd.read_csv(my_file)
rates = df.set_index('Currency')['Value'].to_dict()
print(rates)
