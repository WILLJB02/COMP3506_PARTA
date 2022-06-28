from display_base import DisplayRandomBase, DisplayPartiallySortedBase


class DisplayRandom(DisplayRandomBase):
    """
        Implement all the necessary methods here
    """
    
    def merge_array(self, l, r):
        array = [None] * (len(l) + len(r))
        i = j = k = 0
        while i < len(l) and j < len(r):
                if l[i] < r[j]:
                    array[k] = l[i]
                    i += 1
                else:
                    array[k] = r[j]
                    j += 1
                k += 1
        while i < len(l):
            array[k] = l[i]
            i += 1
            k += 1
        while j < len(r):
            array[k] = r[j]
            j += 1
            k += 1
        return array
        
    
    def sort_array(self, array):
        if len(array) > 1:
            m = len(array)//2
            l = array[:m]
            r = array[m:]
            l = self.sort_array(l)
            r = self.sort_array(r)
            return self.merge_array(l, r)
        else:
            return array

    
    def sort(self):
        self.data = self.sort_array(self.data);
        return self.data
        
class DisplayPartiallySorted(DisplayPartiallySortedBase):
    """
        Implement all the necessary methods here
    """
    def merge_array(self, l, r):
        array = [None] * (len(l) + len(r))
        i = j = k = 0
        while i < len(l) and j < len(r):
                if l[i] < r[j]:
                    array[k] = l[i]
                    i += 1
                else:
                    array[k] = r[j]
                    j += 1
                k += 1
        while i < len(l):
            array[k] = l[i]
            i += 1
            k += 1
        while j < len(r):
            array[k] = r[j]
            j += 1
            k += 1
        return array
        
    
    def sort_array(self, array):
        if len(array) > 1:
            m = len(array)//2
            l = array[:m]
            r = array[m:]
            l = self.sort_array(l)
            r = self.sort_array(r)
            return self.merge_array(l, r)
        else:
            return array
            
    def sort(self):
        schedule = self.schedule
        sorted_extra_planes = self.sort_array(self.extra_planes)        
        return self.merge_array(schedule, sorted_extra_planes)
    

    
    