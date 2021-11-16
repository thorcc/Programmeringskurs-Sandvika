def derivert(f, x, delta_x=0.0001):
    return (f(x + delta_x) - f(x)) / delta_x

def l_hopital(f, g, a):
    #lim x->a f(x) / g(x) = f'(a) / g'(a)
    return derivert(f,a) / derivert(g,a)


# Eksempel
# lim x -> 5 (5x - 25) / (3x^2 - 75)
def f(x):
    return 5*x - 25
def g(x):
    return 3*x**2 - 75

print(f'lim x -> 5 (5x - 25) / (3x^2 - 75) = {l_hopital(f, g, 5)}')