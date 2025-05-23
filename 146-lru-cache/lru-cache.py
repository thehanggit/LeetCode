class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # map key to node

        self.left, self.right = Node(0, 0), Node(0, 0)

        # left = LRU, right = MRU
        self.left.next = self.right
        self.right.prev = self.left
    #remove node from list    
    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev

    
    #insert at right
    def insert(self, node):
        prev, next = self.right.prev, self.right
        prev.next = next.prev = node
        node.next, node.prev = next, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        #check capacity
        if len(self.cache) > self.cap:
            # remove and delete the LRU from the cache
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
            





# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)