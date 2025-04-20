class LRUCache:
    
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None


    def __init__(self, capacity):
        self.capacity = capacity 
        self.keyValCache = {} # key -> linked list node reference
        
        self.cacheHead = self.Node(0, 0) # dummy head
        self.cacheTail = self.Node(0, 0) # dummy tail
        self.cacheHead.next = self.cacheTail
        self.cacheTail.prev = self.cacheHead



    # helper methods for the doubly linked list
    def addNode(self, node):
        # add the node to the front of the list
        node.prev = self.cacheHead 
        node.next = self.cacheHead.next 
        self.cacheHead.next.prev = node 
        self.cacheHead.next = node

    def removeNode(self, node):
        # remove the node from the list
        prevNode = node.prev
        nextNode = node.next 

        prevNode.next = nextNode 
        nextNode.prev = prevNode 
        node.prev = None
        node.next = None
        


    # main methods
    def get(self, key): # return the value of key if it exists, else -1
        if key in self.keyValCache:
            # move the node to the front of the list
            self.removeNode(self.keyValCache[key])
            self.addNode(self.keyValCache[key])

            return self.keyValCache[key].value
        
        else:
            return -1
        

    def put(self, key, value): # update the val of the key if it exists, else, add the key value pair to the cache and evict the LRU key if it is full
        if key in self.keyValCache: # if key is alr in the cache, update its value
            node = self.keyValCache[key]
            node.value = value

            # move the node to the front of the list
            self.removeNode(node)
            self.addNode(node)

        else: # key is not in the cache
            if len(self.keyValCache) >= self.capacity:
                # remove the LRU node (the last node in the list)
                lastNode = self.cacheTail.prev
                del self.keyValCache[lastNode.key]
                self.removeNode(lastNode)

            # add the new node to the front of the list
            newNode = self.Node(key, value)
            self.addNode(newNode)
            self.keyValCache[key] = newNode

        