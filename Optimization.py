# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 15:26:35 2023

@author: Ashish chincholikar
Optimization in Machine Learning
reducing the values of the hyper-parameters

"""
import numpy as np

def gradient_descent(x,y):
    m_curr = b_curr = 0
    iterations = 10000
    n = len(x)
    learning_rate = 0.08
    """
    change the iterations and learning_rate parameters
    and observe the changes"""
    for i in range(iterations):
        y_predicted = m_curr * x + b_curr
        cost = (1/n) * sum([val**2 for val in (y-y_predicted)])
        md = -(2/n) * sum(x*(y-y_predicted))
        bd = -(2/n) * sum(y-y_predicted)
        m_curr = m_curr - learning_rate * md
        b_curr = b_curr - learning_rate * bd
        
        print("m {} , b{} , cost {} iteration {}".format(m_curr , b_curr, cost , i))

x = np.array([1,2,3,4,5])
y = np.array([5,7,9,11,13])
    
gradient_descent(x, y)