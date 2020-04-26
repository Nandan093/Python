





print('''\n
                                                                  DATA STRUCTURE
                                                                        |
                        -----------------------------------------------------------------------------------------------------
                        |                                               |                                                   |
                    1.Stack                                          2.Queue                                         3.Linked list
                        |                                               |                                                   |
                    Operations in Stack                             Operation in Queue                               Operation in Linked list
                     1.Push()                                         1.Enqueue()                                        1.Push
                     2.Pop()                                          2.Dequeue()                                        2.Pop
                     3.Add()                                          3.Add()                                            3.Insertion
                     4.Remove()                                       4.Remove()                                         4.Deletion
                     5.Size of Stack                                  5.Size of Queue                                    
                     6.Search                                         6.Search

''')                            

#-----------------------------------------------------------------------------------------------------------------------------------------------------------#
#Defining function for selection
def selection():
    
    head,tail = 0,0
    #Selecting Stack or Queue
    print('''Data Stucture Available:
                   1.Stack
                   2.Queue
                   3.Linked list
                   4.Exit''')

    select = input("Select any one DS available from the available above : ")

    #Initilizing the empty memory block
    items = []

    head,tail =0,0

    #Condition to check for Stack/Queue
    if(select == '1'):
        Stack()

    elif(select == '2'):
        Queue()

    elif(select == '3'):
        Linked_list()
        
    else:
        print("Invalid Input Enter the valid input")
        selection()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------#

#Defining a Stack function
def Stack():
    print("What is Stack ?")
    print('''          Stack is an abstract data type with a bounded(predefined) capacity. It is a simple
          data structure that allows adding and removing elements in a particular order. Every time an
          element is added, it goes on the top of the stack and the only element that can be removed is
          the element that is at the top of the stack.

          Basic features of Stack : -
           1) Stack is an ordered list of similar data type.
           2) Stack is a LIFO(Last in First out) structure or we can say FILO(First in Last out).
           3) "push()" function is used to insert new elements into the Stack and "pop()" function is used to remove an element from the stack.
              Both insertion and removal are allowed at only one end of Stack called Top.
           4) Stack is said to be in Overflow state when it is completely full and is said to be in Underflow state if it is completely empty.''')
    operation_stack()
#----------------------------------------------------------------------------------------------------------------------------------------------------------#

def operation_stack():
    
    while True:
        print('''\n The stack operation available:
              1.push
              2.pop
              3.add
              4.remove
              5.Size of Stack
              6.Search
              7.exit''')
    
        operation = input("Enter the Stack operation from above to perform : ")

        #Push operation
        if(operation == '1'):
            while True:
                try:
                    value = int(input("Enter the value to push to Stack : "))
                    break
                except:
                    print("Enter the valid value to push to stack")
            if(full_list()):
                print("Stack is full, Unable to add the element")
            else:
                push(int(value))
                
        # pop operation
        elif(operation == '2'):
            if(empty_list()):
                print("Stack is empty, There is no element to take out ")
            else:
                pop()
                
        #Add operation
        elif(operation == '3'):
            while True:
                try:
                    value = int(input("Enter the value to pop from stack : "))
                    break
                except:
                    print("Enter the valid value to add")
            if(full_list()):
                print("Stack is full, Unable to add the element")
            else:
                add(int(value))

        # Remove operation
        elif(operation == '4'):
            while True:
                try:
                    value = int(input("Enter the value to  Remove from Stack : "))
                    break
                except:
                    print("Enter the valid value to remove")
                    
            if(empty_list()):
                print("Stack is empty, There is no element to take out ")
            elif int(value) not in items:
                print("Value not available in Queue:Kindly enter valid operation")
            else:
                remove(int(value))
                
        #Size of the Stack
        elif(operation == '5'):
            length = len(items)
            print("The size of Stack = ",length)

        #Search operation
        elif(operation == '6'):
            while True:
                try:
                    value = int(input("Enter the value to  Search from Stack : "))
                    break
                except:
                    print("Enter the valid value to remove")
            Search(value)
        
        #Terminating the Operations
        elif(operation == '7'):
            selection()

        else:
            print("\nInvalid input. Enter the valid operation")
            operation_stack()


#push operation in stack
def push(x):
    items.append(x)
    print("Stack Memory Allocations :",items)

#pop operation in stack
def pop():
    items.pop()
    print("Popped items from stack :",items.pop())

