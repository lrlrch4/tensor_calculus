from sympy import latex,lambdify
from IPython.display import display, Math 
from numpy import linspace
import matplotlib.pyplot as plt

def printex(symbol, value):    
    display(Math(symbol + latex(value)))
    
    
def latex_printer(title, expressions=[]):    
    
    display(Math(r'\Large %s' % title))

    for i in range(len(expressions)): 

        display(Math(r'\Large %s' % expressions[i]))
        

def graph_function(f, x, xmin=-10, xmax=10):
    
    f_numeric = lambdify(x, f, 'numpy')
    
    x_vals = linspace(xmin, xmax, 1000)
    y_vals = f_numeric(x_vals)

    plt.plot(x_vals, y_vals)
    plt.xlabel('x')
    plt.ylabel(f"{latex(f)}_{{(x)}}")
    plt.title(f'Gráfico de {latex(f)}')
    plt.grid()
    plt.show()