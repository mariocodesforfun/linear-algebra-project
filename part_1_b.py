import numpy as np
import matplotlib.pyplot as plt
from numpy.typing import NDArray
from constants import T_MATRIX

def define_square() -> NDArray[np.float64]:
    """Define the vertices of a square."""
    return np.array([[0, 0],
                     [1, 0],
                     [1, 1],
                     [0, 1],
                     [0, 0]], dtype=np.float64)  # Closing the square

def apply_transformation(square: NDArray[np.float64], matrix: NDArray[np.float64]) -> NDArray[np.float64]:
    """Apply the transformation matrix to the square vertices."""
    return square @ matrix.T

def plot_squares(original: NDArray[np.float64], transformed: NDArray[np.float64]) -> None:
    """Plot the original and transformed square."""
    plt.figure(figsize=(8, 8))
    plt.plot(original[:, 0], original[:, 1], 'b-', label='Original Square')
    plt.plot(transformed[:, 0], transformed[:, 1], 'r-', label='Transformed Square')
    plt.legend()
    plt.xlabel('$x_1$')
    plt.ylabel('$x_2$')
    plt.title('Image of Square under Transformation $T$')
    plt.grid(True)
    plt.axis('equal')
    plt.show()

T = T_MATRIX
square = define_square()
transformed_square = apply_transformation(square, T)
plot_squares(square, transformed_square)
