import numpy as np

"""
Maak een functie die een matrix M en een vector v vermenigvuldigt.
"""

class DimensionError(Exception):
    pass

def inner_product(u: np.ndarray, v: np.ndarray) -> np.ndarray:
    """
    Function returns the inner product of given Vectors
    Example;
    :param u: np.ndarray, np.array([12, -5])
    :param v: np.ndarray, np.array([12, -5])
    :return: result_inner_product: np.ndarray, np.array([169.])
    """
    if u.shape[0] != v.shape[0]:
        raise DimensionError("Vectors niet hetzelfde formaat")
    else:
        result_inner_product = np.zeros(1)
        for i in range(v.shape[0]):
            result_inner_product[0] += u[i] * v[i]
        return result_inner_product


def matrix_vector(M: np.ndarray, v: np.ndarray) -> np.ndarray:
    """
    Function multiplies the given Matrix with a given Vector
    Example;
    :param M: np.ndarray, np.array(([2, 0], [17, 17], [2, 14]))
    :param v: np.ndarray, np.array([7, -7])
    :return: result_matrix_vector: np.ndarray, [ 14.   0. -84.]
    """
    if M.shape[1] != v.shape[0]:
        raise DimensionError("Vectors niet hetzelfde formaat")

    else:
        result_matrix_vector = np.zeros(M.shape[0])

        for i in range(M.shape[0]):
            result_matrix_vector[i] = inner_product(M[i], v)

        return result_matrix_vector


v = np.array([7, -7])
M = np.array(([2, 0], [17, 17], [2, 14]))

print(matrix_vector(M, v))
