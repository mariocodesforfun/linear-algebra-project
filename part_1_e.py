import numpy as np
from numpy.typing import NDArray
from constants import T_MATRIX

def calculate_determinant(matrix: NDArray[np.float64]) -> float:
    """Calculate the determinant of a given matrix."""
    return np.linalg.det(matrix)

def calculate_transformed_area(original_area: float, determinant: float) -> float:
    """Calculate the area of the transformed circle."""
    return abs(determinant) * original_area

# Define the transformation matrix T
T: NDArray[np.float64] = T_MATRIX

# Calculate the determinant of T
det_T: float = calculate_determinant(T)

# Original area of the circle
original_circle_area: float = np.pi

# Area of the transformed circle
transformed_circle_area: float = calculate_transformed_area(original_circle_area, det_T)

# Print the area of the transformed circle
print(f"The area of the transformed circle is {transformed_circle_area:.4f} square units.")
