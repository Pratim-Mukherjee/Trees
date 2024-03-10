#!/usr/bin/env python
# coding: utf-8

# # Inorder Traversal

# In[34]:


class Node:
    def __init__(self,value):
        self.left=None
        self.data=value
        self.right=None
        
class Tree:
    def create_node(self, data):
        return Node(data)

    def insert_node(self, node, data):
        if node is None:
            return self.create_node(data)
        if data < node.data:
            node.left = self.insert_node(node.left, data)
        else:
            node.right = self.insert_node(node.right, data)
        return node
    
    def inorder_traversal(self,root):  # l, rt, R
        if root is not None:
            self.inorder_traversal(root.left)
            print(root.data)
            self.inorder_traversal(root.right)
            
    def Preorder_traversal(self,root):  # rt, L, R
        if root is not None:
            print(root.data)
            self.Preorder_traversal(root.left)
            self.Preorder_traversal(root.right)
    def height(self,root):
        if root is None:
            return-1
        return max(self.height(root.left), self.height(root.right))+1
            
#driver code
tree=Tree() #object for the class tree has been created and stored in variable tree
root=tree.create_node(5)
print(f"The first node is\n",root.data)
tree.insert_node(root,2)
tree.insert_node(root,10)
tree.insert_node(root,7)
tree.insert_node(root,15)
tree.insert_node(root,12)
tree.insert_node(root,20)
tree.insert_node(root,30)
tree.insert_node(root,6)
tree.insert_node(root,8)
print('Inorder traversal ---->')
tree.inorder_traversal(root)
print("Preorder traversal--->")
tree.Preorder_traversal(root)
print("Height of the binary tree is:", tree.height(root))


# # Preorder Traversal (snippet)
# 

# In[25]:


def Preorder_traversal(self,root):
    if root is not None:
        print(root.data)
        self.Preorder_traversal(root.left)
        self.Preorder_traversal(root.right)


# # Inorder Traversal (snippet)

# In[29]:


def inorder_traversal(self,root):  # l, rt, R
    if root is not None:
        self.inorder_traversal(root.left)
        print(root.data)
        self.inorder_traversal(root.right)


# # Postorder Traversal (snippet)

# In[31]:


def postorder_traversal(self,root):
    if root is not None:
        self.postorder_traversal(root.left)
        self.postorder_traversal(root.right)
        print(root.data)


# # Height of a binary Tree

# In[32]:


def height(self,root):
    if root is None:
        return-1
    return max(self.height(root.left), self.height(root.right))+1


# # Top View (snippet)

# In[35]:


def topview(root):
    q=[]
    d=dict()
    root.level=0
    q.append(root)
    while len(q)!=0:
        root=q.pop(0 )
        if root.level not in d:
            d[root.level]=root.info
        if root.left is not None:
            q.append(root.left)
            root.left.level=root.level-1
        if root.right is not None:
            q.append(root.right)
            root.right.level=root.level+1
    print(*d.values())
    


# # Is it a BST (with Inorder travesal)

# In[36]:


def checkBST(root):
    def Inorder_traversal(root, values):
        if root is None:
            return
        Inorder_traversal(root.left, values)
        values.append(root.data)
        Inorder_traversal(root.right, values)
    values=[]
    Inorder_traversal(root,values)
    for i in range(len(values)-1):
        if values[i]>=values[i+1]:
            return False
        return True
        


# # Binary Search Insertion

# In[30]:


def insert(self,val):
    if self.root is None:
        self.root=Node(val)
        return
    root=self.root
    while 1:
        if val<root.info:
            if root.left is not None:
                root=root.left
            else:
                root.left=Node(val)
                break
        elif val>=root.info:
            if root.right is not None:
                root=root.right
            else:
                root.right=Node(val)
                break


# In[ ]:




