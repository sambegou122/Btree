from source.Arbreb import *

def main():
    liste = [2, 4, 5, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 7, 9, 11, 13]
    sup = [14, 10, 20, 18, 16, 24, 6]
    a = Arbreb(2,3)
    for val in liste:
        a.insert(val)
    print("----------------Liste----------------------")
    print(a.flattenBtree())
    print("---------Hauteur de l'arbre-----------")
    print(a.height())
    print("----------------VERIFICATION ARBRE----------------------")
    print(a.root.show())
    print("----------------EST Btree?----------------------")
    print(a.is_Btree())
        

    for val in sup:
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
        print("______________________________________________________________________________")
        print()



if __name__ == "__main__":
    main()
