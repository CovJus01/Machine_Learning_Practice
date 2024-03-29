import numpy as np
import matplotlib.pyplot as plt
import copy
import math


#************************* UNIVARIATE FUNCTIONS *************************

def computeUnivariateCost(x, y, w, b): 
    """
    Computes the cost function for linear regression. 
    This method is specific to one feature, hence the univariate
    
    Args:
        x (ndarray): Shape (m,) Input feature data
        y (ndarray): Shape (m,) Output results for given inputs
        w, b (scalar): Parameters of the model
    
    Returns
        total_cost (float): The cost of using w,b as the parameters for linear regression
               to fit the data points in x and y
    """
    #Size of training set
    m = x.shape[0] 
    total_cost = 0
    
    #Total Cost summation (1/2m)*sum((f_wb(x[i]) - y[i])**2)
    for i in range(m):
        prediction = w*x[i] + b
        total_cost += (prediction - y[i])**2
    total_cost /= (2*m)

    return total_cost


def computeUnivariateGradient(x, y, w, b): 
    """
    Computes the gradient for linear regression
    This method is specific to one feature, hence the univariate
    Args:
      x (ndarray): Shape (m,) Input feature data
      y (ndarray): Shape (m,) Output results for given inputs
      w, b (scalar): Parameters of the model 
    Returns
      dj_dw (scalar): The gradient of the cost w.r.t. the parameter w
      dj_db (scalar): The gradient of the cost w.r.t. the parameter b     
     """
    
    # Size of training set
    m = x.shape[0]
    dj_dw = 0
    dj_db = 0
    
    # Gradient summations
    for i in range(m):
        prediction = w*x[i] + b
        dj_dw += (prediction - y[i]) * x[i]
        dj_db += (prediction - y[i])
    dj_dw /= m
    dj_db /= m
    
    return dj_dw, dj_db


def univariateGradientDescent(x, y, w_in, b_in, cost_function, gradient_function, alpha, num_iters): 
    """
    Performs batch gradient descent to learn parameters w,b. Updates w & b for
    num_iters gradient steps with learning rate alpha
    
    Args:
      x :    (ndarray): Shape (m,)
      y :    (ndarray): Shape (m,)
      w_in, b_in : (scalar) Initial values of parameters of the model
      cost_function: function to compute cost
      gradient_function: function to compute the gradient
      alpha : (float) Learning rate
      num_iters : (int) number of iterations to run gradient descent
    Returns
      w : (ndarray): Shape (1,) Updated values of parameters of the model after
          running gradient descent
      b : (scalar)                Updated value of parameter of the model after
          running gradient descent
    """
    
    # Size of training set
    m = len(x)
    # An array to store cost J and w's at each iteration — primarily for graphing later
    J_history = []
    w_history = []
    w = copy.deepcopy(w_in)  #avoid modifying global w within function
    b = b_in
    
    for i in range(num_iters):

        # Calculate the gradient and update the parameters
        dj_dw, dj_db = gradient_function(x, y, w, b )  

        # Update Parameters using w, b, alpha and gradient
        w = w - alpha * dj_dw               
        b = b - alpha * dj_db               

        # Save cost J 
        if i<100000:      # prevent resource exhaustion 
            cost =  cost_function(x, y, w, b)
            J_history.append(cost)

        # Save w
        if i% math.ceil(num_iters/10) == 0:
            w_history.append(w)
            print(f"Iteration {i:4}: Cost {float(J_history[-1]):8.2f}   ")
        
    return w, b, J_history, w_history 

