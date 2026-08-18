class MyHashSet:

    def __init__(self):
        self.freq = {}
        

    def add(self, key: int) -> None:
        self.freq[key] = 1
        

    def remove(self, key: int) -> None:
        self.freq[key] = 0
        

    def contains(self, key: int) -> bool:
        if self.freq.get(key,0) == 1:
            return True
        return False    


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)