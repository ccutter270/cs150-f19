'''
Lecture 11: Lab 5
Friday, October 11th
'''

def read_filename(filename):
        with open(filename, "r") as file:
            counts = []
            for line in file:
                counts.append(int(line.strip()))
            print(counts)
                
                
            
def freq(counts):
    return sum(counts) / (2 * len(counts))


def allele_freq(filename):