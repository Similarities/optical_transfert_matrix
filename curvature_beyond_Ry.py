# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 10:52:30 2020

@author: julie
"""

import numpy as np
import math


import csv


import matplotlib.pyplot as plt



def Denting_to_radius(sagitta, s):
    
    R = (4*(sagitta **2) + (s **2))/(8*sagitta)
    print('radius of curvature in mm', R)
    
    return R


# radius of curvature for focusing Gaussian beam, Ry is Rayleigh length alls units in [um]
def radius_of_wavefront(Ry, distance):
    R_laser = distance *(1 + (Ry/distance) **2) **0.5
    
    print('Radius of curvature wavefront: ', R_laser, ' at distance:', distance)
    
    if R_laser < 0:
        sign = -1
    else: 
        sign = 1
    
    return R_laser, sign
    


# Radius of curvature in [um], Denting depth in [um], ymax [um], sign +/- for form inwards or outwards

def radius_to_x_position(R, s, sign):
    
    y_list = list(range(0, s))

    x_list = [0] *s 

    for x in y_list:

    # x coordinate von kreis

        x_list[x] =sign * abs((R**2 - (x) **2) ** 0.5)
    
    # x kooridinte von Kreis verschoben, damit y0 die 0 markiert
    

    offset = x_list[-1]
    
    x_list = [ val -offset for val in x_list]
         
    return y_list, x_list

D0 = 0.100
R_D0 = Denting_to_radius(D0, 60)
distance = -2500

R_laser, sign = radius_of_wavefront(630, distance)

    
y_list_wave, x_list_wave = radius_to_x_position(R_laser, 60, sign)
y_list_denting, x_list_denting = radius_to_x_position(R_D0,60, -1)

def calc_difference_with_offset(liste1x, liste1y, liste2x, liste2y):
    
    new = [0]*len(liste1x)
    
    for x in range(0, len(liste1x)):
        new[x] = liste1x[x]-liste2x[x]
        
    offset = new[-1]
    
    new = [ val -offset for val in new]
        
    print(new[0], 'maximum on axis in um')
        
    return new
        
        
        


new = calc_difference_with_offset(x_list_wave, y_list_wave, x_list_denting, y_list_denting)

plt.plot(y_list_wave, x_list_wave, label = 'wavefront at distance: ' +str(distance) + ' um')
plt.plot (y_list_denting, x_list_denting, label = 'denting ' + str(D0*1000) +' nm')

plt.plot(y_list_wave, new, label = 'difference')
plt.xlabel('[um]')
plt.ylabel('curvature depth in [um]')

plt.legend()


    
    
    