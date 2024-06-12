import numpy as np
from numpy.typing import NDArray
from constants import T_MATRIX

def calculate_determinant(matrix: NDArray[np.float64]) -> float:
    """Calculate the determinant of a given matrix."""
    return np.linalg.det(matrix)

def calculate_transformed_area(determinant: float) -> float:
    """Calculate the area of the transformed square, which is the absolute value of the determinant."""
    return abs(determinant)

# Define the transformation matrix T
T: NDArray[np.float64] = T_MATRIX

# Calculate the determinant of T
det_T: float = calculate_determinant(T)
print(f"The determinant of T is {det_T:.4f}")

# Calculate the area of the transformed square
transformed_area: float = calculate_transformed_area(det_T)
print(f"The area of the transformed square is {transformed_area:.4f} square units.")
