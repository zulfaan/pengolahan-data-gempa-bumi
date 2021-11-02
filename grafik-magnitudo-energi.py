# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 23:22:05 2021

@author: Zulfa Nurfajar
"""
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np


plt.style.use('seaborn')

data = pd.read_csv('data-gempa-bumi-jepang-2021.csv')

M = data['Magnitude']
c = 11.8 + 1.5*M
E = 10**c
print(np.mean(E))
plt.plot(M,E)

plt.gcf().autofmt_xdate()

plt.title('Grafik Energi Terhadap Magnitudo')
plt.xlabel('Magnitudo')
plt.ylabel('Energi')
plt.yscale('log')
plt.tight_layout()

plt.show()
plt.savefig("output/grafik-magnitudo-energi.png", dpi=300)