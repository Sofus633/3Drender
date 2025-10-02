from inputs import manage_inp
from settings import win
from pyglet import app, clock, shapes
from settings import batch, batch_list

from vector import Vector3
from point import Point
from camera import Camera
camera1 = Camera(Vector3(1, 0, 0))
point1 = Point(Vector3(10, 10, 1))
batch_list.append(shapes.Circle(*camera1.point_on_plane(point1.position).get(), 5, color=(100, 100,100), batch=batch))
print(camera1.point_on_plane(point1.position).get())

@win.event
def on_draw():
    win.clear()
    batch.draw()



def update(dt):
    manage_inp()


    batch_list.clear()
    pos = camera1.point_on_plane(point1.position).get()
    point1.position.x += 1
    batch_list.append(shapes.Circle(pos[0], pos[1], 5, color=(100, 100,100), batch=batch))
    """display_tree(graph, None)"""

    
clock.schedule_interval(update, 1/60.0)
app.run()