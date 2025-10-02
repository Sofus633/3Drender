from pyglet.window import Window
from pyglet import app, shapes, clock

from vector import Vector2
from node import Node, random_graph, display_tree
from settings import SCREEN_SIZE, batch, batch_list, camera
from pyglet.window import key


win = Window(width=SCREEN_SIZE[0], height=SCREEN_SIZE[1])
keys = key.KeyStateHandler()
win.push_handlers(keys)
graph = Node(Vector2())
random_graph(graph, 3)
camera.cam_pos = graph.position
display_tree(graph)
#line = shapes.Line(0, 0, 100, 100, 5, (100, 100, 0), batch=batch)
 
@win.event
def on_draw():
    win.clear()
    batch.draw()


def update(dt):
    global camera, graph, win, graph, random_graph
    if  keys[key.Z]:
        print("e")
        camera.position_ofset += Vector2(0,10)
    if keys[key.Q]:
        camera.position_ofset += Vector2(-10,0)
    if keys[key.S]:
        camera.position_ofset += Vector2(0,-10)
    if keys[key.D]:
        camera.position_ofset += Vector2(10,0)
    if keys[key.E]:
        camera.zoom_ofset -= .1
    if keys[key.A]:
        camera.zoom_ofset += .1
    if keys[key.R]:
        graph = Node(Vector2())
        random_graph(graph, 3)


    batch_list.clear()
    display_tree(graph, None)

    
clock.schedule_interval(update, 1/60.0)
app.run()