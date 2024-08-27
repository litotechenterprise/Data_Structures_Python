class MaxHeap:
    def __init__(self):
        self.heap = []
    def __left_child__(self, index):
        # when not using index 0
        # return 2 * index
        return 2 * index + 1
    def __right_child__(self,index):
        # when not using index 0
        # return 2 * index + 1
        return 2 * index + 2
    def __parent__(self, index):
        return (index -1) // 2
    
    def __swap__(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2] , self.heap[index1]

    def __sink_down__(self, index = 0):
        max_index = index
        while True:
            left_index = self.__left_child__(index)
            right_index = self.__right_child__(index)
            if left_index < len(self.heap) and self.heap[left_index] > self.heap[max_index]:
                max_index = left_index

            if right_index < len(self.heap) and self.heap[right_index] > self.heap[max_index]:
                max_index = right_index

            if max_index != index:
                self.__swap__(index, max_index)
                index = max_index
            else:
                return


    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) -1

        while current > 0 and self.heap[current] > self.heap[self.__parent__(current)]:
            self.__swap__(current, self.__parent__(current))
            current = self.__parent__(current)

        return True
    

    def remove(self):
        size = len(self.heap)
        if size == 0:
            return None
        if size == 1:
            return self.heap.pop()
        
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.__sink_down__()

        return max_value