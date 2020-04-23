print("----------------------------------------------------------------------------------------------------------------------------------------------------")
print("-------------------------------------------------------------Implementation of Stack and Queue------------------------------------------------------")
print("----------------------------------------------------------------------------------------------------------------------------------------------------")

#----------------------------------------------------------------------------------------------------------------------------------------------------------#

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
    
                    
    attempts = int(input("\nEnter the number of attempts to perform stack operation : "))
    head = 0
    tail = 0
    
    while attempts > 0:

    
        
        operation = input("\nEnter the operation to perform (push <value> / pop / exit): ").split()

        #Push operation
        if(operation[0] == 'push'):
            if(full_list()):
                print("Stack is full, Unable to add the element")
            else:
                push(int(operation[1]))
        # pop operation
        elif(operation[0] == 'pop'):
            if(empty_list()):
                print("Stack is empty, There is no element to take out ")
            else:
                pop()

        #Terminating the Operations
        elif(operation[0] == 'exit'):
            return 0
        attempts = attempts - 1

#push operation in stack
def push(x):
    items.append(x)
    print("Stack Memory Allocations :",items)

#pop operation in stack
def pop():
    print("Popped items from stack :",items.pop())

#To check stack is empty
def empty_list():
    return items == []

#To check stack is full
def full_list():
    if(maxlength == len(items) ):
        return True
    else:
        return False

#----------------------------------------------------------------------------------------------------------------------------------------------------------#

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

    #No.of attempts to perform operation
    attempts = int(input("\nEnter the number of attempts to perform Queue operation : "))
    head, tail = 0,0
    
    #Conditin to check attempts until it becomes zero
    while attempts > 0:
        
        #Asking user to perform specific operation
        operation = input("\nEnter the operation to perform (enqueue <value> /dequeue/ exit): ").split()
        
        #checking the conditions to perform specific operations
        if(operation[0] == "enqueue"):
            if(maxlength == tail):
                print("Queue is full and unable to add element")
            else:
                Enqueue(int(operation[1]))
                tail = tail + 1
        elif(operation[0] == "dequeue"):
            if(Empty_queue()):
                print("Queue is empty cannot retreive data from queue ")
            else:
                Dequeue()
                head = head + 1
        else:
            return 0

        attempts = attempts -1


#Defining enqueue operation
def Enqueue(x):
    items.append(x)
    print("Queue Memory Allocation : ",items)

#Defining dequeue operation
def Dequeue():
    items.pop(head)
    print(items)

#Defining function to check empty Queue
def Empty_queue():
    return items == []    

#----------------------------------------------------------------------------------------------------------------------------------------------------------#


#Main program starts here:

#Memory allocation for storing stack/Queue
maxlength = int(input("Allocate the memory for storing data : "))

head,tail = 0,0
#Selecting Stack or Queue
select = input("\nSelect '1' for 'Stack' or '2' for 'Queue' : ")

#Initilizing the empty memory block
items = []

#Condition to check for Stack/Queue
if(select == '1'):
    Stack()

elif(select == '2'):
    Queue()
