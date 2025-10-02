from vector import Vector2

class Camera:
    def __init__(self, zoom_ofset=None, position_ofset=None, cam_pos=None):
        if cam_pos == None:
            self.cam_pos = Vector2()
        else:
            self.cam_pos = cam_pos
        if zoom_ofset == None:
            self.zoom_ofset = 1
        if zoom_ofset == None:
            self.position_ofset = Vector2()

    def calculate_pos(self, pos):
        print(pos, self.cam_pos)
        return((( pos - self.cam_pos)* self.zoom_ofset)+self.position_ofset )
        