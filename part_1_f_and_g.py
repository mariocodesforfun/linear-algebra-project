import numpy as np
from numpy.typing import NDArray
from constants import T_MATRIX

def calculate_transpose(matrix: NDArray[np.float64]) -> NDArray[np.float64]:
    """Calculate the transpose of a given matrix."""
    return matrix.T

def calculate_eigenvalues_eigenvectors(matrix: NDArray[np.float64]) -> tuple[NDArray[np.float64], NDArray[np.float64]]:
    """Calculate the eigenvalues and eigenvectors of a given matrix."""
    return np.linalg.eig(matrix)

def matrix_power(matrix: NDArray[np.float64], n: int) -> NDArray[np.float64]:
    """Compute T^n using the diagonalization formula."""
    eigenvalues, eigenvectors = calculate_eigenvalues_eigenvectors(matrix)
    D_n = np.diag(eigenvalues**n)
    return eigenvectors @ D_n @ np.linalg.inv(eigenvectors)

# Define the transformation matrix T
T: NDArray[np.float64] = T_MATRIX

# Calculate the transpose of T
A: NDArray[np.float64] = calculate_transpose(T)
print("The transpose of the matrix is:")
print(A)

# Calculate the eigenvalues and eigenvectors of T
eigenvalues, eigenvectors = calculate_eigenvalues_eigenvectors(T)

# Print the eigenvalues and eigenvectors
print("The eigenvalues of T (D) are:")
print(eigenvalues)
print("The eigenvectors of T (P) are:")
print(eigenvectors)

# Print the diagonalization formula
print("\nThe diagonalization formula for T is: T = P D P^(-1)\n")

# Example: Compute T^3
n: int = 3
T_cubed: NDArray[np.float64] = matrix_power(T, n)

# Print the result
print(f"T^{n} is:")
print(T_cubed)
