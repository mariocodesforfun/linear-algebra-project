import numpy as np
from numpy.typing import NDArray
from constants import MIGRATION_MATRIX

def print_matrix(matrix: NDArray[np.float64], name: str) -> None:
    """Print a matrix with a given name."""
    print(f"The {name} matrix is:")
    print(matrix)

def check_matrices_relationship(matrix1: NDArray[np.float64], matrix2: NDArray[np.float64]) -> str:
    """Check if one matrix is the transpose of the other."""
    if np.allclose(matrix1, matrix2.T):
        return f"\nThe matrix {matrix1} is the transpose of the matrix {matrix2}."
    else:
        return f"\nThe matrix {matrix1} is not the transpose of the matrix {matrix2}."

# Define the migration matrix M
M: NDArray[np.float64] = MIGRATION_MATRIX

# Print the migration matrix
print_matrix(M, "migration")

# Define the transformation matrix T from Part I
T: NDArray[np.float64] = np.array([[0.95, 0.05], [0.04, 0.96]])

print_matrix(T, "transformation from Part I")

# Check if M and T are related
relationship: str = check_matrices_relationship(M, T)
print(relationship)
