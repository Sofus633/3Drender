from settings import keys
from pyglet.window import key

def manage_inp():
    global keys
    if keys[key.Z]:
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
    