<<<<<<< HEAD
#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()

    for i in range(len(matrix)):
        new_matrix[i] = list(map(lambda x: x**2, matrix[i]))

    return (new_matrix)
=======
>>>>>>> ed18fc1436307e280e012ecc50f8906d84e117a8
