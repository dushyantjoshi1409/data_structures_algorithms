import ctypes
class customList():
    def __init__(self):
        initialcapacity = 1
        self.capacity = initialcapacity
        self.size = 0
        self.array = self.__create_array(self.capacity)

    def __create_array(self, capacity):
        #create a ctypes array with the given capacity
        return (capacity * ctypes.py_object)()
    
    def __resize_array(self, new_capacity):
        new_array = self.__create_array(new_capacity)
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array #replace old array with new array
        self.capacity = new_capacity #update the capacity

    def append(self, item):
        if self.size == self.capacity:
            self.__resize_array(2 * self.capacity)
        self.array[self.size] = item
        self.size += 1
    def __len__(self):
        return self.size

    def __str__(self):
        result = "["
        for i in range(self.size):
            result += str(self.array[i]) + ","
        return result[:-1] + "]"
    
    def pop(self):
        if self.size == 0:
            return "Empty List"
        popped_item = self.array[self.size - 1]
        self.size -= 1
        return popped_item
    
    def __getitem__(self, index):
        if index >= 0 and index < self.size:
            return self.array[index]
        else:
            return "Index out of bounds"

    def clear(self):
        self.size = 0

    def insert(self, position, item):
        if self.size == self.capacity:
            self.__resize_array(2 * self.capacity)
        for i in range(self.size, position, -1):
            self.array[i] = self.array[i - 1]
        self.array[position] = item
        self.size += 1
        
    def remove(self, position):
        if position < 0 or position >= self.size:
            return "Index out of bounds"
        for i in range(position, self.size - 1):
            self.array[i] = self.array[i + 1]
        self.size -= 1
        return self.array[position]
    
    
myList = customList()
myList.append(1)
myList.append(2)
myList.append(3)

myList.remove(1)
print(myList)
    
    