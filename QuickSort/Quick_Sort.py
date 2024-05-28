"""
@Auther :- Sahil Mulani
@Date :- 16 May 2024
@Description :- In this class implemented the quick sort algorithm using partition procedure.
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


def partitionProcedure(L: List[int], p: int, r: int) -> int:
    """
    This method performs partition procedure algorithm
    @precondition :
        1) 0 <= p < r < len(L)
    @post condition :
        1) Element at L[r] should be moved to index q
           between [p, r] and rest of the elements
           should be re-arrange (permuted) such that

           i) all elements from L[p...q-1] are less than
              or equal to L[q]
           ii) all element from L[q+1...r] are greater than
              L[q]
    @input :
    :param L: List of Integer
    :param p: Start index from list
    :param r: End index from list
    :return: index of pivot element
    """

    i = p - 1  # Compare and Swap element index
    j = p  # Start Index for iteration
    pivot = L[r]  # List element set as a pivot element

    # Check j is less than r
    while j < r:

        # Compare L[j] is less than or equal to pivot
        if L[j] <= pivot:
            i = i + 1  # Increase the i to 1
            L[i], L[j] = L[j], L[i]  # Swap element L[i] <-> L[j]

        j = j + 1  # Increase the j = 1

    L[i + 1], L[r] = L[r], L[i + 1]  # Swap pivot element

    # Return the pivot element index
    return i + 1


def Quick_Sort(L: List[int], p: int, r: int) -> None:
    """
    @precondition :-
        0 <= p < r < len(L)
    @Output :- List of integer while be sorted using quick sort
    :param L: List of Integer
    :param p: Start index from List
    :param r: End Index from List
    :return: None
    """
    if p < r:
        pivotIndex = partitionProcedure(L, p, r)

        Quick_Sort(L, p, pivotIndex - 1)
        Quick_Sort(L, pivotIndex + 1, r)


def main():

    Count = int(input(" Enter the size of list (Greater then 2) :- "))
    if Count < 2:
        raise ValueError(" List Size Should Be Greater Then 2...")

    intList = generate_random_list(Count)

    display_List(intList, "Before Quick sort list...")
    Quick_Sort(intList, 0, Count-1)
    display_List(intList, "After Quick sort list...")

    sys.exit(0)


main()
