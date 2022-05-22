class SetOperations:
    def __init__(self):
        self.set_one=[]
        self.set_two=[]

    def enterElements(self):
        print("Enter the elements of set 1 :\n")
        print("Enter * to terminate .\n")
        while True:
            element = input("Enter the element : ")
            if element != '*':
                self.set_one.append(element)
            else:
                break

        print("Enter the elements of set 2 :\n")
        print("Enter * to terminate .\n")
        while True:
            element = input("Enter the element : ")
            if element != '*':
                self.set_two.append(element)
            else:
                break
        self.set_one=set(self.set_one)
        self.set_two=set(self.set_two)

    def SetUnion(self):
        union_set = set(self.set_one) +set( self.set_two)
        print(union_set)

    def IntersectionOfTwoSets(self):
        set_a=set(self.set_one)
        set_b=set(self.set_two)
        if set_a & set_b:
            print(set_a & set_b)
        else:
            print("No Common Elements")

    def subtractionOfTwoSets(self):
        subtracted_set = self.set_one.difference(self.set_two)
        print(subtracted_set)

