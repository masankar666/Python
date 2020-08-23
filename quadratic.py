# import complex math module
import cmath

# coefficients of a quadratic equation
a = 1
b = 5
c = 6

# calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions
root1 = (-b-cmath.sqrt(d))/(2*a)
root2 = (-b+cmath.sqrt(d))/(2*a)

print('The roots are:')
print(root1)
print(root2)
