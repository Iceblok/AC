import numpy as np

"""
Maak een functie die het inwendig product van een twee vectoren geeft.
Net als bij het optellen moet Python een DimensionError geven als de vectoren
niet hetzelfde formaat hebben.
"""


class DimensionError(Exception):
    pass


def inner_product(u: np.ndarray, v: np.ndarray) -> np.ndarray:
    if len(u) != len(v):
        raise DimensionError("Vectors niet hetzelfde formaat")
    if 0 not in zip(u, v):
        innerproduct = np.zeros(1)
        for i, item in enumerate(v):
            innerproduct += u[i] * v[i]
        return innerproduct
    else:
        innerproduct = u.copy()
        for i, item in enumerate(v):
            innerproduct[i] = u[i] * v[i]
        return innerproduct


print(inner_product([12, -5], [12, -5]))
