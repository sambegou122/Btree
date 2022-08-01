from Nodeb import *

class Arbreb:
    
    def __init__(self,l,u):
        self.L = l #Nombre de fils mini
        self.U = u #Nombre de fils max
        self.root = Nodeb(u,l)
        
    
    
    def insert(self,newValue):
        self.root.insertInNode(newValue)
        if self.root.parent != None:
            self.root = self.root.parent
            
    def delete(self, value):
        v= self.root.deleteValueInTree(value)
        if len(self.root.values) == 0 and len(self.root.children) != 0:
            self.root = self.root.children[0]
            self.root.parent = None
        return v
    
    def printTree(self, node):
        print(node)
        for child in node.children:
            self.printTree(child)
    
    def listValueTree(self, node, l):
        for i in range(len(node.values)):
            if not node.isLeaf:
                self.listValueTree(node.children[i],l)
            l.append(node.values[i])
        if not node.isLeaf:
            self.listValueTree(node.children[len(node.children)-1],l)
                
def main():
    a = Arbreb(3,5)
    for i in range (1,8):
        a.insert(i*5)
        
    print("----------------VERIFICATION ARBRE----------------------")
    a.printTree(a.root)
    print("---------------TEST RECHERCHE---------------------")
    print(a.root.research(10))
    print(a.root.research(15))
    print(a.root.research(35))
    print(a.root.research(8))
    print("---------------TEST SUPPRESSION-------------------")
    for i in range(1,8):
        a.insert(i+35)
    print("---------------ARBRE ACTUEL-----------------------")
    a.printTree(a.root)
    
    print("---------------SUPPRESSION-----------------------")
    
    print("-suppr 39-")
    a.delete(39)
    a.printTree(a.root)
    print("-suppr 40-")
    a.delete(40)
    a.printTree(a.root)
    print("-suppr 42-")
    a.delete(42)
    a.printTree(a.root)
    print("-suppr 37-")
    a.delete(37)
    a.printTree(a.root)
    print("-suppr 35-")
    a.delete(35)
    a.printTree(a.root)
    print("-suppr 10-")
    a.delete(10)
    a.printTree(a.root)
    print("-suppr 25-")
    a.delete(25)
    a.printTree(a.root)
    print("-suppr 5-")
    a.delete(5)
    a.printTree(a.root)
    print("-suppr 15-")
    a.delete(15)
    a.printTree(a.root)
    print("-suppr 30-")
    a.delete(30)
    a.printTree(a.root)
    print("-suppr 38-")
    a.delete(38)
    a.printTree(a.root)
    print("-suppr 20-")
    a.delete(20)
    a.printTree(a.root)
    print("-suppr 36-")
    a.delete(36)
    a.printTree(a.root)
    print("-suppr 41-")
    a.delete(41)
    a.printTree(a.root)
    
    print("###############################")
    print("###### BATTERIE DE TEST #########")
    print("###############################")
    
    print("########### BATTERIE 1 ###################")
    arbret = Arbreb(2,3)
    for i in range(2,36,2):
        arbret.insert(i)
    arbret.printTree(arbret.root)
    arbret.insert(7)
    arbret.insert(9)
    arbret.insert(11)
    arbret.insert(13)
    
    arbret.delete(14)
    arbret.delete(10)
    arbret.delete(20)
    arbret.delete(18)
    arbret.delete(16)
    arbret.delete(24)
    
    arbret.delete(6)
    print("########### BATTERIE 2 ###################")
    
    arbreb = Arbreb(6,11)
    l= []
    for i in range(10,5001,5):
        l.append(i)
    for v in l:
        
        arbreb.insert(v)
        l1 = []
        l2 = []
        arbreb.listValueTree(arbreb.root,l1)
        arbreb.listValueTree(arbreb.root,l2)
        l2.sort()
        for j in range(len(l1)):
            if l1[j] != l2[j]:
                return False
            
    arbreb.printTree(arbreb.root)
    for i in l:
        arbreb.delete(i)
        l1 = []
        l2 = []
        arbreb.listValueTree(arbreb.root,l1)
        arbreb.listValueTree(arbreb.root,l2)
        l2.sort()
        
        for j in range(len(l1)):
            if l1[j] != l2[j]:
                print("#######################################")
                arbreb.printTree(arbreb.root)
                return False
    print("########################################")
    
    
    arbreb.printTree(arbreb.root)
    
    
if __name__ == "__main__":
    main()