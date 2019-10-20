class Person: 
    def __init__(self,men,Age,queue_Number):
        self.Men=men
        self.Age=Age
        self.queue_Number=queue_Number
    def get_priority(self):
        if self.Age>=40:
            priority=100-self.queue_Number
            return priority+100
        else:
            priority=100-self.queue_Number
            return priority
    def __str__(self):
        return str(self.Men)+" "+str(self.get_priority())

def heap_sort(lst):
    n=len(lst)
    
    build_heap(lst)
    
    for i in reversed(range(n)):
        print(i)
        lst[i] ,lst[0] =lst[0],lst[i]
        
        heapify(lst,i,0)
def build_heap(lst):  
    n=len(lst) #1
    for i in reversed(range(n//2)):
        #print("loop count in buid heap")
        #print( " value  of i = ,",i)
        #print( "value of n = ",n)
        heapify(lst,n,i)
            
def heapify(lst,n,root):
    largest=root  
    #1root=1
    l=2*root+1 #3
    r=2*root+2 #4    #198                 #190
    #print("lst[l].get_priority()", lst[l].get_priority())
    #print("lst[largest].get_priority()" ,lst[largest].get_priority())
    if l < n and lst[l].get_priority() < lst[largest].get_priority():
        largest=l # 1
        
                        #193            #198
    if r < n and lst[r].get_priority() < lst[largest].get_priority():
        largest=r  #2
        
    if largest!=root:
        lst[root],lst[largest]=lst[largest],lst[root]
        heapify(lst,n,largest)    


if __name__ == '__main__': 
    p = Person('A', 24, 1)
    p.get_priority()
    print(p) # should output: A 99

    p = Person('A', 40, 1) 
    print(p) # should output: A 199
    
    people = [ 
        Person('A', 24, 1), 
        Person('B', 32, 2), 
        Person('C', 45, 3), 
        Person('D', 22, 4), 
        Person('E', 21, 5), 
        Person('F', 32, 6), 
        Person('G', 39, 7), 
        Person('H', 44, 8), 
        Person('I', 22, 9), 
        Person('J', 29, 10), 
        Person('K', 32, 11), 
        Person('L', 31, 12) 
    ]
    print(p)
    print([str(p)  for p in people])
    heap_sort(people) 
    print([str(p)  for p in people])
    # sould output: 
    # ['C 197', 'H 192', 'A 99', 'B 98', 'D 96', 'E 95', 'F 94', 'G 93', 'I 91', 'J 90', 'K 89', 'L 88']
