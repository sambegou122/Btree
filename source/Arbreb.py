from source.Nodeb import *

class Arbreb:
    
    def __init__(self,l,u):
        self.L = l #Nombre de fils mini
        self.U = u #Nombre de fils max
        self.root = Nodeb(u,l)
        
    
    
    def insert(self,newValue):
        self.root.insertInNode(newValue)
        if self.root.parent != None:
            self.root = self.root.parent
            
    def research(self,value):
        self.root.research(value)
            
    def delete(self,value):
        self.root.delete(value)
        if len(self.root.values) == 0 and not self.root.isLeaf:
            self.root = self.root.children[0]
    
    def flattenBtree(self):
        return self.root.flatten()
        
    def height(self):
        return self.root.height()
        
    def is_Btree(self):
        l = self.flattenBtree()
        l.sort()
        return (l == self.flattenBtree()) and self.root.sameHeight()

