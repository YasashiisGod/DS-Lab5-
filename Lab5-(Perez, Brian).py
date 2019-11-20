class node():
    def __init__ (self, key = None, value = None):
        self.key = None 
        self.value = None 
        self.prev = None 
        self.next = None
  
class LRUCache :
    
    def __init__(self, head = None, tail = None, size):
        self.table = [[] for i in range(size)]
        self.head = None 
        self.tail = None 
        self.max_capacity = None
        
    def insert(self, k):
        location = self.hash(k)
        bucket = self.table[location]

        if not k in bucket: 
            bucket.append(k)


  # Hashtable backs up the Doubly Linked List for O(1) access to cache items
  
  Map <Integer, node> hashtable = new HashMap<Integer, node>();
  node head;
  node tail;

  int totalItemsInCache;
  int maxCapacity;

  public LRUCache(int maxCapacity) {
    # Cache starts empty and capacity is set by client
    totalItemsInCache = 0;
    this.maxCapacity = maxCapacity;

    # Dummy head and tail nodes to avoid empty states
    head = new node();
    tail = new node();

    # Wire the head and tail together
    head.next = tail;
    tail.prev = head;
  }

  public int get(int key) {
    node node = hashtable.get(key);

    if (node == null) {
      return -1; # we should throw an exception here, but for Leetcode's sake
    }

    # Item has been accessed. Move to the front of the cache
    moveToHead(node);

    return node.value;
  }

  public void put(int key, int value) {
    node node = hashtable.get(key);

    if (node == null) {
      # Item not found, create a new entry
      node newNode = new node();
      newNode.key = key;
      newNode.value = value;

      # Add to the hashtable and the actual list that represents the cache
      hashtable.put(key, newNode);
      addToFront(newNode);
      totalItemsInCache++;

      # If over capacity remove the LRU item
      if (totalItemsInCache > maxCapacity) {
        removeLRUEntry();
      }
    } else {
      # If item is found in the cache, just update it and move it to the head of the list
      node.value = value;
      moveToHead(node);
    }

  }

  private void removeLRUEntry() {
    node tail = popTail();

    hashtable.remove(tail.key);
    --totalItemsInCache;
  }

  private node popTail() {
    node tailItem = tail.prev;
    removeFromList(tailItem);

    return tailItem;
  }

  private void addToFront(node node) {
    # Wire up the new node being to be inserted
    node.prev = head;
    node.next = head.next;

    /*
      Re-wire the node after the head. Our node is still sitting "in the middle of nowhere".
      We got the new node pointing to the right things, but we need to fix up the original
      head & head's next.
      head <-> head.next <-> head.next.next <-> head.next.next.next <-> ...
      ^            ^
      |- new node -|
      That's where we are before these next 2 lines.
    */
    head.next.prev = node;
    head.next = node;
  }

  private void removeFromList(node node) {
    node savedPrev = node.prev;
    node savedNext = node.next;

    savedPrev.next = savedNext;
    savedNext.prev = savedPrev;
  }

  private void moveToHead(node node) {
    removeFromList(node);
    addToFront(node);
  }


}