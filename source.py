import random
from time import time

#implementation of the NODE class "from the lecture"

class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self,newdata):
        self.data = newdata
    def setNext(self,newnext):
        self.next = newnext
#implementation of the LINKEDLIST class "from the lecture"

class UnorderedList:
    def __init__(self):
        self.head = None
        self.count = 0
    def isEmpty(self):
        return self.head == None
    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
        self.count+=1
    def length(self):
        return self.count
    def search(self,item):
        current = self.head
        while current != None:
            if current.getData() == item:
                return True
            else :
                current = current.getNext()
        return False
    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
            if previous == None:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())


#implementation of the LIST INSERTION SORT FUNCTION "from the lecture"

def list_insertionSort(alist):
    for index in range(1,len(alist)):


        currentvalue = alist[index]
        position = index
        while position > 0 and alist[position-1] > currentvalue:
                 alist[position] = alist[position-1]
                 position = position-1

        alist[position] = currentvalue

#implementation of the LINKED LIST INSERTION SORT FUNCTION "the task"

def linkedlist_insertionSort(alinkedlist):
    sortedlist = alinkedlist.head                                                                    #we assume that the first node is a sorted list "it has only one element"
    nextnode = alinkedlist.head.next                                                                 #second element.. like aList[1].. iteration
    sortedlist.next = None                                                                           #sorted list has only one element so its next is None
    while nextnode != None:                                                                          #we iterate from second element to the last "alist[i]"
        currentnode = nextnode                                                                       #second element
        nextnode = nextnode.next                                                                     #third element
        if currentnode.data <= sortedlist.data:                                                      #alist[0]<alist[i]
            currentnode.next = sortedlist                                                            #the current element will be the first element
            sortedlist = currentnode                                                                 #we assume that the first node "the current" is a sorted list "it may have more than one element"
        else:                                                                                        #alist[0]>alist[i]
            searchpointer = sortedlist                                                               #we do not need to search in the sorted list.. we will use (.next)
            while searchpointer.next != None and currentnode.data > searchpointer.next.data:         #we iterate from the first element after the sorted list to the last element "alist[i]"
                searchpointer = searchpointer.next                                                   #moving to the next element
            currentnode.next = searchpointer.next                                                    #current -> search (searchpointer.next)
            searchpointer.next = currentnode                                                         #searchpointer -> current -> search (searchpointer.next)
    alinkedlist.head=sortedlist                                                                      #making the sorted list the first element of the linked list "aList[0]"

def linkedlist_print(alinkedlist):
    current = alinkedlist.head
    s = '['
    while current != None:
        s += str(current.data)+', '
        current = current.next
    s += '\b\b]'
    print(s)

alinkedlist=UnorderedList()
alist=list()
for i in range(10000):
    x=random.randrange(-1000,1001)
    alinkedlist.add(x)
    alist.insert(0,x)


print('list:')

print(alist)
print('list length: ',len(alist))

print('linkedlist:')

linkedlist_print(alinkedlist)

print('linkedlist length: ',alinkedlist.length())

list_start=time()

list_insertionSort(alist)

list_end=time()

print('list:')

print(alist)

print('list time :',list_end-list_start)

linkedlist_start=time()

linkedlist_insertionSort(alinkedlist)

linkedlist_end=time()

print('linkedlist:')

linkedlist_print(alinkedlist)

print('linkedlist time :',linkedlist_end-linkedlist_start)
