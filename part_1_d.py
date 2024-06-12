import numpy as np
import matplotlib.pyplot as plt
from numpy.typing import NDArray
from constants import T_MATRIX

def define_unit_circle_points(num_points: int = 100) -> NDArray[np.float64]:
    """Define points on the unit circle."""
    theta = np.linspace(0, 2 * np.pi, num_points)
    return np.array([np.cos(theta), np.sin(theta)]).T

def apply_transformation(points: NDArray[np.float64], matrix: NDArray[np.float64]) -> NDArray[np.float64]:
    """Apply the transformation matrix to the given points."""
    return points @ matrix.T

def plot_circles(original: NDArray[np.float64], transformed: NDArray[np.float64]) -> None:
    """Plot the original and transformed circles."""
    plt.figure(figsize=(8, 8))
    plt.plot(original[:, 0], original[:, 1], 'b-', label='Original Circle')
    plt.plot(transformed[:, 0], transformed[:, 1], 'r-', label='Transformed Circle')
    plt.legend()
    plt.xlabel('$x_1$')
    plt.ylabel('$x_2$')
    plt.title('Image of Circle under Transformation $T$')
    plt.grid(True)
    plt.axis('equal')
    plt.show()

# Define the transformation matrix T
T: NDArray[np.float64] = T_MATRIX

# Define the unit circle points
circle: NDArray[np.float64] = define_unit_circle_points()

# Apply the transformation T to the circle points
transformed_circle: NDArray[np.float64] = apply_transformation(circle, T)

# Plot the original and transformed circles
plot_circles(circle, transformed_circle)

