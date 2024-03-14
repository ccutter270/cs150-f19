"""
CSCI150 Test Project 1

Name: Caroline Cutter
Section: <B>
"""

#Constants

    #length of codon - makes code more clear

CODON_LEN = 3


#My Functions Below


def is_stop(codon):
    '''
    Returns True if the codon entered is a stop codon and False otherwise
    
    Args:
        codon: a three letter sequence containing the letters 'A', 'T', 'G', and 'C'
    
    Returns:
        If 'codon' is a stop codon or not
    
    '''
    return (codon == 'TGA' or codon == 'TAG' or codon == 'TAA')

    


def orf_sequence(sequence):
    '''
    Extracts and returns an ORF from a DNA sequence that begins with a start codon
    
    Args:
        sequence: a DNA sequence that begins with a start codon
        
    Returns:
        an ORF as a string from 'sequence'
    '''
    orf = ''
    index = 0
    for codons in range(0, len(sequence), CODON_LEN):
        codon = str(sequence[index : index + CODON_LEN])
        if is_stop(codon) == True:
            break
        else:
            orf += codon
        index += CODON_LEN
    
    return orf
        
 
 
 

def find_orfs(sequence):
    '''
    Takes a DNA sequence as a string and returns a list of OFRs in the DNA sequence
    
    Args:
        sequence: a DNA sequence in the form of a string
        
    Returns:
        a list of ORFs as strings in the parameter 'sequence'
    '''
    orfs = []
    index = 0
    while index <= len(sequence):
        codon = str(sequence[index : index + CODON_LEN])
        if codon == 'ATG':
            orf = orf_sequence(sequence[index:])
            orfs.append(orf)
            index += len(orf)
        else:
            index += CODON_LEN
    
    return orfs
            
 





def reverse_complement(sequence):
    '''
    Takes a DNA sequence as a string and returns the reverse complement of the DNA sequence as a string. The reverse complement is
    the DNA sequence in reverse order and with the nucleotides replaced with their base pairs
    
    Args:
        sequence: a DNA sequence as a string
    
    Returns:
        the reverse complement of the parameter 'sequence'

    '''
    #Reverse the sequence
    sequence = sequence[::-1]
    #Replace base pairs
    #Using "X" as placeholder because if changing all Ts to As then all As to Ts, then there will only be Ts
    complement = sequence.replace('T', 'X').replace('A', 'T').replace('X', 'A').replace('C', 'X').replace('G', 'C').replace('X', 'G')
    
    return complement
   
   

def gene_finder(sequence):
    '''
    Takes a DNA sequence and returns a list of strings that are valid ORFS for a DNA sequence and its reverse complement.
    
    Args:
        sequence: a DNA sequence as a string
        
    Returns:
        all possible ORFs in the paremeter 'sequence'
    '''
    #possible genes for sequence (in all 3 frames)
    possible_genes = find_orfs(sequence) + find_orfs(sequence[1:]) + find_orfs(sequence[2:])

    
    #possible genes for reverse complement of sequence (in all 3 frames)
    possible_genes += find_orfs(reverse_complement(sequence)) + find_orfs((reverse_complement(sequence))[1:]) + find_orfs((reverse_complement(sequence))[2:])
    
    return possible_genes











#Given Functions

def read_fasta(filename):
    """
    Read a single DNA sequence from a FASTA-formatted file
    
    For example, to read the sequence from a file named "X73525.fasta.txt"
    >>> sequence = read_fasta("X73525.fasta.txt")
    
    Args:
        filename: Filename as a string
        
    Returns: Upper case DNA sequence as a string
    """
    with open(filename, "r") as file:
        # Read (and ignore) header line
        header = file.readline()
        # Read sequence lines
        sequence = ""
        for line in file:
            sequence += line.strip()
        return sequence.upper()


def filter_orfs(orfs, min_length):
    """
    Filter ORFs to have a minimum length
    
    Args:
        orfs: List of candidate ORF sequences
        min_length: Minimum length for an ORF
    
    Returns:
        A new list containing only ORF strings longer than min_length bases
    """
    filtered_orfs = []
    for orf in orfs:
        if len(orf) > min_length:
            filtered_orfs.append(orf)
    return filtered_orfs


def write_fasta(filename, orfs):
    """
    Write list of ORFs to a FASTA formatted text file.
    
    For example, to save a list of orfs assigned to the variable my_orfs to a
    file named "genes.txt"
    >>> write_fasta("genes.txt", my_orfs)
    
    Args:
        filename: Filename as a string. Note that any existing file with this name
            will be overwritten.
        orfs: List of ORF sequences to write to the file
    """
    with open(filename, "w") as file:
        for i in range(len(orfs)):
            # A FASTA entry is a header line that begins with a '>', and then the sequence on the next line(s)
            print(">seq" + str(i), file=file)
            print(orfs[i], file=file)

     


  
     
if __name__ == "__main__":
    sequence = read_fasta('X73525.fasta.txt')
    ORFs = gene_finder(sequence)
    filtered_orfs = filter_orfs(ORFs, 690)
    write_fasta('genes.txt', filtered_orfs)