class GCD:
    def __init__(self):
        self.number_1=int(input("Enter the first Number : "))
        self.number_2=int(input("Enter the second Number : "))
        self.numbers=[self.number_2,self.number_1]

    def gcd(self):
        min_num=min(self.numbers)
        max_num=max(self.numbers)
        while True:
            if max_num % min_num == 0:
                print(f"GCD : {min_num} ")
                break
            else :
                hold=max_num
                max_num=min_num
                min_num=hold % min_num

    def gcd_normal(self,a,b):

        # Recursive function to return gcd of a and b
        # Everything divides 0
        if (a == 0):
            return b
        if (b == 0):
            return a

        # base case
        if (a == b):
            return a

        # a is greater
        if (a > b):
            return self.gcd_normal(a - b, b)
        return self.gcd_normal(a, b - a)

    def call_gcd_normal(self):

        if(self.gcd_normal(self.number_1,self.number_2)):
            print('GCD of', self.number_1, 'and', self.number_2, 'is', self.gcd_normal(self.number_1,self.number_2))
        else:
            print('GCD not found')



