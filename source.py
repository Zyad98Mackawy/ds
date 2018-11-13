import random

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



def list_insertionSort(alist):
    for index in range(1,len(alist)):


        currentvalue = alist[index]
        position = index
        while position > 0 and alist[position-1] > currentvalue:
                 alist[position] = alist[position-1]
                 position = position-1

        alist[position] = currentvalue


def linkedlist_insertionSort(alinkedlist):
    '''

    :param alinkedlist:
    :return:
    '''

alinkedlist=UnorderedList()
alist=list()
for i in range(10000):
    x=random.randrange(-1000,1001)
    alinkedlist.add(x)
    alist.append(x)
