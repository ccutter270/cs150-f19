'''
PreLab 3
Wednesday, Sept 25
'''

#Encryptions

ALPHABET = "abcdefghijklmnopqrstuvwxyz "
key = "hvieksyrbdajqwncxmgufltp oz"




#Problem 5

letter = "a"


'''
Finds index of the character in alphabet

'''

def find_letter(string, letter):
    i = 0
    while i < len(string):
        if string[i] == letter:
            return i
        i = i + 1

   
'''OR'''

print(ALPHABET.find(letter))


#Problem 6

'''
returns encrypted letter 

'''

def encrypted(letter):
     ALPHABET = "abcdefghijklmnopqrstuvwxyz "
     key = "hvieksyrbdajqwncxmgufltp oz"
     index = ALPHABET.find(letter)
     return key[index]
    
    
    
#in expression form
    
key[ALPHABET.find(letter)]
