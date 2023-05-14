import numpy as np

"""
Maak een functie die het inwendig product van een twee vectoren geeft.
Net als bij het optellen moet Python een DimensionError geven als de vectoren
niet hetzelfde formaat hebben.
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


print(inner_product(np.array([12, -5]), np.array([12, -5])))
