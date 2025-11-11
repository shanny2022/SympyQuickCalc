# main.py
from sympy import symbols, Eq, solve, simplify, expand, sympify
import sys

def show_menu():
    print("\n🧮 Sympy Quick Calculator")
    print("1️⃣  Solve an equation")
    print("2️⃣  Simplify an expression")
    print("3️⃣  Expand an expression")
    print("4️⃣  Exit")

def solve_equation():
    expr = input("Enter an equation (e.g., 2*x + 3 = 9): ")
    if "=" not in expr:
        print("❌ Equation must contain '='")
        return
    left, right = expr.split("=")
    x = symbols("x")
    eq = Eq(sympify(left), sympify(right))
    sol = solve(eq, x)
    print("✅ Solution:", sol)

def simplify_expression():
    expr = input("Enter an expression to simplify (e.g., (x**2 + 2*x + 1)/(x+1)): ")
    x = symbols("x")
    simplified = simplify(sympify(expr))
    print("✅ Simplified:", simplified)

def expand_expression():
    expr = input("Enter an expression to expand (e.g., (x + y)**3): ")
    x, y = symbols("x y")
    expanded = expand(sympify(expr))
    print("✅ Expanded:", expanded)

def main():
    while True:
        show_menu()
        choice = input("\nChoose an option (1-4): ")
        if choice == "1":
            solve_equation()
        elif choice == "2":
            simplify_expression()
        elif choice == "3":
            expand_expression()
        elif choice == "4":
            print("👋 Goodbye!")
            sys.exit()
        else:
            print("❌ Invalid choice. Please select 1-4.")

if __name__ == "__main__":
    main()
