Alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
Rottor3 = [0,1,3,7,15,4,9,19,0,2,5,11,21,12,25,14,24,16,8,17,22,20,10,23,18,6,2,13,13]## числа соответсвуют индексам букв английского алфавита начиная с 0
Rottor2 = [5,8,23,21,24,14,12,22,5,2,3,10,11,7,20,15,2,4,18,25,4,1,9,1,6,17,6,13,19,13,0,0,16,16]
Rottor1 = [0,4,11,19,15,7,16,23,17,20,0,1,10,13,22,1,2,12,14,24,2,3,5,6,3,8,21,8,9,25,9,18,18]
Reflector_B = [0,24,0,1,17,1,2,20,2,3,7,3,4,16,4,5,18,5,6,11,6,8,15,8,9,23,9,10,13,10,12,14,12,19,25,19,21,22,21]##reflector type - B
Array = Alphabet.copy()
Commutator = [0, 1, 0, 2, 3, 2, 4, 5, 4, 6, 7, 6, 8, 9, 8, 10, 11, 10, 12, 13, 12, 14, 15, 14, 16, 22, 16, 17, 18, 17, 19, 20, 19, 21, 23, 21, 24, 25, 24]## plague board   

class Machine:
    def __init__(self, R, M, L):
        self.R = R
        self.M = M
        self.L = L
        self.String = str()
        self.sentense = str()
        
##    def imput(self, letter):
##        self.letter = letter
##        print(self.letter)       
    def compute(self, letter):
        R = self.R
        M = self.M
        L = self.L
        self.letter = letter
##        sentense = self.sentense
##        String = self.String
##        for g in range(1):
##            for a in range(len(sentense)):
                
##        letter = sentense[a]
        self.letter = Alphabet.index(self.letter)
        self.letter = Commutator[Commutator.index(self.letter)+1]

        R += 1
        if R == 22:
            M += 1
            if M == 5:
                 L += 1
                 if L == 26:
                    L = 0
            elif M == 26:
                M = 0
        elif R == 26:
            R = 0
                      
        i = (self.letter + R) % 26
        m = Rottor3[Rottor3.index(i)+1]
        i = (m + (M - R)) % 26           
        m = Rottor2[Rottor2.index(i)+1]
        i = (m + (L - M)) % 26
        m = Rottor1[Rottor1.index(i)+1]
        i = (m - L) % 26
        m = Reflector_B[Reflector_B.index(i)+1]
        i = (m + L) % 26
        Rottor1.reverse()        
        m = Rottor1[Rottor1.index(i)+1]
        i = (m - (L - M)) % 26
        Rottor2.reverse()
        m = Rottor2[Rottor2.index(i)+1]
        i = (m - (M - R)) % 26
        Rottor3.reverse()
        m = Rottor3[Rottor3.index(i)+1]
        i = (m - R) % 26
        self.letter = Commutator[Commutator.index(i)+1]

        Rottor1.reverse()
        Rottor2.reverse()
        Rottor3.reverse()
        
##        String += Alphabet[m]
        self.letter = Alphabet[self.letter]
        print(self.letter)
        return self.letter
        
        

