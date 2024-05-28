"""
@Auther : Sahil Mulani
@Date : 13th April 2024
@Description : In this module implemented merge_sorting algorithm.
"""

import sys
from typing import List
from random import randint


def generate_random_list(Count: int) -> List[int]:
    """
    :param Count: positive integer -> Number of elements to generate
    :return: list of random numbers
    """

    if type(Count) != int:
        raise TypeError(" Count must be Integer value.")
    if Count <= 0:
        raise ValueError(" Count must be greater then zero.")

    ranList = []

    Start = 0
    end = Count

    for i in range(0, Count):
        ranList.append(randint(Start, end))

    return ranList


def display_List(intList: List[int], message: str) -> None:
    """
    :param intList: List of Integers
    :param message: Header message
    :return: None
    """
    print(message)

    for i in range(0, len(intList)):
        print(f'List[{i}] : {intList[i]}')


def merge(intList: List[int], p: int, q: int, r: int) -> None:
    """
    This method perform the merge procedure to merge two sorted list.
    :param intList: list of integers
    :param p: Start index in list
    :param q: Middle index in list
    :param r: End index in list
    :return: None
    """
    N1 = q - p + 1  # length of L[p...q]
    N2 = r - q      # length of L[q+1...r]
    # Build sub-list 1
    # L1[0....N1-1] = L[p....q]
    temp1 = []
    i = 0
    while i < N1:
        temp1.append(intList[p + i])
        i = i + 1

    # Build sub-list 2
    # L2[0....N2-1] = L[q+1....r]
    temp2 = []
    i = 0
    while i < N2:
        temp2.append(intList[q + 1 + i])
        i = i + 1
    i = 0
    j = 0
    k = p

    while True:
        if temp1[i] <= temp2[j]:
            intList[k] = temp1[i]
            i = i+1
            k = k+1

            if i == len(temp1):
                while True:
                    intList[k] = temp2[j]
                    k = k+1
                    j = j+1
                    if j == len(temp2):
                        break
                break
        else:
            intList[k] = temp2[j]
            j = j+1
            k = k+1

            if j == len(temp2):

                while True:
                    intList[k] = temp1[i]
                    k = k+1
                    i = i+1
                    if i == len(temp1):
                        break
                break


def merge_sort(intList: List[int], p: int, r: int) -> None:
    """
    This method perform merge sort algorithm through recursive function call
    :param intList: List of Integers
    :param p: Start position
    :param r: End position
    :return: None
    """

    if p < r:
        q = (p+r)//2
        merge_sort(intList, p, q)
        merge_sort(intList, q+1, r)
        merge(intList, p, q, r)


def main():

    Count = int(input(" Enter the size of list (Greater then 2) :- "))
    if Count < 2:
        raise ValueError(" List Size Should Be Greater Then 2...")

    intList = generate_random_list(Count)

    display_List(intList, "Before merge sort list...")
    merge_sort(intList, 0, Count-1)
    display_List(intList, "After merge sort list...")

    sys.exit(0)


main()
