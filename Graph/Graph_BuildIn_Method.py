"""
@Auther : Sahil Mulani
@Date : 2 june 2024
@Description : In this implemented graph data structure using built in method
"""
import sys
from sys import exc_info
from traceback import print_tb


def generic_exception_handler(want_tb=False):
    exc_name, exc_data, exc_tb = exc_info()
    print(exc_name.__name__, exc_data, sep=":")
    if want_tb:
        print_tb(exc_tb)


class VertexInvalidError(Exception):
    pass


class VertexExistsError(Exception):
    pass


class EdgeInvalidError(Exception):
    pass


class EdgeExistsError(Exception):
    pass


class Graph:
    def __init__(self):
        self.dictionary = {}
        self.no_of_edges = 0

    def add_vertex(self, v: int) -> None:
        """
        Vertex exists -> Exception Throw
        :param v: vertex from graph
        :return: None
        """
        if v in self.dictionary.keys():
            raise VertexInvalidError(f'{v} Vertex already exists')

        self.dictionary[v] = []

    def remove_vertex(self, v: int) -> None:
        """
        Remove Vertex from graph
        :param v: Vertex from graph
        :return: None
        """

        if v not in self.dictionary.keys():
            raise VertexInvalidError(f'{v} Not found in the graph')

        for v_adj in self.dictionary[v]:
            self.dictionary[v_adj].remove(v)

        self.no_of_edges = len(self.dictionary)
        del self.dictionary[v]

    def add_edge(self, v_start: int, v_end: int) -> None:
        """
        v_start or v_end or both may be invalid -> exception
        v_start and v_end are valid and edge already exists between them edge_exists
        :param v_start: staring vertex from graph
        :param v_end: ending vertex from graph
        :return None:
        """
        if v_start not in self.dictionary.keys():
            raise VertexInvalidError(f'{v_start} Vertex not present in the graph')
        if v_end not in self.dictionary.keys():
            raise VertexInvalidError(f'{v_end} Vertex not present in the graph')

        if v_start in self.dictionary[v_end] and v_end in self.dictionary[v_start]:
            raise EdgeInvalidError(f'{v_start} is already present in v_end and {v_end} is already present in v_start')

        self.dictionary[v_start].append(v_end)
        self.dictionary[v_end].append(v_start)
        self.no_of_edges += 1

    def remove_edge(self, v_start: int, v_end: int) -> None:
        """
        v_start, v_end or both may be invalid
        v_start, v_end are valid but there is No Edge between the two
        :param v_start: Staring vertex from graph
        :param v_end: Ending vertex from graph
        :return: None
        """
        if v_start not in self.dictionary.keys():
            raise VertexInvalidError(f'{v_start} vertex not found in the graph')
        if v_end not in self.dictionary.keys():
            raise VertexInvalidError(f'{v_end} vertex not found in the graph')

        if not v_start in self.dictionary[v_end] or not v_end in self.dictionary[v_start]:
            raise EdgeExistsError(f'edge ({v_start, v_end}) not found in the graph')

        self.dictionary[v_start].remove(v_end)
        self.dictionary[v_end].remove(v_start)
        self.no_of_edges -= 1

    def __len__(self) -> int:
        """
        This method replace the builtin len method with this class len function
        :return: count of the present vertex in the graph
        """

        return len(self.dictionary)

    def __str__(self) -> str:
        """
        Display graph
        :return str: Return all the Graph in String
        """
        all_vartex = self.dictionary.keys()
        op_String = "\n"
        for vertex in all_vartex:
            op_String += f'[{vertex}] = '
            for edge in self.dictionary[vertex]:
                op_String += f'[{edge}]-'

            op_String += "[End]\n"

        return op_String


def main():

    # Create Graph
    print("Implementation of graph started : ")
    g = Graph()
    for i in range(1, 7):
        g.add_vertex(i)

    print("After insert vertex : ", g)
    print("Count of vertex : ", len(g))
    print("Count of edges : ", g.no_of_edges)

    # Add edges
    edges = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 1), (6, 2), (6, 3), (2, 5), (5, 3)]
    for i in edges:
        g.add_edge(i[0], i[1])

    print("After insert edges : ", g)
    print("Count of edges : ", g.no_of_edges)

    # Remove vertex from graph
    g.remove_vertex(6)
    print("After remove vertex 6 : ", g)
    print("Count of edges : ", g.no_of_edges)

    # Remove edge from graph
    g.remove_edge(1, 2)
    print("After remove edge (1,2)", g)
    print("Count of edges :- ", g.no_of_edges)

    print("Implementation of graph ended : ")
    sys.exit(0)


main()

"""
Output section :

Implementation of graph started : 
After insert vertex :  
[1] = [End]
[2] = [End]
[3] = [End]
[4] = [End]
[5] = [End]
[6] = [End]

Count of vertex :  6
Count of edges :  0
After insert edges :  
[1] = [2]-[6]-[End]
[2] = [1]-[3]-[6]-[5]-[End]
[3] = [2]-[4]-[6]-[5]-[End]
[4] = [3]-[5]-[End]
[5] = [4]-[6]-[2]-[3]-[End]
[6] = [5]-[1]-[2]-[3]-[End]

Count of edges :  10
After remove vertex 6 :  
[1] = [2]-[End]
[2] = [1]-[3]-[5]-[End]
[3] = [2]-[4]-[5]-[End]
[4] = [3]-[5]-[End]
[5] = [4]-[2]-[3]-[End]

Count of edges :  6
After remove edge (1,2) 
[1] = [End]
[2] = [3]-[5]-[End]
[3] = [2]-[4]-[5]-[End]
[4] = [3]-[5]-[End]
[5] = [4]-[2]-[3]-[End]

Count of edges :-  5
Implementation of graph ended : 

"""