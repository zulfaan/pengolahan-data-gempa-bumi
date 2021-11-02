# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 22:50:54 2021

@author: Zulfa Nurfajar
"""
import numpy as np
from scipy.sparse.linalg import lsqr
import matplotlib.pyplot as plt

data = np.genfromtxt('data-value-new.csv', skip_header=1, delimiter=',')
magnitude = data[:, 0]
frequency = data[:, 1]

M = np.array(magnitude)
logN = np.array(np.log10(frequency))
M1 = np.column_stack((M, np.ones(np.shape(M)[0])))
grad = lsqr(M1, logN)[0]
a = grad[1]
b = grad[0]*-1
print('a-value is: ','%.2f' %a)
print('b-value is: ','%.2f' %b)


y_akhir = -1*b*M+a
plt.plot(M, logN, 'ko', label='Data', color='indigo')
plt.plot(M, y_akhir , '--', label='Regresi', color='cyan')
plt.xlabel('Magnitude')
plt.ylabel('Log N')
plt.legend()
plt.title('Data VS Regresi')
plt.show()
