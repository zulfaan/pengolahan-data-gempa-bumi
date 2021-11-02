# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 03:02:28 2021

@author: Zulfa Nurfajar
"""
import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('seaborn')

data = pd.read_csv('data-gempa-bumi-jepang-2021.csv')
long = data['longitude']
lat = data['latitude']
depth = data['depth']



plt.plot(lat, depth,'o',color='black',\
        markeredgewidth=1)
plt.title('Persebaran Hiposentrum')
plt.xlabel('Latitude')
plt.ylabel('Depth (km)')
plt.ylim(max(depth)+50,-10)
plt.tight_layout()

plt.show()
plt.savefig("output/depth-latitude.png", dpi=300)
