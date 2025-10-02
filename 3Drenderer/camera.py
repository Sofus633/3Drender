from vector import Vector3

class Camera:
    def __init__(self, zoom_ofset=1, position_ofset=None, cam_pos=None, n_vector=None):
        self.zoom_ofset = zoom_ofset
        if position_ofset == None:
            self.position_ofset = Vector3()
        if cam_pos == None:
                self.cam_pos = Vector3()
        if n_vector == None:
            self.n_vector = Vector3(1, 0, 0)

    def calculate_pos(self, pos):
        return((( pos - self.cam_pos)* self.zoom_ofset)+self.position_ofset )
    
    import numpy as np

    def point_on_plane(self, pos):
        a, b, c =  (self.n_vector).get()
        d = pos.dot()
        if a == b == c == 0:
            raise ValueError("Normal vector cannot be zero")
        
        if c != 0:
            return Vector3(0, 0, d/c)
        elif b != 0:
            return Vector3(0, d/b, 0)
        else:
            return Vector3(d/a, 0, 0)
        