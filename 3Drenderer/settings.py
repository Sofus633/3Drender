from pyglet.window import Window, key
import pyglet

SCREEN_SIZE = [960, 540]
CAMERA_POS = [0, 0, 0]



batch = pyglet.graphics.Batch()
batch_list = []
win = Window(width=SCREEN_SIZE[0], height=SCREEN_SIZE[1])
keys = key.KeyStateHandler()
win.push_handlers(keys)
