from source.Arbreb import *


def main():
    a = Arbreb(6,11)
    for val in range(0, 50001,10):
        a.insert(val)
    for val in range(5,50001,10):
        a.insert(val)
        
    print("----------------Liste----------------------")
    print(a.flattenBtree())
    print("---------Hauteur de l'arbre-----------")
    print(a.height())
    print("----------------VERIFICATION ARBRE----------------------")
    print(a.root.show())
    print("----------------EST Btree?----------------------")
    print(a.is_Btree())
 
    
    print("_____________________Test 2 Suppression__________________________ ")
    for val in range(0,50001,10):
        if a.is_Btree():
            a.delete(val)
            print("----suppresion de " + str(val)+ "------------")
            print("----------------Liste----------------------")
            print(a.flattenBtree())
            print("---------Hauteur de l'arbre-----------")
            print(a.height())
            print("----------------VERIFICATION ARBRE----------------------")
            print(a.root.show())
            print("----------------EST Btree?----------------------")
            print(a.is_Btree())
            print("_______________________________________________________________________________")
            print()
            
    print("_____________________Test 2 Suppression partie 2__________________________ ")
    for val in range(5,50001,10):
        if a.is_Btree():
            a.delete(val)
            print("----suppresion de " + str(val)+ "------------")
            print("----------------Liste----------------------")
            print(a.flattenBtree())
            print("---------Hauteur de l'arbre-----------")
            print(a.height())
            print("----------------VERIFICATION ARBRE----------------------")
            print(a.root.show())
            print("----------------EST Btree?----------------------")
            print(a.is_Btree())
            print("_______________________________________________________________________________")
            print()

    


if __name__ == "__main__":
    main()