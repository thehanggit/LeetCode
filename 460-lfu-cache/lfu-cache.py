# class ListNode:
#     def __init__(self, val, prev = None, next = None):
#         self.val = val
#         self.prev = prev
#         self.next = next

# class LinkedList:
#     def __init__(self):
#         self.left = ListNode(0)
#         self.right = ListNode(0, self.left)
#         self.left.next = self.right
#         self.map = {}
    
#     def length(self):
#         return len(self.map)

#     def pushRight(self, val):
#         node = ListNode(val, self.right.prev, self.right)
#         self.map[val] = node
#         self.right.prev = node
#         node.prev.next = node

#     def pop(self, val):
#         if val in self.map:
#             node = self.map[val]
#             next, prev = node.next, node.prev
#             next.prev = prev
#             prev.next = next
#             self.map.pop(val, None)


#     # poping the least recently used
#     def popLeft(self):
#         res = self.left.next.val
#         self.pop(res)
#         return res
    
#     def update(self, val):
#         self.pop(val)
#         self.pushRight(val)    


# class LFUCache:

#     def __init__(self, capacity: int):
#         self.cap = capacity
#         self.lfuCnt = 0
#         self.valMap = {} # Map key -> val
#         self.countMap = collections.defaultdict(int) # Map key - count
#         self.listMap = collections.defaultdict(LinkedList)

#     def counter(self, key):
#         cnt = self.countMap[key]
#         self.countMap[key] += 1
#         self.listMap[cnt].pop(key)
#         self.listMap[cnt + 1].pushRight(key)

#         if cnt == self.lfuCnt and self.listMap[cnt].length() == 0:
#             self.lfuCnt += 1

#     def get(self, key: int) -> int:
#         if key not in self.valMap:
#             return -1
#         self.counter(key)
#         return self.valMap[key]

#     def put(self, key: int, value: int) -> None:
#         if self.cap == 0:
#             return

#         if key not in self.valMap and len(self.valMap) == self.cap:
#             res = self.listMap[self.lfuCnt].popLeft()
#             self.valMap.pop(res)
#             self.countMap.pop(res)

#         self.valMap[key] = value
#         self.counter(key)
#         self.lfuCnt = min(self.lfuCnt, self.countMap[key])


class LFUCache:
    def __init__(self, capacity:int):
        self.cap = capacity
        self.key2val = {}
        self.key2freq = {}
        self.freq2key = collections.defaultdict(collections.OrderedDict)
        self.minf = 0
    
    def get(self, key: int) -> int:
        if key not in self.key2val:
            return -1
        
        oldfreq = self.key2freq[key]
        self.key2freq[key] = oldfreq + 1
        self.freq2key[oldfreq].pop(key)
        if not self.freq2key[oldfreq]:
            del self.freq2key[oldfreq]
        self.freq2key[oldfreq + 1][key] = 2
        if self.minf not in self.freq2key:
            self.minf += 1
        return self.key2val[key]

    def put(self, key: int, value: int) -> None:
        if self.cap <= 0:
            return
        if key in self.key2val:
            self.get(key)
            self.key2val[key] = value
            return

        if len(self.key2val) == self.cap:
            delkey,_ = self.freq2key[self.minf].popitem(last=False)
            del self.key2val[delkey]
            del self.key2freq[delkey]
        self.key2val[key] = value
        self.key2freq[key] = 1
        self.freq2key[1][key] = 1
        self.minf = 1

        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)