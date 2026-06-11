class MyHashSet:

    def __init__(self):
        self.toDoSet = [[]] * 10000

    def add(self, key: int) -> None:
        index = hash(key) % 10000
        
        for s in self.toDoSet[index]:
            if s == key:
                return

        self.toDoSet[index].append(key)

    def remove(self, key: int) -> None:
        index = hash(key) % 10000

        for s in self.toDoSet[index]:
            if s == key:
                self.toDoSet[index].remove(key)
                return 

        return None

    def contains(self, key: int) -> bool:
        index = hash(key) % 10000

        for s in self.toDoSet[index]:
            if s == key:
                return True 

        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)