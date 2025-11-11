# main.py
from sympy import symbols, Eq, solve, simplify, expand

# Define symbols
x, y = symbols('x y')

# 1️⃣ Solve an equation
equation = Eq(2*x + 3, 9)
solution = solve(equation)
print("Solution for 2x + 3 = 9:", solution)

# 2️⃣ Simplify an expression
expr = (x**2 + 2*x + 1)/(x + 1)
simplified = simplify(expr)
print("Simplified expression:", simplified)

# 3️⃣ Expand algebraic expression
expanded = expand((x + y)**3)
print("Expanded form of (x + y)^3:", expanded)
