import numpy as np


def check_matrix(f):
    count = 0

    def _check_matrix(n_row, n_col):
        nonlocal count
        matrix = f(n_row, n_col)

        for i in matrix:
            for j in i:
                if j != 0:
                    count += 1
        if count < matrix.size / 10:  # matrix.size - кількість елементів матриці
            # print(np.shape(matrix))
            return {(pos, j): v for pos, i in enumerate(matrix) for j, v in enumerate(i) if v != 0}

        else:
            return matrix
    return _check_matrix


@check_matrix
# генерує матрицю з рандомним вибором значень 0 чи 1, розміром n_row x n_col, з вірогідністю 90% 0, 10% 1
def function(n_row, n_col):
    return np.random.choice([0, 1], size=(n_row, n_col), p=[.9, .1])


@check_matrix
def add_matrix(n_row, n_col):  # m, n - matrix
    m = np.random.choice([0, 1], size=(n_row, n_col), p=[.9, .1])
    print(f"Matrix m:\n{m}")
    n = np.random.choice([0, 1], size=(n_row, n_col), p=[.9, .1])
    print(f"Matrix n:\n{n}")
    return m + n


if __name__ == "__main__":
    print(function(5, 5))
    print(function(5, 5))
    print(add_matrix(5, 5))




