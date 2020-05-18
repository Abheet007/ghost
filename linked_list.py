class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class Linked_List():
    def __init__(self):
        self.start=None

    def display_list(self):
        if self.start is None:
            print("list is empty")
            return
        else:
            p=self.start
            while p is not None:
                print(p.data," ",end='')
                p=p.next
            print()

    def count_nodes(self):
        p=self.start
        n=0
        while p is not None:
            p=p.next
            n+=1
        print("total number of nodes in the linked list are:{}".format(n))

    def search(self,x):
        p=self.start
        pos=1
        while p is not None:
            if p.data==x:
                print(x,"found at position:",pos)
                return True
            pos+=1
            p=p.next
        else:
            print(x,"not found in given linked list")
            return False

    def insert_at_beginning(self,data):
        temp=Node(data)
        temp.link=self.start
        self.start=temp

    def insert_at_end(self,data):
        temp=Node(data)
        if self.start is None:
            self.start=temp
            return
        p=self.start
        while p.next is not None:
            p=p.next
        p.next=temp


    def create_list(self):
        n=int(input("enter number of nodes:"))
        if n==0:
            return
        for i in range(n):
            data=int(input("enter the element to be inserted"))
            self.insert_at_end(data)

    def insert_before(self,data,x):
        if self.start is None:
            print("list is empty")
            return
        if x==self.start.data:
            temp=Node(data)
            temp.next=self.start
            self.start=temp
            return

        p=self.start
        while p.next is not None:
            if p.next.data==x:
                break
            p=p.next
        if p.next is None:
            print(x,"is not present in list")
        else:
            temp=Node(data)
            temp.next=p.next
            p.next=temp
    def insert_at_position(self,data,k):
        if k==1:
            temp=Node(data)
            temp.next=self.start
            self.start=temp
            return

        p=self.start
        i=1
        while i<k-1 and p is not None:
            p=p.next
            i+=1
        if p is None:
            print("you can only insert upto position",i)
        else:
            temp=Node(data)
            temp.next=p.next
            p.next=temp

    def delete_node(self,x):

        if self.start is None:
            print("list is empty")
            return

        #deletion of first node
        if self.start.data==x:
            self.start=self.start.next
            return

        #deletion in between or at the end
        p=self.start
        while p.next is not None:
            if p.next.data==x:
                break
            p=p.next

        if p.next is None:
            print("element ",x ,"not found in the list")
        else:
            p.next=p.next.next

    def reverse_list(self):
        prev=None
        p=self.start
        while p is not None:
            next_node=p.next
            p.next=prev
            prev=p
            p=next_node
        self.start=prev

    def bubble_sort_exdata(self):
        end=None

        while end!=self.start.next:
            p=self.start
            while p.next!=end:
                q=p.next
                if p.data>q.data:
                    p.data,q.data=q.data,p.data
                p=p.next
            end=p

    def bubble_sort_exlinks(self):
        end=None

        while end!=self.start.next:
            r=p=self.start
            while p.next!=end:
                q=p.next
                if p.data>q.data:
                    p.next=q.next
                    q.next=p
                    if p!=self.start:
                        r.next=q
                    else:
                        self.start=q
                    p,q=q,p
                r=p
                p=p.next
            end=p

    def _merge(self,p1,p2):

        if p1.data <= p2.data:
            startM=p1
            p1=p1.next
        else:
            startM=p2
            p2=p2.next
        pM=startM

        while p1 is not None and p2 is not  None:
            if p1.data<=p2.data:
                pM.next=p1
                pM=pM.next
                p1=p1.next
            else:
                pM.next = p2
                pM = pM.next
                p2 = p2.next

            if p1 is None:
                pM.next=p2
            else:
                pM.next=p1
            return  startM



    def merge(self,list2):
        merge_list=Linked_List()
        merge_list.start=self._merge(self.start,list2.start)
        return merge_list



