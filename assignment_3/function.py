def iterate_function(c, max_iter = 150):
    """
    This function returns iterations count at which the function z = z^2 + c diverges, or the maximum iteration value if it does       not escape. 
    
    Parameters
    ----------
    c: complex
       Input value complex number (x + iy). 
    max_iter: int
              Maximum number of times the function will iterate (defult is 150).
              
    Returns
    ----------
    float or int
        The number of iterations it took for the function to diverge. 
        Maximum iteration value if the function does not escape. 
    
    """
    z = 0 + 0j 
    
    for i in range(max_iter):
        
        z_new = z**2 + c
        z = z_new
        
        if abs(z_new) > 2:
            return i + 1
        
    return max_iter

