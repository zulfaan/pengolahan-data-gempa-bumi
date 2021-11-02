# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 00:10:41 2021

@author: Zulfa Nurfajar
"""
import pandas as pd
import matplotlib.pyplot as plt


plt.style.use('seaborn')

#membaca data gempa bumi
data = pd.read_csv('data-gempa-bumi-jepang-2021.csv')
data['time'] = pd.to_datetime(data['time'])
data.sort_values('time', inplace=True)

t = data['time']
long = data['longitude']
lat = data['latitude']
magnitudo = data['Magnitude']
magnitudo_modifikasi = [Magnitude**2.5 for Magnitude in magnitudo]
depth = data['depth']

eq = plt.scatter(long, lat, c=depth, s=magnitudo_modifikasi, label="Episenter", cmap="jet", alpha=1) # mengplot titik episenter
plt.xlabel("Longitude [deg]") #menambah label pada sumbu x
plt.ylabel("Latitude [deg]") # menambah label pada sumbu y
plt.title("Persebaran Gempa Bumi di Jepang pada Tahun2021") #keterangan waktu pada judul

plt.colorbar(label="Kedalaman [km]")
plt.legend(*eq.legend_elements("sizes", num=4, func=lambda x: x**(1/2.5)))
plt.savefig("output/persebaran-episenter.png", dpi=300)