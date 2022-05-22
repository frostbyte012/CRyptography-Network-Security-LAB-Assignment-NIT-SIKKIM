import numpy as np
import string
import random
import sys
import math

class EncryptionDecryption:

    def __init__(self):
        self.text=input("Enter The Text : ")
        self.result=''
        self.playfairkey=''
        self.playfairmessage=''
        self.en_m=''
        self.abc = string.ascii_lowercase
        self.one_time_pad = list(self.abc)
        self.ROTkey=''

        # random.shuffle(one_time_pad)

        self.help = """Synopsis: otp.py -e|-d
        -e encrypt
        -d decrypt """

    def ceasar_encrypt(self,text,s):
        # traverse text
        for i in range(len(text)):
            char = text[i]

            # Encrypt uppercase characters
            if (char.isupper()):
                self.result += chr((ord(char) + s - 65) % 26 + 65)

            # Encrypt lowercase characters
            else:
                self.result += chr((ord(char) + s - 97) % 26 + 97)

        return self.result   #WROTE TILL HERE !

    def call_ceasar(self):
        s = int(input("Enter the shift [ note enter the number between 0 to 25 ]"))
        print("The Encrypted text: ")
        print(self.ceasar_encrypt(self.text,s))


    def generateKey(self,string, key):
        key = list(key)
        if len(string) == len(key):
            return (key)
        else:
            for i in range(len(string) - len(key)):
                key.append(key[i % len(key)])
            return ("".join(key))

        # This function returns the
        # encrypted text generated
        # with the help of the key
    def vignereCipherText(self,string, key):
        cipher_text = []
        for i in range(len(string)):
            x = (ord(string[i]) + ord(key[i])) % 26
            x += ord('A')
            cipher_text.append(chr(x))
        return ("".join(cipher_text))

    # This function decrypts the
    # encrypted text and returns
    # the original text
    def originalText(self,cipher_text, key):
        orig_text = []
        for i in range(len(cipher_text)):
            x = (ord(cipher_text[i]) - ord(key[i]) + 26) % 26
            x += ord('A')
            orig_text.append(chr(x))
        return ("".join(orig_text))

    # Driver code
    def call_vignere_cipher(self):
        string = self.text.upper()
        keyword =input("Enter the Key : ").upper()
        key = self.generateKey(string, keyword)
        cipher_text = self.vignereCipherText(string,key)
        print("Ciphertext :", cipher_text)
        print("Original/Decrypted Text :",self.originalText(cipher_text, key))






    def convertPlainTextToDiagraphs(self,plainText):
        # append X if Two letters are being repeated
        for s in range(0, len(plainText) + 1, 2):
            if s < len(plainText) - 1:
                if plainText[s] == plainText[s + 1]:
                    plainText = plainText[:s + 1] + 'X' + plainText[s + 1:]

        # append X if the total letters are odd, to make plaintext even
        if len(plainText) % 2 != 0:
            plainText = plainText[:] + 'X'

        return plainText

    def generateKeyMatrix(self,key):
        # Intially Create 5X5 matrix with all values as 0
        # [
        #   [0, 0, 0, 0, 0],
        #   [0, 0, 0, 0, 0],
        #   [0, 0, 0, 0, 0],
        #   [0, 0, 0, 0, 0],
        #   [0, 0, 0, 0, 0]
        # ]
        matrix_5x5 = [[0 for i in range(5)] for j in range(5)]

        simpleKeyArr = []

        """
         Generate SimpleKeyArray with key from user Input 
         with following below condition:
         1. Character Should not be repeated again
         2. Replacing J as I (as per rule of playfair cipher)
        """
        for c in key:
            if c not in simpleKeyArr:
                if c == 'J':
                    simpleKeyArr.append('I')
                else:
                    simpleKeyArr.append(c)

        """
        Fill the remaining SimpleKeyArray with rest of unused letters from english alphabets 
        """

        is_I_exist = "I" in simpleKeyArr

        # A-Z's ASCII Value lies between 65 to 90 but as range's second parameter excludes that value we will use 65 to 91
        for i in range(65, 91):
            if chr(i) not in simpleKeyArr:
                # I = 73
                # J = 74
                # We want I in simpleKeyArr not J

                if i == 73 and not is_I_exist:
                    simpleKeyArr.append("I")
                    is_I_exist = True
                elif i == 73 or i == 74 and is_I_exist:
                    pass
                else:
                    simpleKeyArr.append(chr(i))

        """
        Now map simpleKeyArr to matrix_5x5 
        """
        index = 0
        for i in range(0, 5):
            for j in range(0, 5):
                matrix_5x5[i][j] = simpleKeyArr[index]
                index += 1

        return matrix_5x5

    def indexLocator(self,char, cipherKeyMatrix):
        indexOfChar = []

        # convert the character value from J to I
        if char == "J":
            char = "I"

        for i, j in enumerate(cipherKeyMatrix):
            # enumerate will return object like this:
            # [
            #   (0, ['K', 'A', 'R', 'E', 'N']),
            #   (1, ['D', 'B', 'C', 'F', 'G']),
            #   (2, ['H', 'I', 'L', 'M', 'O']),
            #   (3, ['P', 'Q', 'S', 'T', 'U']),
            #   (4, ['V', 'W', 'X', 'Y', 'Z'])
            # ]
            # i,j will map to tupels of above array

            # j refers to inside matrix =>  ['K', 'A', 'R', 'E', 'N'],
            for k, l in enumerate(j):
                # again enumerate will return object that look like this in first iteration:
                # [(0,'K'),(1,'A'),(2,'R'),(3,'E'),(4,'N')]
                # k,l will map to tupels of above array
                if char == l:
                    indexOfChar.append(i)  # add 1st dimension of 5X5 matrix => i.e., indexOfChar = [i]
                    indexOfChar.append(k)  # add 2nd dimension of 5X5 matrix => i.e., indexOfChar = [i,k]
                    return indexOfChar

                # Now with the help of indexOfChar = [i,k] we can pretty much locate every element,
                # inside our 5X5 matrix like this =>  cipherKeyMatrix[i][k]

    def playfairencryption(self,plainText, key):
        cipherText = []
        # 1. Generate Key Matrix
        keyMatrix = self.generateKeyMatrix(key)

        # 2. Encrypt According to Rules of playfair cipher
        i = 0
        while i < len(plainText):
            # 2.1 calculate two grouped characters indexes from keyMatrix
            n1 = self.indexLocator(plainText[i], keyMatrix)
            n2 = self.indexLocator(plainText[i + 1], keyMatrix)

            # 2.2  if same column then look in below row so
            # format is [row,col]
            # now to see below row => increase the row in both item
            # (n1[0]+1,n1[1]) => (3+1,1) => (4,1)

            # (n2[0]+1,n2[1]) => (4+1,1) => (5,1)

            # but in our matrix we have 0 to 4 indexes only
            # so to make value bound under 0 to 4 we will do %5
            # i.e.,
            #   (n1[0]+1 % 5,n1[1])
            #   (n2[0]+1 % 5,n2[1])

            if n1[1] == n2[1]:
                i1 = (n1[0] + 1) % 5
                j1 = n1[1]

                i2 = (n2[0] + 1) % 5
                j2 = n2[1]
                cipherText.append(keyMatrix[i1][j1])
                cipherText.append(keyMatrix[i2][j2])
                cipherText.append(", ")

            # same row
            elif n1[0] == n2[0]:
                i1 = n1[0]
                j1 = (n1[1] + 1) % 5

                i2 = n2[0]
                j2 = (n2[1] + 1) % 5
                cipherText.append(keyMatrix[i1][j1])
                cipherText.append(keyMatrix[i2][j2])
                cipherText.append(", ")


            # if making rectangle then
            # [4,3] [1,2] => [4,2] [3,1]
            # exchange columns of both value
            else:
                i1 = n1[0]
                j1 = n1[1]

                i2 = n2[0]
                j2 = n2[1]

                cipherText.append(keyMatrix[i1][j2])
                cipherText.append(keyMatrix[i2][j1])
                cipherText.append(", ")

            i += 2
        return cipherText

    def call_playfair(self):

        # Getting user inputs Key (to make the 5x5 char matrix) and Plain Text (Message that is to be encripted)
        self.playfairkey = input("Enter key: ").replace(" ", "").upper()
        self.playfairmessage = self.text.replace(" ", "").upper()

        convertedPlainText = self.convertPlainTextToDiagraphs(self.playfairmessage)

        cipherText = " ".join(self.playfairencryption(convertedPlainText, self.playfairkey))
        print(cipherText)





    def encryption(self,m):
        # Replace spaces with nothing
        m = m.replace(" ", "")
        # Ask for keyword and get encryption matrix
        C = self.make_key()
        # Append zero if the messsage isn't divisble by 2
        len_check = len(m) % 2 == 0
        if not len_check:
            m += "0"
        # Populate message matrix
        P = self.create_matrix_of_integers_from_string(m)
        # Calculate length of the message
        m_len = int(len(m) / 2)
        # Calculate P * C
        encrypted_m = ""
        for i in range(m_len):
            # Dot product
            row_0 = P[0][i] * C[0][0] + P[1][i] * C[0][1]
            # Modulate and add 65 to get back to the A-Z range in ascii
            integer = int(row_0 % 26 + 65)
            # Change back to chr type and add to text
            self.en_m += chr(integer)
            # Repeat for the second column
            row_1 = P[0][i] * C[1][0] + P[1][i] * C[1][1]
            integer = int(row_1 % 26 + 65)
            self.en_m += chr(integer)
        return self.en_m

    def decryption(self,en_m):
        # Ask for keyword and get encryption matrix
        C = self.make_key()
        # Inverse matrix
        determinant = C[0][0] * C[1][1] - C[0][1] * C[1][0]
        determinant = determinant % 26
        multiplicative_inverse = self.find_multiplicative_inverse(determinant)
        C_inverse = C
        # Swap a <-> d
        C_inverse[0][0], C_inverse[1][1] = C_inverse[1, 1], C_inverse[0, 0]
        # Replace
        C[0][1] *= -1
        C[1][0] *= -1
        for row in range(2):
            for column in range(2):
                C_inverse[row][column] *= multiplicative_inverse
                C_inverse[row][column] = C_inverse[row][column] % 26
        P = self.create_matrix_of_integers_from_string(en_m)
        m_len = int(len(en_m) / 2)
        de_m = ""
        for i in range(m_len):
            # Dot product
            column_0 = P[0][i] * C_inverse[0][0] + P[1][i] * C_inverse[0][1]
            # Modulate and add 65 to get back to the A-Z range in ascii
            integer = int(column_0 % 26 + 65)
            # Change back to chr type and add to text
            de_m += chr(integer)
            # Repeat for the second column
            column_1 = P[0][i] * C_inverse[1][0] + P[1][i] * C_inverse[1][1]
            integer = int(column_1 % 26 + 65)
            de_m += chr(integer)
        if de_m[-1] == "0":
            de_m = de_m[:-1]
        return de_m

    def find_multiplicative_inverse(self,determinant):
        multiplicative_inverse = -1
        for i in range(26):
            inverse = determinant * i
            if inverse % 26 == 1:
                multiplicative_inverse = i
                break
        return multiplicative_inverse

    def make_key(self):
        # Make sure cipher determinant is relatively prime to 26 and only a/A - z/Z are given
        determinant = 0
        C = None
        while True:
            cipher = input("Input 4 letter cipher: ").upper()
            C = self.create_matrix_of_integers_from_string(cipher)
            determinant = C[0][0] * C[1][1] - C[0][1] * C[1][0]
            determinant = determinant % 26
            inverse_element = self.find_multiplicative_inverse(determinant)
            if inverse_element == -1:
                print("Determinant is not relatively prime to 26, uninvertible key")
            elif np.amax(C) > 26 and np.amin(C) < 0:
                print("Only a-z characters are accepted")
                print(np.amax(C), np.amin(C))
            else:
                break
        return C

    def create_matrix_of_integers_from_string(self,string):
        # Map string to a list of integers a/A <-> 0, b/B <-> 1 ... z/Z <-> 25
        integers = [self.chr_to_int(c) for c in string]
        length = len(integers)
        M = np.zeros((2, int(length / 2)), dtype=np.int32)
        iterator = 0
        for column in range(int(length / 2)):
            for row in range(2):
                M[row][column] = integers[iterator]
                iterator += 1
        return M

    def chr_to_int(self,char):
        # Uppercase the char to get into range 65-90 in ascii table
        char = char.upper()
        # Cast chr to int and subtract 65 to get 0-25
        integer = ord(char) - 65
        return integer

    def callHillCipher(self):
        m = self.text.upper()
        self.en_m = self.encryption(m)
        print(self.en_m)
        de_m = self.decryption(self.en_m)
        print(de_m)





    def encryptRailFence(self,text, key):

        # create the matrix to cipher
        # plain text key = rows ,
        # length(text) = columns
        # filling the rail matrix
        # to distinguish filled
        # spaces from blank ones
        rail = [['\n' for i in range(len(text))]
                for j in range(key)]

        # to find the direction
        dir_down = False
        row, col = 0, 0

        for i in range(len(text)):

            # check the direction of flow
            # reverse the direction if we've just
            # filled the top or bottom rail
            if (row == 0) or (row == key - 1):
                dir_down = not dir_down

            # fill the corresponding alphabet
            rail[row][col] = text[i]
            col += 1

            # find the next row using
            # direction flag
            if dir_down:
                row += 1
            else:
                row -= 1
        # now we can construct the cipher
        # using the rail matrix
        result = []
        for i in range(key):
            for j in range(len(text)):
                if rail[i][j] != '\n':
                    result.append(rail[i][j])
        return ("".join(result))

    # This function receives cipher-text
    # and key and returns the original
    # text after decryption
    def decryptRailFence(self,cipher, key):

        # create the matrix to cipher
        # plain text key = rows ,
        # length(text) = columns
        # filling the rail matrix to
        # distinguish filled spaces
        # from blank ones
        rail = [['\n' for i in range(len(cipher))]
                for j in range(key)]

        # to find the direction
        dir_down = None
        row, col = 0, 0

        # mark the places with '*'
        for i in range(len(cipher)):
            if row == 0:
                dir_down = True
            if row == key - 1:
                dir_down = False

            # place the marker
            rail[row][col] = '*'
            col += 1

            # find the next row
            # using direction flag
            if dir_down:
                row += 1
            else:
                row -= 1

        # now we can construct the
        # fill the rail matrix
        index = 0
        for i in range(key):
            for j in range(len(cipher)):
                if ((rail[i][j] == '*') and
                        (index < len(cipher))):
                    rail[i][j] = cipher[index]
                    index += 1

        # now read the matrix in
        # zig-zag manner to construct
        # the resultant text
        result = []
        row, col = 0, 0
        for i in range(len(cipher)):

            # check the direction of flow
            if row == 0:
                dir_down = True
            if row == key - 1:
                dir_down = False

            # place the marker
            if (rail[row][col] != '*'):
                result.append(rail[row][col])
                col += 1

            # find the next row using
            # direction flag
            if dir_down:
                row += 1
            else:
                row -= 1
        return ("".join(result))


    # Driver code
    def callRailFenceCipher(self):
        inp=self.text.upper()
        key_len=int(input("Enter a number less than the length of the text : "))
        encryp = self.encryptRailFence(inp, key_len)
        print(encryp)
        # Now decryption of the
        # same cipher-text
        print(self.decryptRailFence(encryp, key_len))


