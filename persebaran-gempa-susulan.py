# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 21:25:27 2021

@author: Zulfa Nurfajar
"""
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import cartopy.crs as ccrs


matplotlib.rcParams['figure.figsize'] = (25,10)


plt.style.use('seaborn')

#membaca data gempa bumi
data = pd.read_csv('gempa-utama-gempa-susulan.csv')
utama = pd.read_csv('gempa-utama.csv')
long = data['Longitude']
lat = data['Latitude']
magnitudo = data['Magnitude']
magnitudo_modifikasi = [Magnitude**2.5 for Magnitude in magnitudo]
depth = data['depth']

#plot peta persebaran
ax = plt.axes(projection = ccrs.PlateCarree())
ax.coastlines(resolution='110m')
ax.stock_img()
ax.set_extent([139, 144, 36, 40])
gl = ax.gridlines(draw_labels=True, color='black', alpha=.6, linestyle='--', dms=False, x_inline=False, y_inline=False, zorder=11)
gl.top_labels = False
gl.right_labels = False
# mengplot titik episenter gempa susulan
eq = plt.scatter(long, lat, c=magnitudo, s=magnitudo_modifikasi, label="Gempa Susulan", cmap="gnuplot2", alpha=1) 
# mengplot titik episenter gempa utama
ez = plt.plot(utama['longitude'], utama['latitude'],'b*', markersize=15,markerfacecolor='blue',\
        markeredgewidth=1,label='Gempa Utama')
plt.xlabel("Longitude [deg]") #menambah label pada sumbu x
plt.ylabel("Latitude [deg]") # menambah label pada sumbu y
plt.title("Peta Sebaran Energi Gempa Utama dan Susulan") #keterangan waktu pada judul

plt.colorbar(label="Magnitude [Mw]")
plt.legend(loc="upper right")
plt.savefig("output/persebaran-episenter-gempa-susulan.png", dpi=300)
