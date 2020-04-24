from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # if there are less items currently instorage than the capacity
        # then we add the new item to the tail
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.head
            # oldest added becomes the current

        # else if the max capacity has been met already
        # we must first remove the oldest item (should be the current head)
        # we then add the new item to the tail
        # self.current is a marker to tell us that we've gone through everything and hit our lru
        else:
            lru = self.storage.head
            self.storage.remove_from_head()
            self.storage.add_to_tail(item)
            if lru == self.current:
                self.current = self.storage.tail

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        # add current to the contents array
        # next, find the next node and set the while loop to iterate from this point
        cur = self.current
        list_buffer_contents.append(cur.value)

        # if there's more than one node set the next node for the loop
        if cur.next:
            next_node = cur.next
        else:
            next_node = self.storage.head

        # start with the node after cur
        # add each node to the contents arr
        # until end of loop is reached (.next is equal to None)
        # make next_node equal the head so loop will end
        # since next_node and cur are both the head
        while next_node is not cur:
            list_buffer_contents.append(next_node.value)
            if next_node.next:
                next_node = next_node.next
            else:
                next_node = self.storage.head

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
