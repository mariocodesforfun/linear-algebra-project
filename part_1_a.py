import numpy as np
from constants import T_MATRIX

def calculate_determinant(matrix: np.ndarray) -> float:
    """Calculate the determinant of a given matrix."""
    return np.linalg.det(matrix)

def check_linear_transformation(matrix: np.ndarray) -> str:
    """Check if the linear transformation defined by the matrix is one-to-one and onto."""
    det_T = calculate_determinant(matrix)
    if det_T != 0:
        return "Since the determinant is non-zero, the linear transformation T is one-to-one and onto."
    else:
        return "Since the determinant is zero, the linear transformation T is not one-to-one and onto."



T = T_MATRIX
det_T = calculate_determinant(T)
print(f"The determinant of T is {det_T}")
result = check_linear_transformation(T)
print(result)



