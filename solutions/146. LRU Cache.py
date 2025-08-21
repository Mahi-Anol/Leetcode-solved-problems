class NODE():
    def __init__(self,key,data)->None:
        self.key=key
        self.data=data
        self.next=None
        self.prev=None

        
class LINK_LIST():
    def __init__(self)->None:
        self.head=NODE(-1,-1)
        self.tail=NODE(-1,-1)
        self.head.next=self.tail
        self.tail.prev=self.head

    def add_node(self,node:NODE)->None:
        temp1=self.tail.prev
        temp1.next=node
        node.prev=temp1
        node.next=self.tail
        self.tail.prev=node

    def remove_node(self,node):
        left=node.prev
        right=node.next
        left.next=right
        right.prev=left

    def evict_least_used(self)->None:
        if self.head.next!=self.tail:
            key=self.head.next.key
            self.head.next=self.head.next.next
            self.head.next.prev=self.head
            return key

        else:
            print("evict failed")

    def make_recent(self,Node)->None:
        ### First part
        #removing from middle
        left=Node.prev
        right=Node.next
        left.next=right
        right.prev=left

        
        ###2nd part
        ###adding to tail
        left=self.tail.prev
        self.tail.prev=Node
        left.next=Node
        Node.prev=left
        Node.next=self.tail

        
        
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.map={}
        self.count=0
        self.most_recent_keys=LINK_LIST()
        


    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        else:
            self.most_recent_keys.make_recent(self.map[key])
            return self.map[key].data
        

    def put(self, key: int, value: int) -> None:

        removed_key=-2
        if key not in self.map:
            self.count+=1
            
        if self.count>self.capacity:
            self.map.pop(self.most_recent_keys.head.next.key,None)
            removed_key=self.most_recent_keys.evict_least_used()
            self.count-=1
            
        if key in self.map and key!=removed_key:
            self.most_recent_keys.remove_node(self.map[key])
            # self.map.pop(key,None)
            # self.count-=1

            
        self.map[key]=NODE(key,value)
        self.most_recent_keys.add_node(self.map[key])





            
            
            
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)