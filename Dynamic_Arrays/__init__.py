
class DynamicArray:
    def __init__(self):
        self.length = 0
        self.data = {}


    def get(self, index:int):
        return self.data[index]
    
    def push(self, item) -> int:
        self.data[self.length] = item
        self.length += 1
        return self.length
    
    def pop(self):
        if self.length == 0:
            return None
        
        popped_item = self.data[self.length -1]
        self.data[self.length -1] = None
        self.length -= 1

        return popped_item
    

    def insert(self, index:int, item):
        if index > self.length -1 or index < 0:
            return None
        
        self.length += 1

        for i in range(self.length -1, index -1, -1):
            self.data[i] = self.data[i -1]

        self.data[index] = item

        return self.data
    
    def remove(self, index: int):
        if self.length == 0:
            return None
        
        if index > self.length -1 or index < 0:
            return None
        
        item_to_be_removed = self.data[index]

        for i in range(index, self.length-1):
            self.data[i] = self.data[i+1]

        self.data[self.length-1] = None
        self.length -= 1

        return item_to_be_removed