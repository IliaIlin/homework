class GNode:
    def __init__(self, name, children=None):
        self.__name = name
        self.__children = children if children is not None else []

    def get_name(self):
        return self.__name

    def get_children(self):
        return self.__children

    def __eq__(self, other):
        if isinstance(other, GNode):
            return self.__name == other.__name and self.__children == other.__children
        else:
            return False

    def __hash__(self):
        return hash((self.__name, tuple(self.__children)))

    def __repr__(self):
        return f"{self.__name}"


def walk_graph(node: GNode):
    visited_nodes = {node}
    for child in node.get_children():
        visited_nodes.update(walk_graph(child))
    return visited_nodes


def paths(node: GNode):
    all_paths = []
    if node.get_children():
        for child in node.get_children():
            for child_path in paths(child):
                all_paths.append([node] + child_path)
    else:
        all_paths.append([node])
    return all_paths
