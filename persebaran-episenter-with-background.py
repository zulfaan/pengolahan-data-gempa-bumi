# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 01:47:36 2021

@author: Zulfa Nurfajar
"""
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import cartopy.crs as ccrs


matplotlib.rcParams['figure.figsize'] = (25,10)


plt.style.use('seaborn')

#membaca data gempa bumi
data = pd.read_csv('data-gempa-bumi-jepang-2021.csv')

long = data['longitude']
lat = data['latitude']
magnitudo = data['Magnitude']
magnitudo_modifikasi = [Magnitude**2.5 for Magnitude in magnitudo]
depth = data['depth']

#plot peta persebaran
ax = plt.axes(projection = ccrs.PlateCarree())
ax.coastlines(resolution='50m')
ax.stock_img()
ax.set_extent([125, 149, 24.3, 46.5])
gl = ax.gridlines(draw_labels=True, color='black', alpha=.6, linestyle='--', dms=False, x_inline=False, y_inline=False, zorder=11)
gl.top_labels = False
gl.right_labels = False

eq = plt.scatter(long, lat, c=magnitudo, s=magnitudo_modifikasi, cmap="gist_ncar", alpha=1) # mengplot titik episenter
plt.xlabel("Longitude [deg]") #menambah label pada sumbu x
plt.ylabel("Latitude [deg]") # menambah label pada sumbu y
plt.title("Peta Episentrum di Wilayah Jepang pada Tahun 2021") #keterangan waktu pada judul

plt.colorbar(label="Magnitude [Mw]")
plt.savefig("output/persebaran-magnitudo.png", dpi=300)
