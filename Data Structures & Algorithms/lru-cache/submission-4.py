class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next, self.prev = None, None

class LRUCache:

    def __init__(self, capacity: int):
        # init cache
        self.cache = {}

        # init capacity
        self.cap = capacity

        # init doubly ll
        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, key):
        # remove logic here
        # [head] -> <- [0, 0] -> <- [tail]
        node = self.cache[key]

        node.prev.next = node.next
        node.next.prev = node.prev
        node.next, node.prev = None, None;

    def add(self, key):
        # add logic here
        # [head] -> <- [0, 0] -> <- [tail]
        # [head] -> <- [0, 0] -> <-[1, 1] -> <- [tail]
        node = self.cache[key]

        mru = self.tail.prev

        mru.next = node
        node.prev = mru

        node.next = self.tail
        self.tail.prev = node


    def get(self, key: int) -> int:
        # return the value corresponding to the key if the key exists, otherwise return -1

        if key in self.cache:
            # return value mapped to key !!
            # we have to make sure we update our ll to keep MRU at the front (rightmost)
            node = self.cache[key]
            val = node.value

            # update ll history
            self.remove(key)
            self.add(key)

            return val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. 
        # if the introduction of the new pair causes the cache to exceed its capacity, remove the least recently used key.

        if key in self.cache:
            # retrieve the node using the key, and update its value
            node = self.cache[key]
            node.value = value         

            # update ll history
            self.remove(key)
            self.add(key)
        else:
            # add key value-pair to cache
            node = Node(key, value)
            self.cache[key] = node

            # add it to the ll
            self.add(key)

            # check for capacity here in order to see if we have to remove lru
            if len(self.cache) > self.cap:
                LRUNode = self.head.next

                self.remove(LRUNode.key)
                del self.cache[LRUNode.key]







        
