import numpy as np

# Define two matrices
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

print(matrix1)

# Addition
result_addition = matrix1 + matrix2
print("Addition of two matrices:")
print(result_addition)

# Subtraction
result_subtraction = matrix1 - matrix2
print("\nSubtraction of two matrices:")
print(result_subtraction)

# Multiplication
result_multiplication = np.dot(matrix1, matrix2)
print("\nMultiplication of two matrices:")
print(result_multiplication)

# Transpose
matrix3 = np.transpose(matrix1)
print("\nTranspose of the first matrix:")
print(matrix3)

# Determinant
determinant_matrix1 = np.linalg.det(matrix1)
print("\nDeterminant of the first matrix:")
print(determinant_matrix1)

# Inverse
inverse_matrix1 = np.linalg.inv(matrix1)
print("\nInverse of the first matrix:")
print(inverse_matrix1)

# Eigenvalues and Eigenvectors
eigen_values, eigen_vectors = np.linalg.eig(matrix1)
print("\nEigenvalues and Eigenvectors of the first matrix:")
print("Eigenvalues: ", eigen_values)
print("Eigenvectors: \n", eigen_vectors)