#-----------------------------------------

    def merge_sort(self):
        self.start=self._merge_sort_rec(self.start)

    def _merge_sort_rec(self,list_start):#list_start is reference to the first node of the list to be sorted
        #if the list is empty or has 1 element
        if list_start is None or list_start.next is None:
            return list_start
        #if more than 1 element
        start1=list_start
        start2=self._divide_list(list_start)
        start1=self._merge_sort_rec(start1)
        start2=self._merge_sort_rec(start2)
        startM=self._merge(start1,start2)
        return startM

    def _divide_list(self,p):
        q=p.next
        while q is not None and q.next is not None:#q will become null if list has even number of nodes and q.next will become null if list has even number of nodes
            p=p.next
            q=q.next.next
        start2=p.next
        p.next=None
        return start2
    #cycle detection and removal
    def has_cycle(self):
        if self.find_cycle() is None:
            return False
        else:
            return True

    def find_cycle(self):
        if self.start is None or self.start.next is None:
            return None
        slower=self.start
        faster=self.start
        while faster is not None and faster.next is not None:
            slower=slower.next
            faster=faster.next.next
            if slower==faster:
                return slower
        return None

    def remove_cycle(self):
        c=self.find_cycle()
        if c is None:
            return
        print("Node at which cycle was detected is:",c.data)

        p,q=c
        len_cycle=0
        while True:
            len_cycle+=1
            q=q.next
            if p==q:
                break
        print("length of cycle is:",len_cycle)
        len_of_remain_list=0
        p=self.start
        while p!=q:
            len_of_remain_list+=1
            p=p.next
            q=q.next

        print("number of nodes not included in the cycle are:",len_of_remain_list)
        total_length=len_of_remain_list+len_cycle
        p=self.start
        count=0
        while count!=(total_length-1):
            p=p.next
        p.next=None

    def insert_cycle(self,x):
        if self.start is None:
            return None
        p=self.start
        px=None
        prev=None
        while p is not None:
            if p.data==x:
                px=p
            prev=p
            p=p.next
        if px is not None:
            prev.next=px
        else:
            print(x," is not present in the list")

##################################################################################################################################################################################################

l=Linked_List()
l.create_list()
while True:
    print("1:display list")
    print("2:count the number of node ")
    print("3:Search for an element ")
    print("4:Insert in an empty list/insert a the beginning of list ")
    print("5:Insert at end of the list ")
    print("6:Insert before a specified node ")
    print("7:Insert at a specified position ")
    print("8:Delete node at any position ")
    print("9:Reverse the linked list")
    print("10:Bubble sort by exchanging data ")
    print("11:Bubble sort by exchanging links ")
    print("12:Mergesort  ")
    print("13:insert cycle ")
    print("14:Detect cycle")
    print("15:Remove cycle")
    print("16:Quit ")

    op=int(input("Enter your choice: "))
    if op==1:
        l.display_list()
    elif op==2:
        l.count_nodes()
    elif op==3:
        data=int(input("Enter data to be searched in the linked list"))
        l.search(data)
    elif op==4:
        data = int(input("Enter data to be inserted in the beginning in the linked list"))
        l.insert_at_beginning(data)
    elif op==5:
        data = int(input("Enter data to be inserted at end in the linked list"))
        l.insert_at_end(data)
    elif op==6:
        data=int(input("Enter data of node:"))
        x=int(input("Enter position before which node is to be inserted"))
        l.insert_before(data,x)
    elif op==7:
        data = int(input("Enter data to be searched in the linked list"))
        x = int(input("enter position"))
        l.insert_at_position(data,x)
    elif op==8:
        data=int(input("Enter data to be deleted"))
        l.delete_node(data)
    elif op==9:
        l.reverse_list()
    elif op==10:
        l.bubble_sort_exdata()
    elif op==11:
        l.bubble_sort_exlinks()
    elif op==12:
        l.merge_sort()
    elif op==13:
        data=int(input("enter the element at which cycle is to be inserted"))
        l.insert_cycle(data)
    elif op==14:
        if l.find_cycle() :
            print("List has cycle")
        else:
            print("List does not have cycle")
    elif op==15:
        l.remove_cycle()
    else:
        if op==16:
            break



















































