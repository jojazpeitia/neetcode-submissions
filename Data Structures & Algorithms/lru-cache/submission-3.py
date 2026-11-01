class Node:
    def __init__(self, key, value):
        self.value = value
        self.key = key
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        # init cache
        self.cache = {}

        # init doubly linked-list
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

        # init capacity
        self.cap = capacity

    def remove(self, key):
        # remove logic
        node = self.cache[key]

        nodePrev = node.prev
        nodeNext = node.next

        nodePrev.next = nodeNext
        nodeNext.prev = nodePrev

        node.prev, node.next = None, None

    def add(self, key):
        # add logic
        tmp = self.tail.prev
        tmp.next = self.cache[key]
        self.tail.prev = self.cache[key]

        self.cache[key].next = self.tail
        self.cache[key].prev = tmp
        
    def get(self, key: int) -> int:
        # retrieve the value from node if it exists
        # ^ if it does exist, we have to remove the node and add it to end of ll (mru)
        # other wise return -1

        if key in self.cache:
            val = self.cache[key].value
            self.remove(key)
            self.add(key)
            return val
        else: 
            return -1

    def put(self, key: int, value: int) -> None:
        # add key:node(value) to our cache 
        # ^ if it exists we just update the value of that node
        if key in self.cache:
            self.cache[key].value = value
            self.remove(key)
            self.add(key)
        else:
            node = Node(key, value)
            self.cache[key] = node

            # add node to ll
            self.add(key)

            if len(self.cache) > self.cap:
                oldest = self.head.next
                oldestKey = oldest.key

                # remove mru from ll
                self.remove(oldest.key)

                # delete from the cach
                del self.cache[oldestKey]


        # add node to the end of ll (lru)
        # ^ if this exceeds cache capacity, we have to remove left most item from ll (lru)




        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)