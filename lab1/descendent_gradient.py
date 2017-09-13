
from numpy import *

def compute_error_for_given_points(b, m, points):
    total_error = 0
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        total_error += (y - (m * x + b)) ** 2
    return total_error / float(len(points))    

def step_gradient(b_current, m_current, points, learning_rate):
    #gradient descent 
    b_gradient, m_gradient = 0,0
    N = float(len(points))
    
    for i in range(0,len(points)):
        x,y = points[i,0],points[i,1]
        b_gradient += -(2/N) * (y - ((m_current * x) + b_current))
        m_gradient += -(2/N) * x * (y - ((m_current * x) + b_current))
    new_b = b_current - (learning_rate * b_gradient)
    new_m = m_current - (learning_rate * m_gradient)    
    return [new_b, new_m]

def gradient_descent_runner(points, starting_b, starting_m, \
 learning_rate, tolerance):
     b,m = starting_b, starting_m
     i = 0
     while(compute_error_for_given_points(b, m, points) > tolerance):
     #for i in range(num_iterations):
         i += 1
         b, m = step_gradient(b,m,array(points),learning_rate)
         print "Printing:  iteration = {0}, RSS = {1}".\
          format(i + 1, compute_error_for_given_points\
          (b, m, points))
     return [b, m]    

def run():
    points = genfromtxt('income.csv', delimiter=',')
    #hiperparametro
    learning_rate =  0.0008 
    #funcao  y = mx + b
    initial_b, initial_m = 0,0
    num_iterations = 59900
    tolerance = 29.83
    print "Starting gradient descent at b = {0}, m = {1}, error = {2}".\
     format(initial_b, initial_m, compute_error_for_given_points\
     (initial_b, initial_m, points))
    print "Running..."
    [b, m] = gradient_descent_runner(points, initial_b, initial_m, \
     learning_rate, tolerance)
    print "After {0} iterations b = {1}, m = {2}, error = {3}".\
     format(num_iterations, b, m, compute_error_for_given_points\
     (b, m, points))

if __name__ == '__main__':
    run()
