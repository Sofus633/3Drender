from settings import SCREEN_SIZE, batch, batch_list, camera
from vector import Vector2
from pyglet import shapes
import random

class Node:
    def __init__(self, value=Vector2(), childs=None):
        if childs == None:
            self.child = [] #list Nodes
        else:
            self.child = childs
        self.value = value #Vector2()
        self.position = None


    def add_child(self, child):
        self.child.append(child)

    def remove_child(self, child):
        self.child.remove(child)

def weight_tree(node, parent=None):
    if parent == None:
        node.position = Vector2(SCREEN_SIZE[0]//2, SCREEN_SIZE [1]//2)
    if parent != None:
        node.position = parent.position + node.value
        #batch_list.append(shapes.Line(*node.position.get(), *parent.position.get(), 1, color=(100, 100,100), batch=batch))
    #batch_list.append(shapes.Circle(node.position.x, node.position.y, 5, color=(100, 100,100), batch=batch))

    if len(node.child) > 0:
        for child in node.child:
            weight_tree(child, node)

def display_tree(node, parent=None ):
    global camera
    node_pos = camera.calculate_pos(node.position)
    if parent != None:
        parent_pos = camera.calculate_pos(parent.position)
        batch_list.append(shapes.Line(*(node_pos).get(), *(parent_pos).get(), 1, color=(100, 100,100), batch=batch))
    batch_list.append(shapes.Circle((node_pos.x), (node_pos.y), 5, color=(100, 100,100), batch=batch))

    if len(node.child) > 0:
        for child in node.child:
            display_tree(child, node)



def random_graph(graph, size=random.randint(0, 10)):
    if size <= 0:
        return  
    for i in range(random.randint(1, 5)):
        newnode = Node(Vector2(random.randint(1, 100), random.randint(1, 100)))
        print(newnode.value.get())
        graph.child.append(newnode)
        random_graph(newnode, size-1)
    weight_tree(graph)


def print_graph(node, depth=0):
    prefix = "│   " * (depth-1) + ("├── " if depth > 0 else "")
    print(f"{prefix}{node.value.get()}")
    for child in node.child:
        print_graph(child, depth+1)

if __name__ == "__main__":
    graph = Node(Vector2(0,0))
    random_graph(graph, 2)
    print_graph(graph, 2)

        
        