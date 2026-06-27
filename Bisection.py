def f(x):
    return x**3+2*x+2

def bisection_method(a, b, tol):
    if f(a) * f(b) >= 0:
        print("fail")
        return None
    
    err = (b - a)/2
    
    while err > tol:
        c = (a + b)/2

        if f(c) == 0:
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c

        err = (b - a)/2

    return (a + b) / 2

final_answer = bisection_method(-2.0, 0.0, 1e-15)
print(final_answer)


check_number = (-0.7709169970592482)**3 + 2*(-0.7709169970592482) + 2
print(check_number)



"""This code is to check when does eqn x^3+2x+2 crosses the x-axis
and later out put is check in "check_number" eqn 
the output will be -4.440892098500626e-16 , why is not along the line of 0.000 something
it is just take e-16 to account and shift -4.44 to right , this is due to micro - rounding errors in 16th decimal place """