#-------------------------------------------------------------------------------------------------------


    def encryptOTP(self,msg, key):

        ciphertext = ''
        for idx, char in enumerate(msg):
            charIdx = self.abc.index(char)
            keyIdx = self.one_time_pad.index(key[idx])

            cipher = (keyIdx + charIdx) % len(self.one_time_pad)
            ciphertext += self.abc[cipher]

        return ciphertext


    def decryptOTP(self,ciphertext, key):

        if ciphertext == '' or key == '':
            return ''

        charIdx = self.abc.index(ciphertext[0])
        keyIdx = self.one_time_pad.index(key[0])

        cipher = (charIdx - keyIdx) % len(self.one_time_pad)
        char = self.abc[cipher]

        return char + self.decryptOTP(ciphertext[1:], key[1:])


    def callOTP(self):

        availableOpt = ["-d", "-e"]
        if len(sys.argv) == 1 or sys.argv[1] not in availableOpt:
            print(help)
            exit(0)

        key = input("Enter The Key: ")
        msg = self.text.upper()

        if sys.argv[1] == availableOpt[1]:
            print(self.encryptOTP(msg, key))
        elif sys.argv[1] == availableOpt[0]:
            print(self.decryptOTP(msg, key))



    # Encryption
    def encryptMessage(self,msg):
        cipher = ""

        # track key indices
        k_indx = 0

        msg_len = float(len(msg))
        msg_lst = list(msg)
        key_lst = sorted(list(self.ROTkey))

        # calculate column of the matrix
        col = len(self.ROTkey)

        # calculate maximum row of the matrix
        row = int(math.ceil(msg_len / col))

        # add the padding character '_' in empty
        # the empty cell of the matix
        fill_null = int((row * col) - msg_len)
        msg_lst.extend('_' * fill_null)

        # create Matrix and insert message and
        # padding characters row-wise
        matrix = [msg_lst[i: i + col]
                  for i in range(0, len(msg_lst), col)]

        # read matrix column-wise using key
        for _ in range(col):
            curr_idx = self.ROTkey.index(key_lst[k_indx])
            cipher += ''.join([row[curr_idx]
                               for row in matrix])
            k_indx += 1

        return cipher

    # Decryption
    def decryptMessage(self,cipher):
        msg = ""

        # track key indices
        k_indx = 0

        # track msg indices
        msg_indx = 0
        msg_len = float(len(cipher))
        msg_lst = list(cipher)

        # calculate column of the matrix
        col = len(self.ROTkey)

        # calculate maximum row of the matrix
        row = int(math.ceil(msg_len / col))

        # convert key into list and sort
        # alphabetically so we can access
        # each character by its alphabetical position.
        key_lst = sorted(list(self.ROTkey))

        # create an empty matrix to
        # store deciphered message
        dec_cipher = []
        for _ in range(row):
            dec_cipher += [[None] * col]

        # Arrange the matrix column wise according
        # to permutation order by adding into new matrix
        for _ in range(col):
            curr_idx = self.ROTkey.index(key_lst[k_indx])

            for j in range(row):
                dec_cipher[j][curr_idx] = msg_lst[msg_indx]
                msg_indx += 1
            k_indx += 1

        # convert decrypted msg matrix into a string
        try:
            msg = ''.join(sum(dec_cipher, []))
        except TypeError:
            raise TypeError("This program cannot",
                            "handle repeating words.")

        null_count = msg.count('_')

        if null_count > 0:
            return msg[: -null_count]

        return msg

    # Driver Code
    def callRowTransformation(self):
        msg = self.text.upper()
        self.ROTkey=input(" Enter The Numeric Key ")
        cipher = self.encryptMessage(msg)
        print("Encrypted Message: {}".format(cipher))
        print("Decryped Message: {}".format(self.decryptMessage(cipher)))