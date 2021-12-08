# http://cs.stmarys.ca/~porter/csc/465/code/deitel/examples/ch17/fig17_17/Tree.java2html
'''
    Classe que representa um nó na memória
'''

class Node:
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, newData):
        self.__data = newData

    @property
    def leftChild(self):
        return self.__leftChild

    @leftChild.setter
    def leftChild(self, newLeftChild):
        self.__leftChild = newLeftChild

    @property
    def rightChild(self):
        return self.__rightChild

    @rightChild.setter
    def rightChild(self, newRightChild):
        self.__rightChild = newRightChild

    def insertLeft(self, data):
        if self.__leftChild == None:
            self.__leftChild = Node(data)	

    def insertRight(self,data):
        if self.__rightChild == None:
            self.__rightChild = Node(data)

    def __str__(self):
        return str(self.__data)

    def hasLeftChild(self):
        return self.__leftChild != None

    def hasRightChild(self):
        return self.__rightChild != None
    
    def getLeftChild(self):
        return self.__leftChild
	
    def getRightChild(self):
        return self.__rightChild
'''
    Esta classe é um exemplo de um da estrutura de Arvore Binária implementada como uma classe.
'''
class BinaryTree:
    # constructor initializes an empty Tree of integers
    def __init__(self, data_root):
        self.root = Node(data_root)
        self.cursor = self.root

    def getRoot(self):
        return self.root

    def downLeft(self):
        if(self.cursor.hasLeftChild()): 
            self.cursor = self.cursor.getLeftChild()
            return self.cursor
        else:
            return None
            
    def downRight(self):
        if(self.cursor.hasRightChild()): 
            self.cursor = self.cursor.getRightChild()
            return self.cursor
        else:
            return None

    def addLeftChild(self, dado):
        if(not self.cursor.hasLeftChild()):
            self.cursor.leftChild = Node(dado)

    def addRightChild(self, dado):
        if(not self.cursor.hasRightChild()):
            self.cursor.rightChild = Node(dado)

    def resetCursor(self):
        self.cursor = self.root

    def getCursor(self):
        return self.cursor

    def search(self, chave ):
        return self.__searchData(chave, self.root)
    
    def __searchData(self, chave, node):
        if (node == None):
            return False # Nao encontrou a chave
        if ( chave == node.getValue()):
            return True
        elif ( self.__searchData( chave, node.getLeftChild())):
            return True
        else:
            return self.__searchData( chave, node.getRightChild())

    def preorderTraversal(self):
        self.__preorder(self.root)

    def inorderTraversal(self):
        self.__inorder(self.root)

    def postorderTraversal(self):
        self.__postorder(self.root)
        
    def __preorder(self, node):
        if( node == None):
            return
        print(f'{node.data} ',end='')
        self.__preorder(node.leftChild)
        self.__preorder(node.rightChild)

    def __inorder(self, node):
        if( node == None):
            return
        self.__inorder(node.leftChild)
        print(f'{node.data} ',end='')
        self.__inorder(node.rightChild)

    def __postorder(self, node):
        if( node == None):
            return
        self.__postorder(node.leftChild)
        self.__postorder(node.rightChild)
        print(f'{node.data} ',end='')

    def deleteTree(self):
        # garbage collector will do this for us. 
        self.root = None

    # o cursor tem que estar posicionado no nó pai
    # do nó que vai ser removido
    def deleteNode(self, key):
        self.__deleteNode(self.cursor, key)


    def __deleteNode(self,root, key):

        if root is None: 
            return
        elif root.leftChild == None and root.rightChild == None:
            return
        
        if root.leftChild == None:
            if root.rightChild.data == key:
                root.rightChild = None
        elif root.rightChild == None:
            if root.leftChild.data == key:
                root.leftChild = None