class Nodeb:
    
    def __init__(self,u,l,p=None):
        self.children = []
        self.isLeaf = True
        self.values = []
        self.parent = p
        self.U = u
        self.L = l
        
    
    def research(self, value):
        """
    This function search the value given in parameter if the value in tree return, else false
    :param value: (int)
    :return: (boolean)
    
    CU: none
    
    Exemple:
    >>> n = Nodeb(1,2)
    >>> n.values.append(10)
    >>> n.research(10)
    True
    >>> n.research(2)
    False
    """
        ind = self.whichIndex(value)
        if value in self.values:
            return True
        else:
            if self.isLeaf:
                return False
            
            return self.children[ind].research(value)
        
    
    def whichIndex(self, newValue):
        """
    This function return the index where should be the value given in parameter
    :param newValue: (int)
    :return: (int)
    
    CU: none
    
    Exemple:
    
    >>> n = Nodeb(1,2)
    >>> n.values.append(10)
    >>> n.whichIndex(12)
    1
    """
        i=0
        while i < len(self.values):
            if self.values[i] >= newValue:
                return i
            i+=1
        return i    
    
    # FONCTION INSERTION
    
    def insertValues(self, newValue):
        """
    The function insertValues will take the value in parameter and put it in node values.
    :param newValue: (int)
    
    CU: none
    
    Exemple:
    >>> n = Nodeb(1,2)
    >>> n.values.append(10)
    >>> n.insertValues(12)
    >>> n.values == [10,12]
    True
    >>> n.insertValues(11)
    >>> n.values == [10,11,12]
    True
    """
        i = self.whichIndex(newValue)
        if i == len(self.values):
            self.values.append(newValue)
        else:
            self.values.insert(i, newValue)
    
    
    
    def insertInNode(self, newValue):
        """
    The function will take the new value given in parameter and will make recursive function while we are not in leaf.
    When we are in leaf we will call the function insert.
    :param newValue: (int)
    
    CU: none
    
    Exemple:
    >>> n = Nodeb(4, 2)
    >>> child1 = Nodeb(4, 2, n)
    >>> child2 = Nodeb(4, 2, n)
    >>> child3 = Nodeb(4, 2, n)
    >>> n.values.append(10)
    >>> n.values.append(12)
    >>> n.isLeaf = False
    >>> child1.values.append(8)
    >>> child1.values.append(9)
    >>> child2.values.append(11)
    >>> child3.values.append(13)
    >>> child3.values.append(14)
    >>> n.children.append(child1)
    >>> n.children.append(child2)
    >>> n.children.append(child3)
    >>> n.insertInNode(7)
    >>> n.insertInNode(15)
    
    >>> n.values
    [10, 12]
    >>> child1.values
    [7, 8, 9]

    >>> child3.values
    [13, 14, 15]
    """
        t = len(self.values)-1
        if self.isLeaf != True:
            if self.values[t] < newValue :
                self.children[len(self.children)-1].insertInNode(newValue)
            else :
                i = self.whichIndex(newValue)
                self.children[i].insertInNode(newValue)
        else :
            self.insert(newValue)
    
    
    def insert(self, newValue):
        """
    The function insert the new value given in parameter in values, if the maximum number is reached then we balance
    :param newValue: (int)
    
    CU: none
    
    Exemple:
    
    >>> n = Nodeb(3, 1)
    >>> n.values.append(10)
    >>> n.insert(8)
    >>> n.values
    [8, 10]
    >>> n.insert(12)
    >>> n.values
    [8]
    >>> n.parent.values
    [10]
    >>> n.parent.children[1].values
    [12]
    """
        ind = self.whichIndex(newValue)
        self.values.insert(ind, newValue)
        if(len(self.values) > (self.U)-1):
            self.balance()
    
    
    def balance(self):
        """
    The function balance the node which has reached the maximum number of value
    
    CU: none
    
    Exemple:
    >>> n = Nodeb(3,1)
    >>> n.values.append(8)
    >>> n.values.append(10)
    >>> n.values.append(12)
    >>> n.balance()
    >>> n.values
    [8]
    >>> n.parent.values
    [10]
    >>> n.parent.children[1].values
    [12]
    >>> n.values.append(9)
    >>> n.values.append(9.5)
    >>> n.balance()
    >>> n.parent.values
    [9, 10]
    >>> n.parent.children[1].values
    [9.5]
    >>> n.values
    [8]
    """
        newdict = self.splitNode()
        if self.parent == None:
            self.insertRoot(newdict)
        else:
            self.insertP(newdict)
    
    
    def insertRoot(self, newDict):
        """
    This function is used after insert and when balance is in root. Doctest is in Balance as first case.
    """
        n = Nodeb(self.U,self.L)
        n.isLeaf = False
        n.insert(newDict["Mediane"][0])
        n.children.append(self)
        newDict["Node"].parent = n
        n.children.append(newDict["Node"])
        self.parent = n
    
    def insertP(self, newDict):
        """
    This function is used after insert and when balance is not in root. Doctest is in Balance as second case.
    """
        self.parent.isLeaf = False
        ind = self.parent.whichIndex(newDict["Mediane"][0])
        if ind < len(self.parent.values):
            self.parent.children.insert(ind+1, newDict["Node"])
        else:
            self.parent.children.append(newDict["Node"])
        self.parent.insert(newDict["Mediane"][0])
    
    def mediane(self):
        """
    Give middle index in a values.
    
    CU: none
    
    Exemple:
    >>> n = Nodeb(5,1)
    >>> n.values = [1,2,3,4]
    >>> n.mediane()
    1
    """
        return (len(self.values)//2)-1+(len(self.values)%2)
    
    def getMediane(self):
        """
    Give middle number in a values.
    
    CU: none
    
    Exemple:
    >>> n = Nodeb(5,1)
    >>> n.values = [1,2,3,4]
    >>> n.getMediane()
    [2]
    """
        return [self.values[self.mediane()]]
        

    def splitNode(self):
        """
    This function split the actual node in half, create and new one with the value and children which are removed from the actual
    and return a dictionnary with the new Node and mediane.
    
    :return: (dictionnary) {"Node":Node, "Mediane":int}
    
    CU: none
    
    Exemple:
    
    >>> n = Nodeb(5,1)
    >>> n.values = [1,2,3,4]
    >>> d = n.splitNode()
    >>> d["Node"].values
    [3, 4]
    >>> d["Mediane"]
    [2]
    >>> n.values
    [1]
    
    """
        m = self.getMediane()
        n = Nodeb(self.U,self.L,self.parent)
        n.isLeaf = self.isLeaf
        i = self.mediane()
        del self.values[i]
        
        while len(self.values) > i:
            n.values.append(self.values[i])            
            del self.values[i]
        if(self.isLeaf != True):
            while len(self.children) > i+1:
                self.children[i+1].parent = n
                n.children.append(self.children[i+1])
                del self.children[i+1]
        
        return { "Node":n ,"Mediane":m}
    
    
    # FONCTION POUR LA SUPPRESSION
    
    def deleteValueInTree(self, value):
        """
    The function delete the value given in parameter, return a String if the value not in node else call deleteValue.
    Check deleteValue documentation.
    
    :param value:(int)
    
    CU: value in Node
    >>> n = Nodeb(4,1)
    >>> n.values.append(10)
    >>> n.deleteValueInTree(9)
    'Value 9 not in tree'
    """
        if(self.research(value) == False):
            return "Value " + str(value) + " not in tree" 
        else:
            return self.deleteValue(value)
                
                

    def deleteValue(self,value):
        """
    The following function will take the value given in parameter, after check if the value is not in values and if is not a leaf, in this case
    we will call by recurisvity the fonction in the children at the index i given by whichIndex. Else if node is a leaf we will call the function
    delete (check documentation of delete) else calling deleteAsNode (check documentation). At the end, if the node is not a leaf we call the function
    balanceOnDel (check documentation)
    """
        i = self.whichIndex(value)
        if value not in self.values and not self.isLeaf:
            self.children[i].deleteValue(value)
        else:
            if(self.isLeaf):
                self.delete(value)
            else:
                self.deleteAsNode(value,i)
        if self.isLeaf == False:
            self.balanceOnDel(i)
        
    # Fonction partie feuille
    
    def delete(self,value):
        """
    Delete the value given in parameter in node.
    :param value:(int)
    
    CU: none
    
    Exemple:
    >>> n = Nodeb(4,2)
    >>> n.values = [1,2,3]
    >>> n.delete(2)
    >>> n.values
    [1, 3]
    """
        i = self.whichIndex(value)
        self.values.pop(i)
    
    def deleteAsNode(self, value, index):
        """
    The functions is started where the value is in non leaf node, to delete the value we will swap with the function (swapFromLeft/swapFromRight)
    If the children is a leaf we call the function delete, else deleteValue. Balance the node at the end.
    :param value: (int)
    :param index: (int)
    
    CU: none
    
    Exemple:
    >>> n = Nodeb(4, 2)
    >>> child1 = Nodeb(4, 2, n)
    >>> child2 = Nodeb(4, 2, n)
    >>> child3 = Nodeb(4, 2, n)
    >>> n.values.append(10)
    >>> n.values.append(12)
    >>> n.isLeaf = False
    >>> child1.values.append(8)
    >>> child1.values.append(9)
    >>> child2.values.append(11)
    >>> child3.values.append(13)
    >>> child3.values.append(14)
    >>> n.children.append(child1)
    >>> n.children.append(child2)
    >>> n.children.append(child3)
    >>> n.deleteAsNode(10,0)
    >>> n.values
    [12]
    >>> n.children[0].values
    [8, 9, 11]
    >>> n.children[1].values
    [13, 14]
    """
        p = self.values.pop(index)
        i = self.whichIndex(value)
        if i !=0:
            newIndex = i
            v = self.children[newIndex].swapFromLeft(value)
            self.values.insert(i,v)
        else:
            newIndex = i+1
            v = self.children[newIndex].swapFromRight(value)
            self.values.insert(i,v)
            
        if self.isLeaf == False:
            if (self.children[newIndex].isLeaf == True):
                self.children[newIndex].delete(value)
            else:
                self.children[newIndex].deleteValue(value)
            self.balanceOnDel(newIndex)
    
    
    def swapFromLeft(self, value):
        """
    The function will return the maximum value from the left branch. Before returning the value given in parameter will replace the recent value.
    If we are not in leaf he call recursively the function on the right branch.
    :param value:(int)
    
    CU: none
    
    Exemple:
    >>> n = Nodeb(4, 2)
    >>> child1 = Nodeb(4, 2, n)
    >>> child2 = Nodeb(4, 2, n)
    >>> child3 = Nodeb(4, 2, n)
    >>> n.values.append(10)
    >>> n.values.append(12)
    >>> n.isLeaf = False
    >>> child1.values.append(8)
    >>> child1.values.append(9)
    >>> child2.values.append(11)
    >>> child3.values.append(13)
    >>> child3.values.append(14)
    >>> n.children.append(child1)
    >>> n.children.append(child2)
    >>> n.children.append(child3)
    >>> n.swapFromLeft(10)
    14
    >>> n.children[2].values[1]
    10
    """
        if self.isLeaf:
            res = self.values.pop()
            self.values.append(value)
            return res
        else:
            return self.children[len(self.children)-1].swapFromLeft(value)
        
    def swapFromRight(self, value):
        """
    The function will return the minimum value from the right branch. Before returning the value given in parameter will replace the recent value.
    If we are not in leaf he call recursively the function on the left branch.
    :param value:(int)
    
    CU: none
    
    Exemple:
    >>> n = Nodeb(4, 2)
    >>> child1 = Nodeb(4, 2, n)
    >>> child2 = Nodeb(4, 2, n)
    >>> child3 = Nodeb(4, 2, n)
    >>> n.values.append(10)
    >>> n.values.append(12)
    >>> n.isLeaf = False
    >>> child1.values.append(8)
    >>> child1.values.append(9)
    >>> child2.values.append(11)
    >>> child3.values.append(13)
    >>> child3.values.append(14)
    >>> n.children.append(child1)
    >>> n.children.append(child2)
    >>> n.children.append(child3)
    >>> n.swapFromRight(10)
    8
    >>> n.children[0].values[0]
    10
    """
        if self.isLeaf:
            res = self.values.pop(0)
            self.values.insert(0,value)
            return res
        else:
            return self.children[0].swapFromRight(value)
    
    def balanceOnDel(self, index):
        """
    This function is used to find which case we have to use for balancing after deletion. If we can take from left neighboor we are calling
    balancingFromLeft, else if we can take from right we call balancingFromRight, else we merge.
    :param index:(int)
    
    CU: none
    
    For exemple check the different documentation.
    """
        if len(self.children[index].values) < self.L :
            if(index !=0 and len(self.children[index-1].values) > self.L):
                self.balancingFromLeft(index)
            elif (index != len(self.values) and len(self.children[index+1].values) > self.L):
                self.balancingFromRight(index)
            else:
                self.merge(index)
    
    def balancingFromLeft(self, index):
        """
    BalancingFromLeft is used when we can take a value from left neighboor. It means the value  at index given in parameter will replace
    the deleted value from children and the value from left will replace the value.
    :param index:(int)
    
    CU: none
    
    Exemple:
    >>> n = Nodeb(4, 2)
    >>> child1 = Nodeb(4, 2, n)
    >>> child2 = Nodeb(4, 2, n)
    >>> child3 = Nodeb(4, 2, n)
    >>> n.values.append(10)
    >>> n.values.append(12)
    >>> n.isLeaf = False
    >>> child1.values.append(8)
    >>> child1.values.append(9)
    >>> n.children.append(child1)
    >>> n.children.append(child2)
    >>> n.children.append(child3)
    >>> n.balancingFromLeft(1)
    >>> n.children[1].values
    [10]
    >>> n.values
    [9, 12]
    """
        value = self.values[index-1]
        self.children[index].values.append(value)
        newValueForP = self.children[index-1].values[(len(self.children[index-1].values)-1)]
        self.values.insert(index, newValueForP)
        if not self.children[index].isLeaf:
            np = self.children[index-1].children.pop()
            np.parent = self.children[index]
            self.children[index].children.insert(0, np)
        del self.children[index-1].values[(len(self.children[index-1].values)-1)]
        del self.values[index-1]
        
        
    def balancingFromRight(self, index):
        """
    BalancingFromRight is used when we can take a value from right neighboor. It means the value at index given in parameter will replace
    the deleted value from children and the value from right will replace the value.
    
    :param index:(int)
    
    CU: none
    
    Exemple:
    >>> n = Nodeb(4, 2)
    >>> child1 = Nodeb(4, 2, n)
    >>> child2 = Nodeb(4, 2, n)
    >>> child3 = Nodeb(4, 2, n)
    >>> n.values.append(10)
    >>> n.values.append(12)
    >>> n.isLeaf = False
    >>> child1.values.append(8)
    >>> child1.values.append(9)
    >>> child2.values.append(11)
    >>> child3.values.append(13)
    >>> child3.values.append(14)
    >>> n.children.append(child1)
    >>> n.children.append(child2)
    >>> n.children.append(child3)
    >>> n.balancingFromRight(1)
    >>> n.children[1].values
    [11, 12]
    >>> n.values
    [10, 13]
    """
        value = self.values[index]
        self.children[index].values.append(value)
        newValueForP = self.children[index+1].values[0]
        self.values.insert(index, newValueForP)
        if not self.children[index].isLeaf:
            np = self.children[index+1].children.pop(0)
            np.parent = self.children[index]
            self.children[index].children.insert(len(self.children[index].children), np)
        del self.children[index+1].values[0]
        del self.values[index+1]
        
    
    def merge(self, index):
        """
    The function merge is used when we can't balance from left or right, the process of merge is taking the child at index given in parameter,
    Putting value from the child at the neighboor (depending if index is 0 or not). And putting the other value and children if needed in the node.
    :param index:(int)
    
    CU: none
    
    Exemple:
    >>> n = Nodeb(4, 2)
    >>> child1 = Nodeb(4, 2, n)
    >>> child2 = Nodeb(4, 2, n)
    >>> child3 = Nodeb(4, 2, n)
    >>> n.values.append(10)
    >>> n.values.append(12)
    >>> n.isLeaf = False
    >>> child1.values.append(8)
    >>> child1.values.append(9)
    >>> child2.values.append(11)
    >>> child3.values.append(13)
    >>> child3.values.append(14)
    >>> n.children.append(child1)
    >>> n.children.append(child2)
    >>> n.children.append(child3)
    >>> n.merge(1)
    >>> n.values
    [12]
    >>> n.children[0].values
    [8, 9, 10, 11]
    """
        if index != 0:
            p = self.children.pop(index)
            self.children[index-1].values.append(self.values.pop(index-1))
            for value in p.values:
                self.children[index-1].values.append(value)
            for child in p.children:
                self.children[index-1].children.append(child)
        else:
            self.children[index].values.append(self.values.pop(index))
            if len(self.values) < len(self.children) :
                p = self.children.pop(index+1)
                for value in p.values:
                    self.children[index].values.append(value)
                for child in p.children:
                    self.children[index].children.append(child)
            
    
    
    
    
        
    

    def __str__(self):
        return "values "+str(self.values)+" leaf: "+ str(self.isLeaf)
    
    def __repr__(self):
        return str(self)        
    
    
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose= True)
    

    