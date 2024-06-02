import matplotlib.pyplot as plt
import networkx as nx
import uuid
import queue

class Node:
    def __init__(self, key, color="#FFFFFF"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def dfs(root):
    stack = [root]
    color = "#101001"
    while stack:
        node = stack.pop()
        if node:
            node.color = color
            color = "#%06x" % (int(color[1:], 16) + 0x202020)
            print('after', color)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

def bfs(root):
    color = "#101001"
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        node = q.get()
        if node:
            node.color = color
            color = "#%06x" % (int(color[1:], 16) + 0x202020)

            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)

def draw_tree(root, traversal="dfs"):
    if traversal == "dfs":
        dfs(root)
    else:
        bfs(root)

    tree = nx.DiGraph()
    pos = {root.id: (0, 0)}
    tree = add_edges(tree, root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}
    print(labels)
    print(colors)

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

# Test
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# draw_tree(root, "dfs")
draw_tree(root, "bfs")
