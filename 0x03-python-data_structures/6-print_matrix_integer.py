#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix[0]:
        for i in matrix:
            for j in i:
                print(f"{j:d}", end=("\n" if j == i[-1] else " "))
    else:
        print("")
