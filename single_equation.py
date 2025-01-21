def solve_single(a, b):
    """
    Solve a single linear equation of the form ax + b = 0.

    Args:
        a (float): Coefficient of x.
        b (float): Constant term.

    Returns:
        float: Solution for x.
    """
    if a == 0:
        if b == 0:
            return "Infinite solutions exist."
        else:
            return "No solution exists."
    return -b / a
