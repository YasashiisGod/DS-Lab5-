"""
Created on day 11/11/2019
Course: CS 2302 - Data Structures
Author: Brian Perez
Assignment: Lab #5 
Instructor: Diego Aguirre 
D.O.L.M.: 12/02/19 
"""
class LRU_Node:
    def __init__(self, key, value, next = None, previous = None):
        self.key = key
        self.item = value;
        self.next = next;
        self.previous = previous

class LRUcache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dict = {}
        self.head = None
        self.tail = None
    
    def add (self, node):
        
        if self.head is None and self.tail is None:
            self.head = node
            self.tail = node
            
        self.tail.next = node
        node.previous = self.tail
        self.tail = node
        self.dict[node.key] = node      

    def remove(self, node):
        
        if self.head is None and self.tail is None:
            return None
        
        elif self.head == self.tail:
            self.head = None
            self.tail = None
            
        elif node == self.head:
          self.head = self.head.next 
          
        elif node == self.tail:
            self.tail = self.tail.previous
            
        else: #middle
            previous_node = node.previous
            next_node = node.next
            previous_node.next = next_node
            next_node.previous = previous_node
        
    def get(self, key):
        
        if key not in self.dict:
            return -1
        
        else:
            node = self.dict[key]
            self.remove(node)
            self.add(node)
            return node.item

    def put(self, key, value):
        
        if key in self.dict:
            self.remove(self.dict[key])
            
        new_node = LRU_Node(key, value)
        self.add(new_node)
        self.dict[key] = new_node
        
        if len(self.dict) > self.capacity:
            del self.dict[self.head.key]
            self.head = self.head.next          
        
    def printing(self):
        
        temp = self.head
        
        while temp is not None:
            print(temp.item, end=' ')
            temp = temp.next
            
        print()
        
    def max_capacity(self):
        return self.capacity
    
if __name__ == '__main__':
    
    LRU = LRUcache(5)
    
    LRU.put(9,1)
    LRU.put(9,2)
    LRU.put(8,4)
    LRU.put(7,3)
    LRU.put(9,1)
    LRU.get(7)
    LRU.put(5,5)
    
    LRU.printing()
    print(LRU.max_capacity())
    
    
    
    
    
    
    
