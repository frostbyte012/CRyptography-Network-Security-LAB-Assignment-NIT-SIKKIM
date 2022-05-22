class PrimeNumbers:
    '''
    Here we use the class to initialize the elements
    by def __init__(self)
    :var used
    number: to get and initialize the elements using the pytho
    '''
    def __init__(self):
        self.number=int(input("Enter the Number : "))

    def primeNumber(self):
        # if self.number % 10 == 0 or self.number % 10 == 2 or self.number % 10 == 4 or self.number % 10 == 6 or self.number % 10 == 8:
        #     print(f"{self.number} is not a prime number")
        # else:
        #     if self.getSum(self.number) % 3 == 0:
        #         print(f"{self.number} is not a prime number")
        #     else:
        #         sqr=math.sqrt(self.number)
        #         for r in range(2,sqr):


        if self.number == 0 or self.number == 1:
            print(f"{self.number} is not a prime number")
            return 0

        for num in range(1,int(self.number/2) + 1):
            if self.number % num == 0:
               print(f"{self.number} is not a prime number")
               break
        else:
            print(f"{self.number} is not a prime number")

    def getSum(self,num):
        sum=0
        for digit in str(num):
            sum=sum+int(digit)
        return sum
