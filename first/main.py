from gnode import GNode, walk_graph, paths

if __name__ == '__main__':
    nodeE = GNode("E")
    nodeF = GNode("F")
    nodeG = GNode("G")
    nodeH = GNode("H")
    nodeJ = GNode("J")

    nodeB = GNode("B", [nodeE, nodeF])
    nodeC = GNode("C", [nodeE, nodeG, nodeH])
    nodeD = GNode("D", [nodeJ])
    nodeA = GNode("A", [nodeB, nodeC, nodeD])

    print(nodeA.get_children())
    print(walk_graph(nodeA))
    print(paths(nodeA))
