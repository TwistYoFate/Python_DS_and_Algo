#This is a class for implementing Queue
class Q:
    def __init__(self):
        self.__que=[]

    def queue(self,val):
        self.__que.append(val)

    def dequeue(self):
        x=self.__que[0]
        del(self.__que[0])
        return x

    def sizee(self):
        return len(self.__que)

# A class to create nodes
class node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.key=key


#Traversals

def inorder(root):
    if root:
        inorder(root.left)
        print(root.key),
        inorder(root.right)

def preorder(root):
    if root:
        print(root.key),
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.key),

def lot(root):                                           #Level Order Traversal
    q=Q()
    q.queue(root)
    while(q.sizee()):
        a=q.dequeue()
        print(a.key)
        if(a.left):
            q.queue(a.left)
        if(a.right):
            q.queue(a.right)

# without using Q class
# def lot(root):
#     q=[]
#     q.append(root)
#     while(len(q)):
#         a=q[0]
#         del(q[0])
#         print(a.key)
#         q.append(a.left)
#         q.append(a.right)        

def dft(root):                                           #Depth First Search
    stack=[]
    stack.append(root)
    while(len(stack)):
        a=stack.pop()
        print(a.key)
        if(a.left):
            stack.append(a.left)    
        if(a.right):
            stack.append(a.right)  

def inorder_itr(root):
    stack=[]
    current=root
    while True:
        if(current):
            stack.append(current)
            current=current.left
        elif(stack):
            current=stack.pop()
            print(current.key)
            current=current.right
        else:
            break        


root=node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.left.right=node(5)

print("Inorder:")
inorder(root)

print("Preorder:")
preorder(root)

print("Postorder:")
postorder(root)

print("lot")
lot(root)

print("dft")
dft(root)

print("inorder_itr")
inorder_itr(root)