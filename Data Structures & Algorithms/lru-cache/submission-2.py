class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next, self.prev = None, None

class LRUCache:

    def __init__(self, capacity: int):
        # cap variable
        self.cap = capacity

        # doubly ll set up
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

        # hashmap set up
        self.cache = {}

    def remove(self, node):
        # remove alg
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

        node.next, node.prev = None, None

    def add(self, node):
        # add alg
        self.tail.prev.next = node
        node.prev = self.tail.prev
        self.tail.prev = node
        node.next = self.tail


    def get(self, key: int) -> int:
        # return -1 if doesnt exist
        # return the value of the node
        # remove node from list if it exists, then add it back again to front to keep LRU pattern

        if key in self.cache:
            node = self.cache[key]

            self.remove(node)
            self.add(node)

            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # as simple as adding to the end of ll and hashmap if doesnt exist
        # if exists, we just remove, and add again, and make sure to have the node have that value updated i think
        # WE also have to run the cap check, and remove LRU to make space
        # ^ also have to make sure we remove it from hashmap

        if key in self.cache:
            node = self.cache[key]

            # makes sure to update the value
            # then we move the right after
            node.val =value

            # make it MRU
            self.remove(node)
            self.add(node)
        else:
            node = Node(key, value)

            self.cache[key] = node
            self.add(node)

            # remove LRU if exceeds cap
            if len(self.cache) > self.cap:
                lru = self.head.next

                self.remove(lru)
                del self.cache[lru.key]