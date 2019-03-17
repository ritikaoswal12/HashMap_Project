import threading


class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.key == other.key
        return False


class HashMap:

    def __init__(self):
        self.DEFAULT_LOAD_FACTOR = 0.75
        self.capacity = 16
        self.bucket_list = [None] * self.capacity
        self.size = 0
        self.load_factor = self.size / self.capacity
        self.lock = threading.RLock()

    # Indexing key and placing the Node at the hashed position
    # if key exists update value
    # if hashcode returns same index, connect to previous node via linked list
    def put(self, key, value):
        self.lock.acquire()
        try:
            index = hash(key) % self.capacity
            n = Node(key, value)
            if not self.bucket_list[index]:
                self.bucket_list[index] = [n]
            else:
                list_at_index = self.bucket_list[index]
                for i in list_at_index:  # updating an existing value
                    if i == n:
                        i.value = n.value
                        return
                list_at_index.append(n)  # Adding to an already exiting bucket
            self.size += 1
            # Rehashing
            load_factor = self.size / self.capacity
            if load_factor > self.DEFAULT_LOAD_FACTOR:
                self.rehash()
        finally:
            self.lock.release()

    def get(self, key):
        self.lock.acquire()
        try:
            index = hash(key) % self.capacity
            if not self.bucket_list[index]:
                return False
            else:
                list_at_index = self.bucket_list[index]
                for i in list_at_index:
                    if i.key == key:
                        return i.value
        finally:
            self.lock.release()

    def remove(self, key):
        self.lock.acquire()
        try:
            index = hash(key) % self.capacity
            if not self.bucket_list[index]:
                return False
            else:
                list_at_index = self.bucket_list[index]
                for i in list_at_index:
                    if i.key == key:
                        list_at_index.remove(i)
        finally:
            self.lock.release()

    def map_size(self):
        return self.size

    def rehash(self):
        temp = self.bucket_list.copy()
        self.capacity = self.capacity * 2
        self.bucket_list = [None] * self.capacity
        self.size = 0
        for j in temp:
            if j:
                for element in j:
                    if element:
                        self.put(element.key, element.value)





