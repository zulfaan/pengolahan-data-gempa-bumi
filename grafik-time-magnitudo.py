# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 19:42:23 2021

@author: Zulfa Nurfajar
"""
import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('seaborn')

data = pd.read_csv('data-gempa-bumi-jepang-2021.csv')

data['time'] = pd.to_datetime(data['time'])
data.sort_values('time', inplace=True)

plt.plot(data['time'],data['Magnitude'], 'o')

plt.gcf().autofmt_xdate()

plt.title('Grafik Magnitudo vs Waktu')
plt.xlabel('Time')
plt.ylabel('Magnitudo')

plt.tight_layout()

plt.show()
plt.savefig("output/grafik-time-magnitudo.png", dpi=300)