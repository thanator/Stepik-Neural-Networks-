"""
Массив, который нужно было создать в предыдущей задаче, хранится в переменной mat.
 Превратите его в вертикальный вектор и напечатайте.
"""

import numpy as np
mat = np.ndarray(shape=(3, 4), buffer  = 2 * np.eye(3, 4, 0) + np.eye(3, 4, 1))

print(mat.reshape(12, 1))