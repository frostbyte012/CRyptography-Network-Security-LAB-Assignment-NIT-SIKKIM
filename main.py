#Major Imports
from SetOperations import SetOperations
from CheckingDivisibleFile import DivisibleNumberFile
from SquareRootFunction import SquareRoot
from PrimeNumber import PrimeNumbers
from GreatestCommonDivisor import GCD
from ExtendedGCD import ExtendedGCD
from LeastCommonFactor import LeastCommonFactor
from AndOrXorStringProgram import AndOrXorStringProgram
from EncryptionTechniques import EncryptionDecryption

# Entering the choices
print("1. Set Operations :")
print("2. Divisible Long range :")
print("3. Square Root of the elements:")
print("4. Long Prime Number:")
print("5. The GCD of the Numbers")
print("6. The extended GCD of the Numbers")
print("7. The LCM of the Numbers")
print("8. The AND OR XOR String Program")
print("9. The Encryption and Decryption Algorithms")
choice=input("Enter your Choice : ")

#Operations of the choices
if choice == '1':
    union = SetOperations()
    print("1. Union of Two Sets:")
    print("2. Intersection of two Sets :")
    print("3. Subtraction of two Sets:")
    choice_inp=input("Enter the choice : ")
    union.enterElements()
    if choice_inp == "1":
        union.SetUnion()
    elif choice_inp == "2":
        union.IntersectionOfTwoSets()
    elif choice_inp =="3":
        union.subtractionOfTwoSets()
elif choice == '2':
    div = DivisibleNumberFile()
    div.CheckDivisibility()

elif choice == '3':
    srt = SquareRoot()
    srt.squareroot()

elif choice == '4':
    prime = PrimeNumbers()
    prime.primeNumber()

elif choice == '5':
    gcd = GCD()
    gcd.call_gcd_normal()

elif choice == '6':
    gcd = ExtendedGCD()
    gcd.call_extended_gcd()

elif choice == '7':
    LCM=LeastCommonFactor()
    LCM.call_prime_lcm()
    LCM.call_lcm_using_gcd()

elif choice == '8':
    asc=AndOrXorStringProgram()
    asc.convert_and_compute_the_string()

elif choice == '9':

    print("1. Caesar Cipher as a special a case of Affine Cipher : ")
    print("2. Vignere Cipher using Caesar Cipher as a component : ")
    print("3. Wheatstone Playfair Cipher : ")
    print("4. Polygraphic Hill Cipher :")
    print("5. Rail fence transposition Cipher")
    print("6. Row Transportation Cipher")
    print("7. One Time Pad Cipher [Verman Cipher]")

    sub_choice=input("Enter your Choice : ")

    encrypt=EncryptionDecryption()

    if sub_choice=='1':
        encrypt.call_ceasar()
    elif sub_choice=="2":
        encrypt.call_vignere_cipher()
    elif sub_choice=="3":
        encrypt.call_playfair()
    elif sub_choice=="4":
        encrypt.callHillCipher()
    elif sub_choice=="5":
        encrypt.callRailFenceCipher()
    elif sub_choice=='7':
        encrypt.callOTP()
    elif sub_choice=='6':
        encrypt.callRowTransformation()


else:
    print("Wrong Choice ! Try once again.")






