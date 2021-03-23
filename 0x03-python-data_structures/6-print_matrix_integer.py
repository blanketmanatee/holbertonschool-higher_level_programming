#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for r in range(len(matrix)):
        c = -1
        for c in range(len(matrix[r]) - 1):
            print("{:d} ".format(matrix[r][c]), end="")
        print("{:d}".format(matrix[r][c + 1]))
