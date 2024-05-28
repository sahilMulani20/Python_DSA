"""
@Auther : Sahil Mulani
@Date : 11 May 2024
@Description: In this module implemented the insertion sort algorithm on random list element
"""
import sys


def insertion_sort(L):
    # if type(L) != list:
    #     raise TypeError("L must be a list object")
    if len(L) == 0:
        raise ValueError("L must a non-empty")

    for j in range(1, len(L)):
        key = L[j]
        i = j - 1
        while i > -1 and L[i] > key:
            L[i + 1] = L[i]
            i = i - 1
        L[i + 1] = key


def openAndReadFile(filePath: str) -> list:
    list = []
    try:
        f_handle = open(filePath, "r")
        for line in f_handle:
            line = line.strip()
            list.append(int(line))
        f_handle.close()
    except object:
        exc_tb: object
        exc_name, exc_data, exc_tb = sys.exc_info()
        print(exc_name, exc_data)
        sys.exit(-1)

    return list


def writeInTheFile(filePath: str, L):
    try:
        f_handle = open(filePath, "w")

        for x in L:
            print(x, file=f_handle)
        f_handle.close()
    except object:
        exc_name, exc_data, exc_tb = sys.exc_info()
        print(exc_name, exc_data)
        sys.exit(-1)


def main():
    in_file_path = "InputFile.txt"
    op_file_path = "OutputFile.txt"
    L = openAndReadFile(in_file_path)
    insertion_sort(L)
    writeInTheFile(op_file_path, L)

    sys.exit(0)


main()
