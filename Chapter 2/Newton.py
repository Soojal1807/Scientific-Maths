def f(x):
    return x**3 + 2*x + 2

def df(x):
    return 3*x**2 + 2

def newtons(x0, tol=1e-7, max_iter=100):
    x = x0
    for _ in range(max_iter):
        fx = f(x)
        dfx = df(x)
        if dfx == 0:
            break
        x_new = x - fx / dfx
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    return x

root = newtons(-1.0)
print(root)


"""x**3 + 2*x + 2 is the standard equation we are testing for for newton's method
 3*x**2 + 2 is obtained after differentiating the eqn, x0 is x-naught, x0 is our singular initial guess
 we are taking here, our core formula is  Xn+1 = Xn-f(Xn)/f'(Xn) ,this is called Newton-Raphson Formula
  at the end we check if distance between our old guess and new guess is in tolerance limit or not because
   getting exact answer in computational mathematics is almost impossible so we need to closest to correct value,
    if our answer is not close enough we loop back again.
     
      Note: convergence of Newton's method is generally 2 """  
