def f(x):
    return x**3 + 2*x + 2

def secant_method(x0, x1, tol=1e-7, max_iter=100):
    for _ in range(max_iter):
        fx0 = f(x0)
        fx1 = f(x1)
        if fx1 - fx0 == 0:
            break      
        x_new = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        if abs(x_new - x1) < tol:
            return x_new       
        x0 = x1
        x1 = x_new
        
    return x1

root = secant_method(-2.0, 0.0)
print(root)

"""Standard equation here is x**3 + 2*x + 2, sometimes taking derivatives like we do in newton's method
either is complex or computationally heavy, so we calculate slope ourselves in secant method, we take two guesses
(x0 and x1) like we did in bisection method and we draw a secant line through our two guesses, where that line
crosses x-axis becomes our new guess(Xn + 1), formula we generally use is Xn+1 = Xn-f(Xn)*Xn-Xn-1/f(Xn)-f(Xn-1)
we do tolerance check here as well to check if our solution is withing acceptable range or not if not we loop again,

Note: Secant method has convergence of 1.62 which is also called golden ratio that means it is faster than 
bisection method and but slightly slower than Newton's method, but it also suffers from same problem as that of
Newton's method i.e it might overshoot """