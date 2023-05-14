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

#
# v = np.array([7, -7])
# M = np.array(([2, 0], [17, 17], [2, 14]))
#
# print(matrix_vector(M, v))

def matrix_product(M: np.ndarray, N: np.ndarray) -> np.ndarray:
    """
    Function returns matrix-matrix multiplication.
    A matrix and a vector multiplication is also possible.
    Example;
    :param M: np.ndarray, np.array(([6, 5, 4], [9, 8, 7]))
    :param N: np.ndarray, np.array(([4, 0], [4, 5], [8, 3]))
    :return: result_matrix_product: np.ndarray,
    """
    if M.shape[1] != N.shape[0]:
        raise DimensionError("Vectors niet hetzelfde formaat")

    elif M.shape[1] == N.shape[0]:
        if len(N.shape) == 1:
            return matrix_vector(M, N)

        elif len(N.shape) > 1:
            result_matrix_product = np.zeros((M.shape[0], N.shape[1]))
            for i in range(N.shape[1]):
                tijdelijk = N[:, i]
                a = matrix_vector(M, tijdelijk)
                for x in range(M.shape[0]):
                    result_matrix_product[x][i] = a[x]
            return result_matrix_product


# m = np.array(([6, 5, 4], [9, 8, 7]))
# n = np.array(([4, 0], [4, 5], [8, 3]))
#
#
# print(matrix_product(m, n))
#
# np.array(([76.,  37.], [124.,  61.]))

import json


def read_network(filename: str) -> np.ndarray:
    """
    Function reads the layers from the JSON file, and creates matrices for the different layers.
    If this is more than 1, the layers are multiplied with each other.
    :param filename: str, given JSON-file
    :return: result: np.ndarray, A matrix of multiplied matrices
    """
    # Network file
    f_network = open(filename, "r")
    data = json.loads(f_network.read())

    for layer in data:

        size_in = int(data[layer]["size_in"])
        size_out = int(data[layer]["size_out"])

        matrix = np.zeros((size_in, size_out))

        for index, column in enumerate(data[layer]["weights"]):

            for i in range(size_out):
                if str(i + 1) not in data[layer]["weights"][column]:
                    data[layer]["weights"][column][str(i + 1)] = 0

                matrix[index, i] = data[layer]["weights"][column][str(i + 1)]

        data[layer]["matrix"] = matrix.T

    # Set correct the correct size for output array
    last_layer = list(data.keys())[-1]
    result = data[last_layer]["matrix"]

    layer_list = list(data.keys())
    layer_list_reversed = layer_list[::-1]

    if len(layer_list_reversed) > 1:
        layer_list_reversed.pop(0)

        for i in range(len(layer_list_reversed)):
            next_layer_matrix = data[layer_list_reversed[i]]["matrix"]
            result = matrix_product(result, next_layer_matrix)

    return result


def run_network(filename: str, input_vector: np.ndarray) -> np.ndarray:
    """
    Function uses read_network() and matrix_vector(),
    to apply the JSON file to the given input_vector.
    :param filename: str, given JSON-file
    :param input_vector: np.ndarray, given Vector
    :return: result: np.ndarray, JSON-file matrices multiplied * given Vector
    """
    file_matrix = read_network(filename)

    result = matrix_vector(file_matrix, input_vector)

    return result
