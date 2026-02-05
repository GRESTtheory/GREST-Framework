import math

def calculate_grest(g_newton):
    # Acceleration floor locked to H0 = 73.0 
    a0 = 1.129e-10 
    
    # Quadratic Metric Response Law 
    g_observed = math.sqrt(g_newton**2 + (g_newton * a0))
    
    return g_observed