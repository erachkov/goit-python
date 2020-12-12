def calc_quadratic_equations(a,b,c):  
    D = b**2 - 4*a*c
    if (D>0):
        x1 = (-b + D**0.5) / 2*a
        x2 = (-b - D**0.5) / 2*a
        return x1, x2
    elif  (D==0):
        x1 = -b / (2 * a)
        x2  = None
        return x1, x2
    else:
        return None, None      
    

a = input("Enter number a: ")
b = input("Enter number b: ")
c = input("Enter number c: ")

a = float(a)
b = float(b)
c = float(c)

x1, x2 = calc_quadratic_equations(a, b, c)
print(f"a = {a} b = {b},c = {c} => {a}x^2 + {b}x + {c} = 0")
print(f"x1 = {x1}, x2 = {x2}")

