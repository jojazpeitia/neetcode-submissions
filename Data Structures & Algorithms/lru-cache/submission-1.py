class Node:
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.next, self.prev = None, None

class LRUCache:

    def __init__(self, capacity: int):
        # needa create the cap variable
        self.cap = capacity

        # needa create the left and right nodes
        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        # have the head and tail pointing to each other for we can then start the ll
        self.head.next = self.tail
        self.tail.prev = self.head

        # needa create the hashmap that will be used for accesing values fast
        self.cache = {}

    def remove(self, key):
        # remove alg here
        # need to remember that we remove from any where in list
        key.prev.next = key.next
        key.next.prev = key.prev
        key.prev = None
        key.next = None


    def add(self, key):
        # remove alg here
        # need to remember that add always goes to right most    
        key.prev = self.tail.prev
        self.tail.prev.next = key
        self.tail.prev = key
        key.next = self.tail


    def get(self, key: int) -> int:
        
        # we need to retrieve the value
        # first need to see if it exists in the hashmap
        # if it does, return the node's value
        # if it doesnt return -1
        # also need to make sure that we move the node to the front of list
        # front of the list is where the most recent cached item is
        # 1. need to first remove the node
        # 2. need to then add to end of list

        if key in self.cache:
            self.remove(self.cache[key])
            self.add(self.cache[key])
            return self.cache[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # if it exists, we move the current thing from cache, and readd it (this is in case they update the value only and stuff)
        # else we can just add it normally
        # need to rememebr to add it to the hashmap, and to the right of our ll

        # when we add it, we also need to see if went past capacity
        # ^ if it did, we remove left most item (lru)


        if key in self.cache:
            self.remove(self.cache[key])
            self.cache[key] = Node(key, value)
            self.add(self.cache[key])
        else:
            self.cache[key] = Node(key, value)
            self.add(self.cache[key])

            if len(self.cache) > self.cap:
                del self.cache[self.head.next.key]
                self.remove(self.head.next)




        
