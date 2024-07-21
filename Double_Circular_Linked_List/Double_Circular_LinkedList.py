"""
Author :- Sahil Mulani
Date :- 20-July-2024
Description :- Implemented a double circular linked list with 20 algorithms
"""
import random
import sys

from typing import List


def NodeDataIsInValid(Exception):
    pass


def ValueErrorException(Exception):
    pass


def generateRanElements(start: int, end: int) -> List[int]:
    elemList = []
    for i in range(start, end):
        elemList.append(random.randint(1, end))

    return elemList


class dNode:
    def __init__(self, Data):
        self.Data = Data
        self.Prev = None
        self.Next = None


class doubleCirList:

    def __init__(self):
        self.headDNode = dNode(None)

    def insertEnd(self, Data) -> None:
        """
        This function insert node at end of the doubly circular linked list and connected in circular list
        :param Data: Data to be inserted at the end of list
        :return: None
        """

        if Data is None:
            raise NodeDataIsInValid(f"Data should not be {Data}")

        run = self.headDNode

        node = dNode(Data)

        # For First Element Add
        if run.Next is None:
            node.Next = run
            run.Prev = node

            node.Prev = run
            run.Next = node
        else:
            # Iterate elements to the last node
            while run is not self.headDNode.Prev:
                run = run.Next

            node.Next = run.Next
            node.Prev = run

            run.Next = node
            self.headDNode.Prev = node

    def insertStart(self, Data) -> None:
        """
        This function inserted element at start of the double circular linked list  and connected in circular list
        :param Data: Data to be inserted at start of list
        :return: None
        """

        if Data is None:
            raise NodeDataIsInValid(f"Data should not be {Data}")

        node = dNode(Data)
        run = self.headDNode
        node.Next = run.Next
        node.Prev = run
        run.Next = node

    def insertAfterElement(self, Data, Element) -> None:
        """
        This function inserted element after given Element of the double circular linked list and connected in
        circular list
        :param Data: Data to be inserted after element or inbetween the list
        :param Element: Element were data to be inserted after
        :return: None
        """

        if Data is None:
            raise NodeDataIsInValid(f"Data should not be {Data}")
        if Element is None:
            raise NodeDataIsInValid(f"Data should not be {Data}")

        run = self.headDNode

        while run.Next is not self.headDNode.Prev:

            run = run.Next

            if run.Data is Element:
                break
        else:
            raise ValueErrorException(f"Element not present in double circular linked list")

        node = dNode(Data)
        node.Next = run.Next
        node.Prev = run
        run.Next = node

    def insertBeforeElement(self, Data, Element) -> None:
        """
        This function inserted element before given Element of the double circular linked list and
        :param Data: Data to be inserted before element or inbetween the list
        :param Element: Element were data to be inserted before
        :return: None
        """
        if Data is None:
            raise NodeDataIsInValid(f"Data should not be {Data}")
        if Element is None:
            raise NodeDataIsInValid(f"Data should not be {Element}")

        run = self.headDNode

        while run is not self.headDNode.Prev:

            run = run.Next
            if run.Data is Element:
                break
        else:
            raise ValueErrorException(f"Element :- {Element} not present in double circular linked list")

        node = dNode(Data)

        # Linked new node between the two links
        node.Next = run
        node.Prev = run.Prev

        # Remove Existing links and connect new nodes
        run.Prev.Next = node
        run.Prev = node

    def deleteFirst(self) -> None:
        """
        This function deleted elements from start
        :return: None
        """
        if self.headDNode.Next is self.headDNode:
            raise ValueErrorException("Double Circular Linked List Is Empty")

        self.headDNode.Next = self.headDNode.Next.Next
        self.headDNode.Next.Prev = self.headDNode

    def deleteLast(self) -> None:
        """
        This function deleted element from start
        :return: None
        """

        if self.headDNode.Next is self.headDNode:
            raise ValueErrorException("Double Circular Linked List Is Empty")

        print("Deleted Last Element :- " + str(self.headDNode.Prev.Data))
        self.headDNode.Prev = self.headDNode.Prev.Prev
        self.headDNode.Prev.Next = self.headDNode

    def deleteSpecificElement(self, Element) -> None:
        """
        This function will delete the specific element from double circular linked list
        :param Element: Element to be deleted
        :return: None
        """

        if Element is None:
            raise ValueErrorException(f"Element should not be {Element}")

        print("Deleted Specific Element :- " + str(Element))
        run = self.headDNode

        while run is not self.headDNode.Prev:
            run = run.Next
            if Element is run.Data:
                break
        else:
            raise ValueErrorException(f"Element :- {Element} not present in the double circular list")

        # Shuffle run Prev and Next With Before and After Node
        run.Prev.Next, run.Next.Prev = run.Next, run.Prev

        run.Next = None
        run.Prev = None

    def showDoubleCircularList(self, message: str) -> None:
        """
        This method show the list of element
        :return: None
        """
        # Display message
        print(" *** " + message + " *** ")

        run = self.headDNode
        print("START ->", end='')
        while run is not self.headDNode.Prev:
            print(f" [{run.Data}] -> ", end='')
            run = run.Next
        print(f" [{run.Data}] -> ", end='')
        print("End")
        # print(run)

    def __len__(self) -> int:
        """
        This function calculate the number of elements are present in the double circular linked list
        :return: Integer of total count
        """
        count = 0
        run = self.headDNode.Next

        while run is not self.headDNode:
            count += 1
            run = run.Next

        return count

    # def __str__(self, DoubleCirList:
    #     """
    #     This function override the In-Built print function
    #     :return: Double Circular Linked List in formated string
    #     """
    #     return self


def main():
    # Generate Random Element List

    # elemList = generateRanElements(0, 20)
    elemList = [
        100, 20, 30, 288, 514,
        400, 562, 677, 819, 22,
        21, 22, 323, 667
    ]

    # Create head Node
    D = doubleCirList()

    # Iterate Elements
    for element in elemList:
        # Insert Element
        D.insertEnd(element)

    # print(str(D.headDNode.Prev) + " | " + str(D.headDNode.Data) + " | " + str(D.headDNode.Next))
    # print(str(D.headDNode.Prev.Prev) + " | " + str(D.headDNode.Prev.Data) + " | " + str(D.headDNode.Prev.Next))
    # Display Double Circular Linked List
    D.showDoubleCircularList("Insert At End")

    D.insertStart(700)
    D.insertStart(786)

    # Display Double Circular Linked List
    D.showDoubleCircularList("Insert At Start")

    D.insertEnd(1980)

    # Display Double Circular Linked List
    D.showDoubleCircularList("Insert At End")

    D.insertAfterElement(202, 786)
    D.insertAfterElement(3, 400)

    D.showDoubleCircularList("Insert After Element")

    D.insertBeforeElement(3033, 786)
    D.insertBeforeElement(3033, 1980)

    # Display Double Circular Linked List
    D.showDoubleCircularList("Insert Before Element")

    D.deleteFirst()
    D.deleteFirst()

    # Display Double Circular Linked List
    D.showDoubleCircularList("Deleted First Element")

    D.deleteLast()
    D.deleteLast()

    # Display Double Circular Linked List
    D.showDoubleCircularList("Deleted Last Element")

    D.deleteSpecificElement(20)
    D.deleteSpecificElement(667)
    D.deleteSpecificElement(202)

    # Display Double Circular Linked List
    D.showDoubleCircularList("Deleted Specific Element")

    print("Total count of element :- " + str(len(D)))
    sys.exit(0)


main()
