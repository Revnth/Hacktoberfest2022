class Node:
    '''
    an object for storing a single node of a linked list
    Models two attributes - data and the link to the next list
    '''

    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f'<Node data : {self.data}>'


class LinkedList:
    '''
    Singly linked list
    '''

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        '''
        Returns the number of nodes in a list. 
        Takes O(n) -> linear time 
        '''
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next_node

        return count

    def add(self, data):
        '''
        Adds a new node containing the data at the head of the list 
        Takes constant time
        '''
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        '''
        search for the first node that contains the data that matched the key
        Return None if not found

        takes O(n) - linear time 
        '''
        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    def insert(self, data, index):
        '''
        Inserts a new node containing data at index position
        Insertion takes contain time but finding the node at 
        insertion point  takes linear time ( O(n) )

        Takes overall O(n) time 
        '''
        if index == 0:
            self.add(data)

        if index > 0:
            new = Node(data)

            position = index
            current = self.head

            while position > 1:
                current = node.next_node
                position -= 1

            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new
            new.next_node = next_node

    def remove(self, key):
        '''
        Removes node that contains data matching the key
        Returns the node or Node if the doesnt exist 
        Takes O(n) time (linear search)
        '''
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node
        return current

    def node_at_index(self, index):
        if index == 0:
            return self.head
        else:
            current = self.head
            position = 0

            while position < index:
                current = current.next_node
                position += 1

            return current

    def __repr__(self):
        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append(f"[Head: {current.data}]")
            elif current.next_node is None:
                nodes.append(f"[Tail: {current.data}]")
            else:
                nodes.append(f"{current.data}")

            current = current.next_node
        return ' -> '.join(nodes)
