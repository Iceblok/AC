import numpy as np

"""
Maak een functie die een matrix M en een vector v vermenigvuldigt.
"""


class DimensionError(Exception):
    pass


def matrix_product(M: np.ndarray, v: np.ndarray) -> np.ndarray:
    if len(M[0]) != len(v):
        raise DimensionError("Vectors niet hetzelfde formaat")
    else:
        matrix_product = np.array(((0,)*len(M)))
        for i, item in enumerate(M):
            count = 0
            for x, j in enumerate(item):
                count += j*v[x]
            matrix_product[i] = count
        return matrix_product


v = np.array((7, -7))
M = np.array(((2, 0), (17, 17), (2, 14)))

print(matrix_product(M, v))
