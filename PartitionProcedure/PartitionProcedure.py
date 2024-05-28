"""
@Auther :- Sahil Mulani
@Date :- 14 April 2024
@Description :- In this class implemented the partition procedure which is a main helper procedure in the quick sort
                algorithm.
"""


from typing import List


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

    i = p - 1     # Compare and Swap element index
    j = p         # Start Index for iteration
    pivot = L[r]  # List element set as a pivot element

    # Check j is less than r
    while j < r:

        # Compare L[j] is less than or equal to pivot
        if L[j] <= pivot:
            i = i + 1                  # Increase the i to 1
            L[i], L[j] = L[j], L[i]    # Swap element L[i] <-> L[j]

        j = j + 1                      # Increase the j = 1

    L[i + 1], L[r] = L[r], L[i + 1]    # Swap pivot element

    # Return the pivot element index
    return i + 1


def main():
    listInt = [
        10, 20, 33,
        55, 68, 77, 1, 8, 99, 45, 50, 60, 44, 32, 20, 55, 80, 51,
        110, 113, 442, 510, 39
    ]

    print("Before partition procedure : ", listInt)

    pivotIndex = partitionProcedure(listInt, listInt.index(55), listInt.index(51))

    print("After partition procedure : ", listInt)

    print("Pivot element index :- ", pivotIndex)


main()
