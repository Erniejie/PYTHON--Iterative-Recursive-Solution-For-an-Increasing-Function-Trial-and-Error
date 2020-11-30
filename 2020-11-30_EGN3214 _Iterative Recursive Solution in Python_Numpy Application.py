"""
Iterative Recursive Solution in Python-Engineering
Simpler than the general Newton-Raphson equations
but tailored to more specific INCREASING or decreasing functions),
the technique is simple and easy to be  implemented.
"""
#  we are not solving for "y" but for "x".ie.: given "y"- how do we find "x"
#TRIAL AND ERROR:ITERATIVE RECURSIVE SOLUTION FOR A INCREASING FUNCTION
   #Logical Explanation Summary:
   # x_start: x to start looking
   # x_max: don't go over this x
   # x_step: increment x by this
   # target: y value We are looking for
   # accuracy: how close We want to be


import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.1,1,101)  # we can also use "arange", instead of "linspace"
y = np.log(x) + np.tan(x)

plt.plot(x,y,"r+")

def f(x):
    return np.log(x) + np.tan(x)

def t_and_error(x_start,x_max,x_step,target,accuracy):
    i = np.arange(x_start,x_max,x_step) #np.arange-it creates array from start to max with increment step

    for x_guess in i:
        y_guess = f(x_guess)
        print("x:{:.5f} y:{:.5f} target:{:.5f}".format(x_guess,y_guess,target))

        if np.abs(y_guess-target) < accuracy:  # to be found it
            #return i
            return x_guess

        if y_guess > target:
            print("**** Overshot- Back up and Reduce step to {:.6f}".format(x_step/10))
            return t_and_error(x_guess-x_step, x_max, x_step/10, target,accuracy)

    return x_max

answer = t_and_error(0.1,1,0.1,1,0.0001)
i = np.linspace(0,1,0,0.1)

plt.show()
            
    
