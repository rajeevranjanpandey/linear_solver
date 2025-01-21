from single_equation import solve_single
from system_solver import solve_system

# Solve a single-variable equation
print("Solving single-variable equation:")
single_solution = solve_single(3, -9)  # 3x - 9 = 0
print(f"Solution for 3x - 9 = 0: x = {single_solution}")

# Solve a system of equations
print("\nSolving system of equations:")
coefficients = [[3, 2], [1, 4]]
constants = [8, 6]
system_solution = solve_system(coefficients, constants)
print("Solution for the system is:", system_solution)
