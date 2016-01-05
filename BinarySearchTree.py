class Node:
    left= None
    right= None
    parent= None
    data=0
    
    def __init__(self, data, parent):
        self.parent = parent
        self.data=data

    def print_In(self):

        if self.left:
            self.left.print_In()

        print self.data,

        if self.right:
            self.right.print_In()
            
    def print_Pre(self):

        print self.data,
        
        if self.left:
            self.left.print_Pre()

        if self.right:
            self.right.print_Pre()

    def print_Post(self):

        if self.right:
            self.right.print_Post()
            
        if self.left:
            self.left.print_Post()

        print self.data,


class BST:
    root= None        

    def ins(self, data):
        if self.root:
            temp= self.root
            
            while(temp):
                if data <= temp.data:
                    if temp.left is None:
                        temp.left = Node(data, temp)
                        return
                    else:
                        temp= temp.left
                        
                else:
                    if temp.right is None:
                        temp.right = Node(data, temp)
                        return
                    else:
                        temp= temp.right
                        
        else:
            self.root= Node(data, None)

    def lookup(self, data):
        if self.root == None:
            return False

        temp= self.root
        
        while(temp):
            if data == temp.data:
                return True
            
            if data < temp.data:
                temp= temp.left
            else:       
                temp= temp.right

        return False

    def delete(self, data):
        if self.root == None:
            raise ValueError('BST.delete(): BST is empty!')

        temp= self.root
        direct=0
        
        while(temp):
            if data == temp.data:
                if temp.left==None and temp.right==None:
                    if direct==0:
                        self.root= None
                    elif direct==1:
                        temp.parent.left= None
                    else:
                        temp.parent.right= None
                        
                elif temp.left==None:
                    temp.data= temp.right.data
                    temp.left= temp.right.left
                    temp.right= temp.right.right
                    
                elif temp.right==None:
                    temp.data= temp.left.data
                    temp.right= temp.left.right
                    temp.left= temp.left.left

                else:
                    if temp.right.left==None:
                        temp.data= temp.right.data
                        temp.right= temp.right.right
                        return
                        
                    burp= temp.right
                    while(burp.left):
                        burp= burp.left
                    temp.data= burp.data
                    burp.parent.left= burp.right
                        
                            
            if data < temp.data:
                temp= temp.left
                direct=1
            else:       
                temp= temp.right
                direct=2

        
        
    def print_In(self):
        self.root.print_In()

    def print_Pre(self):
        self.root.print_Pre()

    def print_Post(self):
        self.root.print_Post()



import unittest
import random
class TestTree(unittest.TestCase):
    def setUp(self):
        self.bst = BST()
        self.bst.ins(7)
        self.bst.ins(3)
        self.bst.ins(14)
        self.bst.ins(13)
        self.bst.ins(1)
        self.bst.ins(17)
        """
        self.seq = range(10)
        random.shuffle(self.seq)
        print self.seq
        for a in self.seq:
            self.bst.ins(a)
        """
 
    def testlookup(self):
        
        var = self.bst.lookup(7)
        self.assertEqual(var,True)
        var = self.bst.lookup(3)
        self.assertEqual(var,True)
        var = self.bst.lookup(14)
        self.assertEqual(var,True)
        var = self.bst.lookup(21)
        self.assertEqual(var,False)

    def testdelete0(self):
        self.bst.root= None
        try:
            self.bst.delete(1)
        except ValueError as err:
            return
        self.assertTrue(False)
        
    def testdelete1(self):
        self.setUp()
        self.bst.delete(3)
        self.bst.delete(3)
        var = self.bst.lookup(3)
        self.assertEqual(var,False)
        
    def testdelete2(self):
        self.setUp()
        self.bst.delete(3)
        var = self.bst.lookup(3)
        self.assertEqual(var,False)
        var = self.bst.lookup(1)
        self.assertEqual(var,True)

    def testdelete3(self):
        self.setUp()
        self.bst.delete(7)
        var = self.bst.lookup(7)
        self.assertEqual(var,False)
        var = self.bst.lookup(13)
        self.assertEqual(var,True)
        var = self.bst.lookup(14)
        self.assertEqual(var,True)
        var = self.bst.lookup(17)
        self.assertEqual(var,True)
        """================================================================
        print ('\n' "In Order")
        self.bst.print_In()

        print ('\n' "Pre Order")
        self.bst.print_Pre()

        print ('\n' "Post Order")
        self.bst.print_Post()
        ================================================================"""

        """
        print ('\n' "Test")
        btree = BST()
        vals = [5]
        for v in vals:
            btree.ins(v)
            tests = [8, 5]
        for t in tests:
            print "lookup(%i) = %s" % (t, ("True" if btree.lookup(t) else "False"))
        """
        
if __name__ == '__main__': unittest.main()