#add operation in stack
def add(x):
    items.append(x)
    print("Stack Memory Allocations :",items)

#remove operation in stack
def remove(x):
    items.remove(x)
    print("Stack Memory Allocations :",items)

def Search(value):
    if value in items:
        print("Value is available in items")
    else:
        print("Value is not available in items")

#To check stack is empty
def empty_list():
    return items == []

#To check stack is full
def full_list():
    if(maxlength == len(items) ):
        return True
    else:
        return False
#------------------------------------------------------------------------------------------------------------------------------------------------------------#
def Queue():
    
    print("What is Queue ?")
    print('''     Queue is also an abstract data type or a linear data structure, just like stack data structure, in which the first element is inserted
          from one end called the REAR(also called tail), and the removal of existing element takes place from the other end called as FRONT(also called
         head.

         The process to add an element into queue is called "Enqueue" and the process of removal of an element from queue is called "Dequeue".

         Basic features of Queue:-
         1) Like stack, queue is also an ordered list of elements of similar data types.
         2) Queue is a FIFO( First in First Out ) structure.
         3) Once a new element is inserted into the Queue, all the elements inserted before the new element in the queue must be removed, to remove the new
            element.

         Disadvantage of Linear Queue:
         In a Linear queue, once the queue is completely full, it's not possible to insert more elements. Even if we dequeue the queue to remove some of the
         elements.''')
    operation_Queue()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------#

def operation_Queue():
    head , tail = 0,0
    while True:
        print('''\n The stack operation available:
              1.Enqueue
              2.Dequeue
              3.add
              4.remove
              5.Size of Queue
              6.Search
              7.exit''')
        
        #Asking user to perform specific operation
        while True:
            try:
                operation = input("Enter the Queue operation from above to perform : ")
                break
            except:
                print("Enter valid Input")
        
        #checking the conditions to perform specific operations
        #Enqueue operation
        if(operation == "1"):
            while True:
                try:
                    value = int(input("Enter the value to Enqueue to Queue : "))
                    break
                except:
                    print("Enter the valid value to enqueue")
            if(maxlength == tail):
                print("Queue is full and unable to add element")
            else:
                Enqueue(int(value))
                tail = tail + 1
        
        # Dequeue operation
        elif(operation == "2"):
            if(Empty_queue()):
                print("Queue is empty cannot retreive data from queue ")
            else:
                Dequeue()
                head = head + 1

        # Add operation        
        elif(operation == "3"):
            while True:
                try:
                    value = int(input("Enter the value to add to Queue : "))
                    break
                except:
                    print("Enter the valid value to add")
            if(maxlength == tail):
                print("Queue is full and unable to add element")
            else:
                Add(value)
                tail = tail + 1

        # Remove operation
        elif(operation == "4"):
            while True:
                try:
                    value = int(input("Enter the value to remove from Queue : "))
                    break
                except:
                    print("Enter the valid value to add")  
            if(Empty_queue()):
                print("Queue is empty cannot retreive data from queue ")
            elif int(value) not in items:
                print("Value not available in Queue:Kindly enter valid operation")
            else:
                Remove(int(value))

        #Size of the Queue
        elif(operation == '5'):
            length = len(items)
            print("The size of Queue = ",length)

        #Search operation
        elif(operation == '6'):
            while True:
                try:
                    value = int(input("Enter the value to  Remove from Queue : "))
                    break
                except:
                    print("Enter the valid value to Search")
            Search(value)
        
        #Exit operation        
        elif(operation == '7'):
            selection()
        
        else:
            print("\nInvalid input. Enter the valid operation")
            operation_Queue()


#Defining enqueue operation
def Enqueue(x):
    items.append(x)
    print("Memory Allocation in Queue : ",items)

#Defining dequeue operation
def Dequeue():
    items.pop(head)
    print("Memory Allocation in Queue : ",items)

#Defining add operation
def Add(value):
    items.append(value)
    print("Memory Allocation in Queue : ",items)

#Defining remove operation
def Remove(value):
        items.remove(value)
        print("Memory Allocation in Queue : ",items)

#Defining function to check empty Queue
def Empty_queue():
    return items == []    

#----------------------------------------------------------------------------------------------------------------------------------------------------------#
def Linked_list():
    
    print("What is Linked list ?")
    print('''     Linked List is a very commonly used linear data structure which consists of group of nodes in a sequence.

        Each node holds its own data and the address of the next node hence forming a chain like structure.

        Advantages of Linked Lists:-
        1) They are a dynamic in nature which allocates the memory when required.
        2) Insertion and deletion operations can be easily implemented.
        3) Stacks and queues can be easily executed.
        4) Linked List reduces the access time.

        Applications of Linked Lists
        1) Linked lists are used to implement stacks, queues, graphs, etc.
        2) Linked lists let you insert elements at the beginning and end of the list.
        3) In Linked Lists we don't need to know the size in advance.''')

    operation_Linked_list()
    
#-----------------------------------------------------------------------------------------------------------------------------------------------------------#

def operation_Linked_list():
    
    #Initiating address location
    head_addr = 0
    while True:
        print('''\n The stack operation available:
              1.Push
              2.pop
              3.insertion
              4.deletion
              5.exit''')
        
        #Asking user to perform specific operation
        while True:
            try:
                operation = input("Enter the Linked_list operation from above to perform : ")
                break
            except:
                print("Enter valid Input")
        
        #checking the conditions to perform specific operations
        #Push operation
        if(operation == "1"):
            while True:
                try:
                    value = int(input("Enter the value to push into Linked list : "))
                    break
                except:
                    print("Enter the valid value to enqueue")
            if(maxlength == head_addr):
                print("Linked list is full and unable to add element")
            else:
                push(int(value))
                head_addr = head_addr + 1
        
        # Pop operation
        elif(operation == "2"):
            if(Empty_list()):
                print("Linked list is empty cannot retreive data from queue ")
            else:
                pop()
                head_addr = head_addr - 1

        # insertion operation        
        elif(operation == "3"):
            print('''Insertion operation available:
                  1.Start
                  2.At particular position
                  3.Last
                  ''')
            option = input("Enter the available insertion operation : ")
            #Starting position
            if(option == '1'):
                while True:
                    try:
                        value = int(input("\nEnter the value to insert to list : "))
                        break
                    except:
                        print("Enter the valid value to insert")             
                items.insert(0,value)
                head_addr = head_addr + 1
                print("Linked list Memory Allocation : ",items)
                
            #At particular position
            elif(option == '2'):
                while True:
                    try:
                        value = int(input("\nEnter the value to insert to list : "))
                        position = int(input("\nEnter the position where we need to insert : "))
                        break
                    except:
                        print("Enter the valid value to insert")
                items.insert(position,value)
                head_addr = head_addr + 1
                print("Linked list Memory Allocation : ",items)
                
            #At last position
            elif(option == '3'):
                while True:
                    try:
                       value = int(input("\nEnter the value to insert to list : "))
                       break
                    except:
                        print("Enter the valid value to insert")             
                items.insert(-1,value)
                head_addr = head_addr + 1
                print("Linked list Memory Allocation : ",items)

            else:
                print("Enter the valid operation to perform " )             

        # deletion operation
        elif(operation == "4"):
            while True:
                try:
                    value = int(input("Enter the value to remove from Linked_list : "))
                    break
                except:
                    print("Enter the valid value to add")  
            if(Empty_list()):
                print("Linked_list is empty cannot retreive data from List")
            elif int(value) not in items:
                print("Value not available in Queue:Kindly enter valid operation")
            else:
                Deletion(int(value))
                head_addr = head_addr - 1
                
        
        #Exit operation        
        elif(operation == '5'):
            selection()
        
        else:
            print("\nInvalid input. Enter the valid operation")
            operation_Linked_list()


#Defining push operation
def push(x):
    items.append(x)
    print("Linked list Memory Allocation : ",items)

#Defining pop operation
def pop():
    items.pop()
    print("Linked list Memory Allocation : ",items)

#Defining Insertion operation
def Insertion(value,head_addr):
    items.insert(head_addr,value)
    print("Linked list Memory Allocation : ",items)

#Defining Deletion operation
def Deletion(value):
        items.remove(value)
        print("Linked list Memory Allocation : ",items)

#Defining function to check empty Queue
def Empty_list():
    return items == []

#--------------------------------------------------------------------------------------------------------------------------------------------------#
#Main program starts here:
while True:
    try:
#Memory allocation for storing stack/Queue
        maxlength = int(input("\nAllocate the memory for storing data : "))
        break
    except:
        print("\nInvalid Input for length")
    
head,tail,head_addr = 0,0,0
items = []
selection()
