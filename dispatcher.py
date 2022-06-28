from dispatcher_base import DispatcherBase
from plane import Plane


class PlaneNode:
    def __init__(self, plane):
      self.plane = plane
      self.next = None
      self.prev = None


class PriorityQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        
        
    def insert_plane(self, plane):
        new = PlaneNode(plane)
        if self.head is None:
            self.head = new
            self.tail = new
        elif (plane < self.head.plane):
            new.next = self.head
            self.head.prev = new
            self.head = new
        elif (self.tail.plane < plane):
            new.prev = self.tail
            self.tail.next = new
            self.tail = new
        else:
            n = self.head
            while n is not None:
                if n.plane > plane:
                    new.next = n
                    new.prev = n.prev
                    n.prev.next = new
                    n.prev = new
                    break
                n = n.next

    def size(self):
        if self.head is None:
            return 0
        else:
            k = 0 
            node = self.head
            while node is not None:
                k = k + 1
                node = node.next
            return k
                
                
    def remove_min(self):
        if self.head is None:
            return None
        removed = self.head
        if self.head.next is None:
            self.head = None
            return removed
        self.head = self.head.next
        self.head.prev = None;
        return removed
    
    def min(self):
        if self.head is None:
            return None
        return self.head
    
    def remove_plane(self, plane_number):
        if self.head is None:
            return None
        if self.head.next is None and self.head.plane.plane_number == plane_number:
            self.head = None
            self.tail = None
            return plane_number
        if self.head.plane.plane_number == plane_number:
            self.head = self.head.next
            self.head.prev = None
            return plane_number
        if self.tail.plane.plane_number == plane_number:
            self.tail = self.tail.prev
            self.tail.next = None
            return plane_number
        else:
            n = self.head
            while n is not None:
                if n.plane.plane_number == plane_number:
                    n.prev.next = n.next
                    n.next.prev = n.prev
                    return plane_number
                n = n.next
            return None
                
            
            
            
    def is_present(self, plane_number):
        n = self.head
        while n is not None:
            if n.plane.plane_number == plane_number:
                return True
            n = n.next
        return False
        
        
        
          

class Dispatcher(DispatcherBase):
    """
        Implement all the necessary methods here
        
    """
    def __init__(self):
        self.planeQueue = PriorityQueue()

    def __len__(self):
        return self.planeQueue.size()

    def add_plane(self, plane_number: str, time: str):
        plane = Plane(plane_number, time)
        self.planeQueue.insert_plane(plane)

    def allocate_landing_slot(self, current_time: str):
        min_node = self.planeQueue.min()
        if min_node is None:
            return None
        next_plane = min_node.plane
        hours = int(next_plane.time[0:2])
        mins = int(next_plane.time[3:5])
        landing_mins = 60 * hours + mins
        hours = int(current_time[0:2])
        mins = int(current_time[3:5])
        current_mins = 60 * hours + mins
        if (current_mins + 5 >= landing_mins):
            return self.planeQueue.remove_min().plane.plane_number
        return None

    def emergency_landing(self, plane_number: str):
        return self.planeQueue.remove_plane(plane_number)
        

    def is_present(self, plane_number: str):
        return self.planeQueue.is_present(plane_number)


