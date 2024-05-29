"""
@Auther : Sahil Mulani
@Date : 29-May-2024
@Description : Implemented Singly Linked List including all function and test
"""
import sys


# Create Node class with data and next class members
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Create Singly Linked List class for implemented all list method
class SinglyLinkedList:
    def __init__(self):
        self.headNode = Node(None)

    def insert_end(self, new_data):
        run = self.headNode
        while run.next is not None:
            run = run.next

        new_node = Node(new_data)
        new_node.next = run.next
        run.next = new_node

    def insert_start(self, new_data):
        run = self.headNode
        new_node = Node(new_data)
        new_node.next = run.next
        self.headNode.next = new_node

    def pop_end(self):

        run = self.headNode
        while run.next.next is not None:
            run = run.next

        run.next = None

    def pop_start(self):

        run = self.headNode
        self.headNode = run.next

    def insert_before(self, new_data, existing_data):

        run = self.headNode

        while run.data is not existing_data:
            run = run.next

        previous = self.headNode

        while previous.next is not run:
            previous = previous.next

        new_node = Node(new_data)
        previous.next = new_node

        new_node.next = run

    def showList(self, msg):

            if type(msg) != str:
                raise TypeError("Message must be string")
            else:
                print(msg)

            print("[Start] ->", end="")
            run = self.headNode.next
            while run is not None:
                print("[" + str(run.data) + "] ->", end="")
                run = run.next

            print("[End]")


def main():
    L = SinglyLinkedList()
    L.insert_end(10)
    L.insert_end(20)
    L.insert_end(30)

    L.showList("Show After insert_end()")

    L.insert_start(100)
    L.insert_start(200)
    L.insert_start(200)
    L.showList("Show After insert_start()")

    L.pop_end()
    L.showList("Show after pop_end()")

    L.pop_end()
    L.showList("Show after pop_end()")

    L.pop_start()
    L.showList("Show after pop_start()")

    L.insert_before(456, 100)
    L.showList("Show after insert_before()")
    sys.exit(0)


main()
