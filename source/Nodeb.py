


class Nodeb:
    
    def __init__(self,u,l,p=None):
        self.children = []
        self.isLeaf = True
        self.values = []
        self.parent = p
        self.U = u
        self.L = l
        
#_______________________ Partie Recherce_____________________________________________  
        
    def research(self, value):
        if value in self.values:
            return True
        else:
            if not self.isLeaf:
                ind = self.whichIndex(value)
                return self.children[ind].research(value)
            else:
                return False
            
#_______________________ Partie Insertion_____________________________________________        
    #Possible amélioration recherche dichotomique/ enumerate()
    def whichIndex(self, newValue):
        i=0
        while i < len(self.values):
            if self.values[i] >= newValue:
                return i
            i+=1
        return i    
    
    def insertValues(self, newValue):
        i = self.whichIndex(newValue)
        if i == len(self.values):
            self.values.append(newValue)
        else:
            self.values.insert(i, newValue)

    def insertInNode(self, newValue):
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
        ind = self.whichIndex(newValue)
        self.values.insert(ind, newValue)
        if(len(self.values) > (self.U)-1):
            self.balance()
    
    
    def balance(self):
        newdict = self.splitNode()
        if self.parent == None:
            self.insertRoot(newdict)
        else:
            self.insertP(newdict)
        
    def insertRoot(self, newDict):
        n = Nodeb(self.U,self.L)
        n.isLeaf = False
        n.insert(newDict["Mediane"])
        n.children.append(self)
        newDict["Node"].parent = n
        n.children.append(newDict["Node"])
        self.parent = n
    
    def insertP(self, newDict):
        self.parent.isLeaf = False # utile ?
        ind = self.parent.whichIndex(newDict["Mediane"])
        if ind < len(self.parent.values):
            self.parent.children.insert(ind+1, newDict["Node"])
        else:
            self.parent.children.append(newDict["Node"])
        self.parent.insert(newDict["Mediane"])
    
    def mediane(self):
        return (len(self.values)//2)-1+(len(self.values)%2)
    
    def getMediane(self):
        return self.values[self.mediane()]
        

    def splitNode(self):
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

    def __str__(self):
        return "values "+str(self.values)+" leaf: "+ str(self.isLeaf)
    
    def __repr__(self):
        return str(self)
    
    
    
#_______________________ Partie Suppression_____________________________________________
    
    def rightNeighbor(self):
        """
        cette foncton retour son visoin droite si il existe sinon None
        """
        if  (self.parent!=None):
            index =self.parent.children.index(self)
            if index != len(self.parent.children)-1:
                return self.parent.children[index+1]
        return None
    
    def leftNeighbor(self):
        """
        cette foncton retour son visoin droite si il existe sinon None
        """
        if  (self.parent!=None):
            index =self.parent.children.index(self)
            if index!=0:
                return self.parent.children[index-1]
        return None
        
    def deteteValueInNode(self, value):
        """
        cette fonction suprime la valeur en parametre dans le noeud
        param value(int): La valeur a supprimer
        """
        ind = self.values.index(value)
        del self.values[ind]
    
    def minimunKey(self):
        """
        cette fonction retourne true si le noeud a un le nobre minimum de clef sinon false.
        param value(int): La valeur a supprimer
        """
        
        return len(self.values)<=(self.L-1)
    
    # pour feuille
            
    def addChildren(self,children, est_nd):
        """
        cette fonction rajoute des fils a un noeud
        params :
                children (NodeB) : les fils a ajouter au noeud en question
                est_nd (Bool) : ce boolen nous permet de savoir si les fils a ajouter viennent de son voisin a gauche ou a droite
                                    True ---> si il s viennent du Voisin a droite
                                    False ---> si il s viennent du Voisin a gauche
                                    NB: elle permet d'eviter de faire for unitile ou rechercher des indice pour
                                            inserer l'enfant au bon endroit. Je fais juste des addition en fonction 
        """
        for child in children:
            child.parent = self
        if est_nd:
            self.children = self.children + children
        else:
            self.children = children + self.children
            
                

    def indexChildToDeleteInparent(self, est_nd, i):
        """
        cette fonction donne l'index du voisin a supprimer
        params :
                i : l'indice du noeud dans la liste de fils de son parent
                est_nd (Bool) : ce boolen nous permet de savoir si il faut supprimer son voisin a gauche ou a droite
                                    True ---> suppression de son voisin a droite
                                    False ---> suppression de son voisin a gauche
        NB: cette fonction est utiliser que dans le cas on veut supprimer un voisin au moment de la fussion
        """
        if est_nd:
            return i+1
        else:
            return i-1
        
    def indexValueToDeleteInparent(self, est_nd , i):
        """
        cette fonction renvoie l'index de la valeur a supprimer dans le noeud
        params :
                i : l'indice du noeud dans la liste des fils de son parent
                est_nd (Bool) : ce boolen nous permet de la valeur a supprimer
        NB: cette fonction est utiliser que dans le cas on veut suprimer une valeur au moment de la fussion
        """
        if est_nd:
            return i
        else:
            return i-1
    
    def mergeInNode(self, neighbor,est_nd):
        """
        cette fonction ajoute les fils et les valeurs de son voisin au noeud et les supprime de l'arbre en meme temps
        params :
                ind : l'indice du noeud dans la liste des fils de son parent
                est_nd (Bool) : ce boolen nous permet de la valeur a supprimer
                voisin (Nodeb) : le voisin a supprimer lors de la la fussion
        NB: cette fonction est utiliser si le noeud qu'on fussione est un noeud interne
        """
        self.addChildren(neighbor.children,est_nd)
        for val in neighbor.values:
            self.insertValues(val)
        while len(neighbor.children)>0:
            neighbor.children.pop()
        while len(neighbor.values)>0:
            neighbor.values.pop() 
    
            
            
    def mergeInLeaf(self, neighbor ,value):
        """
        cette fonction ajoute les valeurs de son voisin au noeud et le supprime de l'arbre en meme temps
        params :
                ind : l'indice du noeud dans la liste des fils de son parent
                est_nd (Bool) : ce boolen nous permet de la valeur a supprimer
                voisin (Nodeb) : le voisin a supprimer lors de la fussion
                value (int): la valeur a supprimer
        NB: cette fonction est utiliser si le noeud qu'on fussione est une feuille
        """
        if self.parent !=None:
            for i in neighbor.values:
                self.insertValues(i)
            self.deteteValueInNode(value)
            
    def merge(self, neighbor, est_nd,value):
        """
        cette fonction fais la fussion en faisant un merge ou un arrange
        params :
                ind : l'indice du noeud dans la liste des fils de son parent
                est_nd (Bool) : ce boolen nous permet de la valeur a supprimer
                voisin (Nodeb) : le voisin a supprimer lors de la fussion
                value (int) : valeur a supprimer
        NB: La fonction principale de la fusion
        """
        
        print("merge")
        ind = self.parent.children.index(self)
        if(self.isLeaf):
            self.mergeInLeaf(neighbor, value)
        else:
            self.mergeInNode(neighbor, est_nd)
        v = self.parent.values[self.indexValueToDeleteInparent(est_nd,ind)]
        self.insertValues(v)
        del self.parent.children[self.indexChildToDeleteInparent(est_nd,ind)] 
        del self.parent.values[self.indexValueToDeleteInparent(est_nd,ind)]
        dic = self.parent.getThePossibleCase()
        cas = dic["Cas"]
        if self.parent!=None and len(self.parent.values)<self.L-1 and cas!=0:
            val = None
            self.parent.merge(dic["Node"],dic["droite"],val)     

    def rotation(self,neighbor,est_nd,value):
        """
        cette fonction fais la rotation à gauche ou a droite
        params :
                est_nd (Bool) : ce boolen nous permet de savoir de quel côté on fais la rotation 
                voisin (Nodeb) : le voisin avec le quel on fais la rotation
                value (int) : valeur a supprimer
        """
        if (not est_nd):
            print("rotation gauche")
            ind = self.parent.children.index(neighbor)
            vf = neighbor.values.pop()

        else:
            print("rotation droite")
            ind = self.parent.children.index(self)
            vf = neighbor.values.pop(0)
        self.deteteValueInNode(value)
        vp = self.parent.values[ind]
        self.parent.insertValues(vf)
        self.parent.deteteValueInNode(vp)
        self.insertValues(vp)

    def getThePossibleCase(self):
        """
        cette fonction est tres inportante car c'est grace a elle on sait ce qu'il faut faire.
        Elle retourne une structe (dictonnaire) qui contien un voisin un cas et
        un boolen qui permet de savoir de quel côte on fais les choses
        
        """
        vg = self.leftNeighbor() # on recupere le voisin a gauche
        vd = self.rightNeighbor() # on recupere le voisin a droite
        if vg == None and vd == None:
            return {"Node":vd ,"Cas":0, "droite":False} # cas 0: on n'est a la racine
        else:
            if vg!= None and not vg.minimunKey():
                return {"Node":vg ,"Cas":1, "droite":False} #cas 1: Pour faire la rotation a gauche
            elif vd!= None and not vd.minimunKey():
                return {"Node":vd ,"Cas":1, "droite":True} #cas 1: Pour faire la rotation a droite
            else:
                if vg == None:
                    return {"Node":vd ,"Cas":2, "droite":True} #cas 2: Pour faire la fussion a droite
                return {"Node":vg ,"Cas":2, "droite":False} #cas 2: Pour faire la fussion a gauche
                    
    def applyTheCase(self,cas,value,voisin, est_nd):
        """
        cette fonction applique une fonction pour chacun des cas possible
        
        """
        if cas ==0:
            if self.isLeaf:
                self.deteteValueInNode(value)
        elif cas ==1:
            self.rotation(voisin,est_nd,value)
        else:
            self.merge(voisin,est_nd,value)
            
            
    def deleteInLeaf(self, value):
        """
         fonction de suppression dans une feuille
         param: value ---> valeur a supprimer
        """
        print("delete feuille")
        dic = self.getThePossibleCase()
        if self.minimunKey():
            self.applyTheCase(dic["Cas"],value,dic["Node"], dic["droite"])
                  
        else:
            self.deteteValueInNode(value)
                
    def deleteInNode(self, value):
        """
         fonction de suppression dans un noeud interne ou dans une racine
         param: value ---> valeur a supprimer
        """
        ind =  self.values.index(value)
        if ind == len(self.values):
            child = self.children[ind]
        else:
            child = self.children[ind+1]
        while (not child.isLeaf):
            child = child.children[0] 
        self.values[ind]=child.values[0]
        child.values[0]=value
        child.deleteInLeaf(value)
    
    def delete(self, value):
        """
         fonction de suppression principale
         param: value ---> valeur a supprimer
        """
        if self.research(value):
            if (value in self.values):
                if self.isLeaf:
                    self.deleteInLeaf(value)
                else:
                    self.deleteInNode(value)      
            else:
                ind =  self.whichIndex(value)
                self.children[ind].delete(value)
    
    def flatten(self):
        """
         fonction retourne la liste du noeud applatit
        """
        l =[]
        if self.isLeaf:
            return self.values
        for i in range(len(self.children)):
            if not self.children[i] is None:
                l+=self.children[i].flatten()
            if i <len(self.values):
                l.append(self.values[i])
        return l
    
    def height(self):
        l = []
        if self.isLeaf:
            l.append(0)
        for i in range(0,len(self.children)):
            l.append(1 + self.children[i].height())
        return max(l)
    
    def sameHeight(self):
        eq = []
        for child in self.children:
            if not child is None:
                eq.append(child.height())
        return all(l==eq[0] for l in eq)
        

#_______________________ Partie Affichage_____________________________________________  
                
    def show(self):
        if self.isLeaf and self!=None:
            print(self)
        else:
            print(self)
            for child in self.children:
                if child !=None:
                    child.show()
                
        
 
    
    
    
    
    
    
    
    
    
    
    
    
