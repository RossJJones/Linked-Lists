class Node():
    def __init__(self,data):
        self.__head = False
        self.__length = 0
        self.__previous = None
        self.__next = None
        self.__data = data
    def Get_Next(self):
        return(self.__next)
    def Set_Next(self,node):
        self.__next = node
    def Get_Previous(self):
        return(self.__previous)
    def Set_Previous(self,node):
        self.__previous = node
    def Get_Head(self):
        return(self.__head)
    def Set_Head(self,head):
        if head:
            self.__head = True
        elif not head:
            self.__head = False
    def Get_Length(self):
        if self.__head:
            return(self.__length)
        else:
            print("Not head node")
    def Set_Length(self,num,val):
        if self.__head and val:
            self.__length += num
        elif self.__head and not val:
            self.__length -= num
        else:
            print("Not head node")
    def Get_Data(self):
        return(self.__data)

#setup
head = Node("Head")
head.Set_Head(True)
head.Set_Length(1,True)
node = head
arr = ["A","B","C","Tail"] #List od node names
for i in range(0,4): #4 nodes, total 5 with head
    node.Set_Next(Node(arr[i])) #New node made
    node.Get_Next().Set_Previous(node) #Point new node to current node
    node = node.Get_Next() #Next node
    head.Set_Length(1, True) #Update length
print("Linked List Setup")

#Traverse a linked list
def Traverse():
    node = head #Start at head
    for i in range(head.Get_Length()): #Loop through list
        print(node.Get_Data()) #Print node data
        node = node.Get_Next() #Next node

#Add to linked list
def Add():
    data = input("What would you like to put in this node?") #Input data
    pos = input("What position would you like to place this node? Head for start and Tail for end") #Input position
    global head #Tell Python to stop being silly 
    node = head #Start at head
    if pos == "Tail": #Check if Tail is being added
        for i in range(1,head.Get_Length()+1): #Loooooop through list
            if i == head.Get_Length(): #Check if at the end of list
                node.Set_Next(Node(data)) #Create new node
                node.Get_Next().Set_Previous(node) #New node pointers being set
                head.Set_Length(1,True) #Increase length
            node = node.Get_Next() #Next node
    elif pos == "Head": #Check if Head is being added
        head.Set_Previous(Node(data)) #New node
        head.Get_Previous().Set_Next(head) #Swapping pointers
        head.Get_Previous().Set_Head(True) #Setup new head
        head.Get_Previous().Set_Length(head.Get_Length()+1,True) #Swap length attribute
        head.Set_Length(head.Get_Length(),False) #Remove length from old head
        head.Set_Head(False) #Remove head rights from old head, long live new head! 
        head = head.Get_Previous() #Replace head
    else: #if number position given
        for i in range(1,head.Get_Length()): #Loooooop through list
            if i == int(pos) - 1: #If at chosen position
                node.Get_Next().Set_Previous(Node(data)) #New node
                node.Get_Next().Get_Previous().Set_Next(node.Get_Next()) #Set new node next to current next
                node.Set_Next(node.Get_Next().Get_Previous()) #Next gets set to new node
                node.Get_Next().Set_Previous(node) #New node previous set to current node
                head.Set_Length(1,True) #Change length
            node = node.Get_Next() #Next node

def Delete():
    data = input("What would you like to delete?") #input
    node = head #Start at the head
    for i in range(0,head.Get_Length()): #Loop through linked list
        if node.Get_Data() == data: #Check for common data
            node.Get_Next().Set_Previous(node.Get_Previous()) #Swap pointer of next node
            node.Get_Previous().Set_Next(node.Get_Next()) #Swap pointer of previous node
            head.Set_Length(1,False) #Reduce list length
        node = node.Get_Next() #Next node



    


    
