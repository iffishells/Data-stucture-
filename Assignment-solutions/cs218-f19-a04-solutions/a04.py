class Node:

    def __init__(self,data=None):
    	self.val=data
    	self.next=None

class Ring:
    def __init__(self):
    	self.head=None


def get_last(self):
    
    if self.head is None:
        return 
    #to get last node
    temp=self.head.next

    while temp.next!=self.head:
        temp=temp.next

    return temp
Ring.get_last=get_last
def __str__(self):
    re_str="["
    temp=self.head
    
    while temp is not None:
        re_str+=str(temp.val)+", "
        temp=temp.next
        if temp==self.head:
            break
    re_str=re_str.rstrip(", ")
    re_str+="]"
    return re_str
Ring.__str__=__str__


def insert(self,index,val):
    
    new_node=Node(val)
    last=self.get_last()
    
        
    if index==0:
        new_node.next=self.head
        self.head=new_node
        
        if last is None:
            self.head.next=self.head
        else:
            last.next=self.head
            
        return
    
    

            
    if self.head is None:
        raise Exception("List is Empty ")
        
    temp=self.head
    count=0
    while temp is not None and count<index:
        pre=temp
        temp=temp.next
        count+=1
    pre.next=new_node
    new_node.next=temp
    
    return
Ring.insert=insert

def len(self):
    if self.head is None:
        return 0
    
    if self.head.next is None:
        return 0
   
    count=1
    temp=self.head
    # [1 , 2 , 3 , 4]
    last=self.get_last()
    
    while temp!=last:
        temp=temp.next
        count+=1
        #print(count)
    return count
Ring.len=len
def push(self,val):
    
    new_node=Node(val)
    
    last=self.get_last()
    
    if last is None:
        self.head=new_node
        self.head.next=self.head
        return 
    last.next=new_node
    new_node.next=self.head
    
    return
Ring.push=push



def pop(self):
    
    if self.head is None:
        raise IndexError("List is empty , !Cannot be removed ")
        
    if self.head.next is self.head:
        val=self.head.val
        self.head=None
        return val
    
    #lenght=5
    index=self.len()-1
    print("last index",index)
    node_del=self.remove_at(index)
    last_node_value=self.get_last()
    
    return last_node_value.val
    

Ring.pop=pop

def get(self,index):
    
    
    if self.head is None:
        raise IndexError("List is empty")
    if index==0:
        return self.head.val
    
    temp=self.head
    count=0
    while temp is not None and count<index:
        pre=temp
        temp=temp.next
        count+=1
        if temp.val==count:
            break
    return temp.val
Ring.get=get
def remove_at(self,index):
    
    last=self.get_last()
    temp=self.head
    
    
    if self.head is None:
        return 0
    
    if index==0:
        if self.head.next == self.head:
            self.head=None
        else:
            self.head=self.head.next
            last.next=self.head
        return
    temp=self.head
    count=0
    while temp is not None and count<index:
        pre=temp
        temp=temp.next
        count+=1
    pre.next=temp.next
            
Ring.remove_at=remove_at  

def remove(self,val):
	
	if self.head is None:
		return
	temp=self.head
	last=self.get_last()

	if temp.val==val:
		if last==self.head:
			self.head=None
		else:
			self.head=temp.next
			last.next=self.head
		return

	pre=temp
	temp=temp.next

	while temp!=self.head:
		if temp.val==val:
			break
		pre=temp
		temp=temp.next
	if temp==self.head:
		return
	pre.next=temp.next
Ring.remove=remove           
if __name__ == '__main__': 
    r = Ring()
    # r.insert(1, 1)
    r.insert(0, 1)
    r.insert(1, 2)
    r.insert(2, 3)
    r.insert(3, 5)  # different behavrior since it's a ring! 
    print(r)


