__author__ = 'dick'
__email__ = 'ralbayaty@gmail.com'


class Node(object):
    def __init__(self, value, children=[]):
        self.value = value
        self.children = []
        for val in children:
            self.children.append(val)

    def __repr__(self, level=0):
        ret = "\t"*level+repr(self.value)+"\n"
        for child in self.children:
            ret += child.__repr__(level+1)
        return ret


def dfs(graph):
    """
    Depth First Search that will re-visit nodes it has already expanded.
    :param graph: the tree structured graph of the nodes
    :return: the list of visited nodes
    """
    visited = [graph.value]
    stack = []
    for val in graph.children:
        stack.append(val)
    while stack:
        node = stack[0]
        stack = stack[1:]
        # print(visited)
        visited.append(node.value)
        vals = []
        for val in node.children:
            vals.append(val)
        stack = vals + stack
    return visited


def bfs(graph):
    """
    Breadth First Search that will re-visit nodes it has already expanded.
    :param graph: the tree structured graph of the nodes
    :return: the list of visited nodes
    """
    visited = [graph.value]
    stack = []
    for val in graph.children:
        stack.append(val)
    while stack:
        node = stack[0]
        stack = stack[1:]
        # print(visited)
        visited.append(node.value)
        for val in node.children:
            stack = stack + [val]
    return visited


def dfs2(graph):
    """
    Depth First Search that won't re-visit nodes it has already expanded.
    :param graph: the tree structured graph of the nodes
    :return: the list of visited nodes
    """
    visited = [graph.value]
    stack = []
    for val in graph.children:
        stack.append(val)
    while stack:
        node = stack[0]
        stack = stack[1:]
        # print(visited)
        if node.value not in visited:
            visited.append(node.value)
            vals = []
            for val in node.children:
                vals.append(val)
            stack = vals + stack
    return visited


def bfs2(graph):
    """
    Breadth First Search that won't re-visit nodes it has already expanded.
    :param graph: the tree structured graph of the nodes
    :return: the list of visited nodes
    """
    visited = [graph.value]
    stack = []
    for val in graph.children:
        stack.append(val)
    while stack:
        node = stack[0]
        stack = stack[1:]
        # print(visited)
        if node.value not in visited:
            visited.append(node.value)
            for val in node.children:
                stack = stack + [val]
    return visited


if __name__ == "__main__":

    tree = Node("A", [Node("B", [Node("D"), Node("E", [Node("H")])]),
                      Node("C", [Node("F"), Node("G")])])

    tree2 = Node("A", [Node("B", [Node("D", [Node("H"), Node("B"), Node("C", [Node("F"), Node("G")])]),
                                  Node("E")]), Node("C", [Node("F"), Node("G")])])

    print(tree)
    print("Depth First Search:", dfs(tree))
    print("Breadth First Search:", bfs(tree))
    print("Depth First Search:", dfs2(tree))
    print("Breadth First Search:", bfs2(tree))

    print(tree2)
    print("Depth First Search:", dfs(tree2))
    print("Breadth First Search:", bfs(tree2))
    print("Depth First Search:", dfs2(tree2))
    print("Breadth First Search:", bfs2(tree2))


