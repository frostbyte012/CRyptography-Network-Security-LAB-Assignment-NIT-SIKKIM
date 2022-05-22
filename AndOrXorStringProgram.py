class AndOrXorStringProgram:

    def __init__(self):
        self.string=input("Enter the string : ")
        self.characterString=[]
        self.ASCIIString=[]
        self.ANDListZero=[]
        self.ORListZero=[]
        self.XORListZero=[]
        self.XORList127=[]
        self.ORList127=[]
        self.ANDList127=[]

    def convert_and_compute_the_string(self):

        for str in self.string:
            self.characterString.append(str)
            self.ASCIIString.append(ord(str))

        for ele in self.ASCIIString:
            self.ANDListZero.append(ele & 0)
            self.ORListZero.append(ele | 0)
            self.XORListZero.append(ele ^ 0)
            self.ANDList127.append(ele & 127)
            self.ORList127.append(ele | 127)
            self.XORList127.append(ele ^ 127)


        print("The Characters",self.characterString)
        print("The ASCII Sets",self.ASCIIString)
        print("The AND Operation with Zero : ",self.ANDListZero)
        print("The OR Operation with Zero : ",self.ORListZero)
        print("The XOR Operation with Zero : ",self.XORListZero)
        print("The AND Operation with 127 : ",self.ANDList127)
        print("The OR Operation with 127 : ",self.ORList127)
        print("The XOR Operation with 127 : ",self.XORList127)



