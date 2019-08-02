class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        dummy = Node("dummy")
        self.head = dummy
        self.tail = dummy 
        
        self.current = None
        self.before = None
        
        self.num_of_data = 0

    def append(self, data):
        #append called then create new node
        new_node = Node(data)
        # self.tail = Node('something') and NOde has tail instance
        self.tail.next = new_node
        self.tail = new_node
        
        self.num_of_data +=1
    
    def delete(self):
        #current searching referenced data 
        pop_data = self.current.data
        # if data is in last node, change tail references
        if self.current is self.tail:
            self.tail = self.before
        # change before node's reference to current's next node
        self.before.next = self.current.next
        #current 가 다음 노드가 아닌 이전 노드로 변경된다.  왜? 
        self.current = self.before
        
        self.num_of_data -= 1 
        
        return pop_data 

    def first(self):
        if self.num_of_data == 0:
            return None
        # always move before first and change current node 
        self.before = self.head
        #you know self.head is always dummy node. actual first data is placed after dummy node. 
        self.current = self.head.next 
        
        return self.current.data
        
    def next(self):
        if self.current.next == None:
            return None
        self.before = self.current
        self.current = self.current.next

        return self.current.data 

    def size(self):
        return self.num_of_data
        
