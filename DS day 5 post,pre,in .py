class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
def printinorder(root):
    if root:
        #first recur on left child
        printinorder(root.left)
        #then print the data of node
        print(root.val,end=" "),
        #now recur on right child
        printinorder(root.right)
def printpostorder(root):
    if root:
         #first recur on left child
        printpostorder(root.left)
         #then print the data of node
        print(root.val,end=" "),
         #now recur on right child
        printpostorder(root.right)
def printpreorder(root):
    if root:
        
         #first recur on left child
        printpreorder(root.left)
         #then print the data of node
        print(root.val,end=" "),
         #finally recur on right child
        printpreorder(root.right)
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.right.left=Node(5)
print ("PRE-ORDER:")
printpreorder(root)
print()
print ("\nIN-ORDER:")
printinorder(root)
print()
print ("\nPOST-ORDER:")
printpostorder(root)
print()


