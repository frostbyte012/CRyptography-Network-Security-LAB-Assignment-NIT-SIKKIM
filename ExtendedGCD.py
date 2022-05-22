class ExtendedGCD:
    def __init__(self):
        self.number_1 = int(input("Enter the First Number"))
        self.number_2 = int(input("Enter the Second Number"))

    def extended_gcd(self,a,b):
        # Base Case
        if a == 0:
            return b, 0, 1

        gcd, x1, y1 = self.extended_gcd(b % a, a)

        # Update x and y using results of recursive
        # call
        x = y1 - (b // a) * x1
        y = x1

        return gcd, x, y


    def call_extended_gcd(self):
        a,b=self.number_1,self.number_2
        g,x,y=self.extended_gcd(a,b)
        print(a," * ",x," + ",b," * ",y," = ",g)
        print("gcd(",a,",",b,") = ",g)