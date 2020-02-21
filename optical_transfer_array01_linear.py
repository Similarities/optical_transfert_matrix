# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 14:36:33 2020

@author: similarities
"""

import numpy as np

import matplotlib.pyplot as plt



class optical_Transfer_matrix:
    def __init__(self, x, Theta):
        self.working_array = np.array([[1,0], [0,1]])
        self.working_array2 = np.array([[1,0], [0,1]])
        self.result_array = np.array([[1,0], [0,1]])
        self.vector_in = np.array([[x], [Theta]])
        self.vector_out = np.array([[x], [Theta]])
        
        
        
    def transfer(self, distance):       
        self.working_array = np.array([[1,distance],[0,1]])
        self.result_array = np.dot(self.working_array, self.result_array)
        return self.result_array
    
        
    def calculate_output(self):       
        self.vector_out = np.dot(self.result_array, self.vector_in)
        #print('output: x, Theta', self.vector_out)
        return self.vector_out
        
    
        
    def thin_lens(self, focal_length):      
        self.working_array2 = np.array([[1,0], [-1/focal_length,1]])
        self.result_array = np.dot(self.working_array2, self.result_array)
        return self.result_array
    
    
    def curved_mirror (self, curvature_radius):
        self.working_array2 = ([[1,0], [-2/curvature_radius,1]])
        self.result_array = np.dot(self.working_array2, self.result_array)
        return self.result_array
        
        
    
        

# input: vector [beam radius [m] = x] [Divergence [rad] = Theta]
# for collminated beam e.g. outer radius = x, Theta = 0
# all input parameter in [m]
my_optical_system = optical_Transfer_matrix(0.06, 0.)

my_optical_system.thin_lens(1.5)
my_optical_system.transfer(1.495)
my_optical_system.curved_mirror(0.0004)
my_optical_system.transfer(1.5)
my_optical_system.calculate_output()


def parameter_scan(radius):
    
    result = np.zeros([20])
    z_liste = np.zeros([20])
    #print(z_liste)
    
    for x in range (0,20):
        
        z = -0.001*x + 0.01
        
        optic = optical_Transfer_matrix(0.06, 0)
        optic.thin_lens(1.5)
        optic.transfer(1.5-z)
        optic.curved_mirror(radius)
        optic.transfer(1.5)
        #print(optic.calculate_output())
        
        result[x] = optic.calculate_output()[1]*1000
        z_liste[x] = z*1000


    plt.plot( z_liste, result, label = 'R: ' + str(radius))
    

     
              
        
        
    
        
parameter_scan(0.0004)
parameter_scan(0.001)
parameter_scan(0.01)


plt.xlabel('defocus in mm')
plt.ylabel('divergence halfange [mrad]')

plt.hlines(-0.06*1000/(1.5*25), -10, 10.0)
plt.vlines(0, -10,10)
plt.legend()





    


