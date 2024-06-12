import numpy as np

# Define the matrix A (the transpose of T in this case)
A = np.array([[0.95, 0.04],
              [0.05, 0.96]])

# Direct calculation of A^3
A_direct_cubed = np.linalg.matrix_power(A, 3)

# Calculate the eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

# Print the eigenvalues and eigenvectors
print("The eigenvalues of A (D) are:")
print(eigenvalues)
print("The eigenvectors of A (P) are:")
print(eigenvectors)

# Diagonal matrix of eigenvalues raised to the power 3 (D^3)
D_cubed = np.diag(eigenvalues**3)

# Reconstruct A^3 using the diagonalization formula A^3 = P D^3 P^(-1)
A_diagonalization_cubed = eigenvectors @ D_cubed @ np.linalg.inv(eigenvectors)

# Print the formula for A^n
print("\nThe formula for A^n is: A^n = P D^n P^(-1)\n")

# Print the directly computed A^3
print("Directly computed A^3 is:")
print(A_direct_cubed)

# Print the A^3 computed using the diagonalization formula
print("\nA^3 computed using the diagonalization formula is:")
print(A_diagonalization_cubed)
