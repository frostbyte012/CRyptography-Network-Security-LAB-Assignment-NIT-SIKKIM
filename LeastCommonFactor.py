# Python3 program to find prime factors
# of LCM of array elements
import math
class LeastCommonFactor:
    def __init__(self):
        self.MAX = 10000
        self.number_1=int(input("Enter the first number : "))
        self.number_2=int(input("Enter the second number : "))
        # array to store all prime less than
        # and equal to 10^6
        self.primes = []

        # utility function for sieve of sundaram
    def sieve(self):

        n = self.MAX

        # In general Sieve of Sundaram, produces
        # primes smaller than (2*x + 2) for a
        # number given number x. Since we want
        # primes smaller than n, we reduce n to half
        nNew = int(n / 2)

        # This array is used to separate numbers of
        # the form i+j+2ij from others where 1 <= i <= j
        marked = [False] * (nNew + 100)

        # Main logic of Sundaram. Mark all numbers
        # which do not generate prime number by
        # doing 2*i+1
        tmp = int(math.sqrt(n))
        for i in range(1, int((tmp - 1) / 2) + 1):
            for j in range((i * (i + 1)) << 1,nNew + 1, 2 * i + 1):
                marked[j] = True

            # Since 2 is a prime number
        self.primes.append(2)

        # Print other primes. Remaining primes
        # are of the form 2*i + 1 such that
        # marked[i] is false.
        for i in range(1, nNew + 1):
            if (marked[i] == False):
                self.primes.append(2 * i + 1)

        # Function to find prime factors of
        # n elements of given array
    def primeLcm(self,arr, n):

        # factors[] --> array to mark all prime
        # factors of lcm of array elements
        factors = [0] * (self.MAX)

        # One by one calculate prime factors of
        # number and mark them in factors[] array
        for i in range(n):

            # copy --> duplicate of original
            # element to perform operation
            copy = arr[i]

            # sqr --> square root of current number
            # 'copy' because all prime factors are
            # always less than and equal to square
            # root of given number
            sqr = int(math.sqrt(copy))

            # check divisibility with prime factor
            j = 0
            while (self.primes[j] <= sqr):

                    # if current prime number is
                    # factor of 'copy'
                    if (copy % self.primes[j] == 0):

                        # divide with current prime factor
                        # until it can divide the number
                        while (copy % self.primes[j] == 0):
                            copy = int(copy / self.primes[j])

                        # mark current prime factor as 1
                        # in factors[] array
                        factors[self.primes[j]] = 1
                    j = j + 1


            if (copy > 1):
                factors[copy] = 1

            # if 2 is prime factor of lcm of
            # all elements in given array
            if (factors[2] == 1):
                print("2 ", end="")

            # traverse to print all prime factors of
            # lcm of all elements in given array
            for i in range(3, self.MAX + 1, 2):
                if (factors[i] == 1):
                    print(i, end=" ")


    def call_prime_lcm(self):
        # Driver Code
        self.sieve()
        arr = [self.number_1,self.number_2]
        n = len(arr)
        self.primeLcm(arr, n)

        # This code is contributed by chandan_jnu

    def gcd(self,a,b):
        if a == 0:
            return b
        return self.gcd(b % a,a)


    def lcm_using_gcd(self):
        return (self.number_1/self.gcd(self.number_1,self.number_2))*self.number_2


    def call_lcm_using_gcd(self):
        print("\nThe LCM of the Numbers : ",self.lcm_using_gcd())