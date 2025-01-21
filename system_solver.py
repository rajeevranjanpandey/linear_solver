import numpy as np

def solve_system(coefficients, constants):
    """
    Solve a system of linear equations: Ax = B.

    Args:
        coefficients (list of list): Coefficient matrix (A).
        constants (list): Constant terms (B).

    Returns:
        list: Solution vector (x) or an error message.
    """
    A = np.array(coefficients, dtype=float)
    B = np.array(constants, dtype=float)
    try:
        solution = np.linalg.solve(A, B)
        return solution.tolist()
    except np.linalg.LinAlgError:
        return "No unique solution exists."
