from plane_base import PlaneBase


class Plane(PlaneBase): 
    def __lt__(self, other):
        if self.time < other.time:
            return True
        elif self.time == other.time and self.plane_number < other.plane_number:
            return True
        return False
    
    