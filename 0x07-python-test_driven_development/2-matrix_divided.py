#!/usr/bin/python3
""" matrix divided """


def matrix_divided(matrix, div):
    """
    divide all elements of a matrix. 
    Must be ints or floats, otherwise raise TypeError
    Each row must be same size or raise TypeError
    Must be divided by a number or raise TypeError
    Cannot divide by 0 or raise ZeroDivisionError
    Returns new matrix
    """
    result[]
    len = 0

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if matrix == [] or matrix == [[]]:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(matrix[0], list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if len(matrix[0]) <= 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        new_row = []
    if type(row) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    